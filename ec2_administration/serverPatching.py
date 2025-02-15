import boto3
import logging

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

def initiatePatchBaseLine(instances, region):
    if instances:
        ssm = boto3.client('ssm', region_name=region)
        response = ssm.send_command(
        InstanceIds= list(instances),
        DocumentName="AWS-RunPatchBaseline",
        Parameters={
        'Operation': ['Scan']},
        Comment='Initiating Scan from python',
        )
        logging.info ("Initiating patch scan for: \n")
        for instance in response['Command']['InstanceIds']:
            logging.info(f"{instance} command ID is {response['Command']['CommandId']}")

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
    initiatePatchBaseLine(validInstanceSet, region)    


def main():
    getInstances()
    
main()
                  
 
