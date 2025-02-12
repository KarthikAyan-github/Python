import boto3
ec2 = boto3.client('ec2')
servers = ec2.describe_instances()
instanceIds = servers["Reservations"][0]["Instances"][0]["InstanceId"]
response=ec2.stop_instances(InstanceIds=[instanceIds])
print(response)