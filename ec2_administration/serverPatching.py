import boto3
import logging
import time

ec2=boto3.client('ec2')
logging.basicConfig(encoding='utf-8', level=logging.INFO)

def getRegion():
    regions = ec2.describe_regions()
    regionList = []
    for i in regions["Regions"]:
        region = i['RegionName']
        regionList.append(region)
    return regionList 

def tagProcessing(tags):
    for tag in tags:
        if tag.get('Key') == 'Patching' and tag.get('Value') == 'yes':
            return True
    return False

def getInstances():
    regions = getRegion()
    for region in regions:
        instanceSet = set()
        regionViseEc2 = boto3.client('ec2', region_name = region) 
        serverList=regionViseEc2.describe_instances()
        for instances in serverList["Reservations"]:
            for server in instances["Instances"]:
                instnaceState = server["State"]
                if instnaceState['Name'] == "running":
                    if tagProcessing(server['Tags']):
                        instanceSet.add(server["InstanceId"])
                    else:
                        logging.info('{} is skipped due to no patching tag..'.format(server["InstanceId"]))
                else:
                    logging.info(f'{server["InstanceId"]} is in {instnaceState['Name']} state..')
        ssmConnectionCheck(instanceSet,region)                          

def states(instance, actualStatus):
    if actualStatus == 'Pending':
        logging.info(f"{instance} is {actualStatus}: The command hasn't been sent to the server.")
        time.sleep(5)
    elif actualStatus == 'InProgress':
        logging.info(f"{instance} is {actualStatus}.")
        time.sleep(10)
    elif actualStatus == 'Delayed':
        logging.warning(f"{instance} is {actualStatus}:") 
        logging.warning("The system attempted to send the command to the managed node but wasn't successful. The system retries again.")  
        time.sleep(10)
    elif actualStatus == 'Success':
        logging.info(f"{instance} is {actualStatus}.")
        return "done"          
    elif actualStatus == 'Cancelled':
        logging.info(f"{instance} is {actualStatus}.")
        return "done" 
    elif actualStatus == 'TimedOut':
        logging.critical(f"{instance} is {actualStatus}:")
        logging.critical("Command execution started on the managed node, but the execution wasn't complete before the execution timeout expired.")
        return "done" 
    
def initiatePatchBaseLine(ssm, instances, region):
    if instances:
        response = ssm.send_command(
        InstanceIds= list(instances),
        DocumentName="AWS-RunPatchBaseline",
        Parameters={
        'Operation': ['Scan']},
        Comment='Initiating Scan from python',
        )
        commandID = response['Command']['CommandId']
        logging.info (f"Initiating patch {response['Command']['Parameters']['Operation'][0]} with Command ID: {commandID} in {region} region")
        for instance in response['Command']['InstanceIds']:
            time.sleep(5)
            while True:
                instanceStatus = ssm.list_command_invocations(
                    CommandId = commandID,
                    InstanceId = instance,
                    Details=True)
                terminator = states(instance, instanceStatus['CommandInvocations'][0]['StatusDetails'])
                if terminator == 'done':
                    break

def ssmConnectionCheck(instances,region):
    ssm = boto3.client('ssm', region_name=region)
    validInstanceSet = set()
    invalidInstanceSet = set()
    for instance in instances:
        response = ssm.describe_instance_information()
        if response['InstanceInformationList']:
            validInstanceSet.add(instance) 
        else:
            invalidInstanceSet.add(instance)
            logging.info(f"{instance} SSM is not worinking | {region}")
    initiatePatchBaseLine(ssm, validInstanceSet, region)    

def main():
    getInstances()

main()
                  
 
