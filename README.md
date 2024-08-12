https://github.com/linuxacademy/la-aws-security_specialty/tree/master/Enabling-VPC-Flow-Logs-with-Automation

https://github.com/linuxacademy/content-lambda-boto3


-----------------


SSH into EC2 instance


ssh -i id_rsa -l ec2-user ec2-35-176-140-146.eu-west-2.compute.amazonaws.com

ssh -i ~/.ssh/id_rsa -l ec2-user ec2-35-176-140-146.eu-west-2.compute.amazonaws.com


-----

In AWS Linux 2 instance

pip3 install boto3 --user

Use python3


Configure profile

aws configure

Then use

aws sts get-caller-identity

{
    "Account": "360057177229", 
    "UserId": "AIDAVHVIUQSG5R4RUNWNN", 
    "Arn": "arn:aws:iam::360057177229:user/acg_course"
}

--------------------

Alternatively for local use:

*create virtual environment*

python3 -m venv acg-env    
source ./acg-env/bin/activate  
pip3 install boto3             

and to exit virtual environment

*deactivate*

--------------------


[ec2-user@ip-172-31-22-180 ~]$ python3
Python 3.7.16 (default, May  6 2024, 19:30:00) 
[GCC 7.3.1 20180712 (Red Hat 7.3.1-17)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> s3 = boto3.resource('s3')
/home/ec2-user/.local/lib/python3.7/site-packages/boto3/compat.py:82: PythonDeprecationWarning: Boto3 will no longer support Python 3.7 starting December 13, 2023. To continue receiving service updates, bug fixes, and security updates please upgrade to Python 3.8 or later. More information can be found here: https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/
  warnings.warn(warning, PythonDeprecationWarning)
>>> for bucket in s3.buckets.all():
...     print(bucket.name)
... 
amplify-ampbasic-dev-17d5a-deployment
amplify-b2bdeploy-dev-1bdbf-deployment
amplify-bk2basebasic-dev-7eba0-deployment
amplify-bk2baseimgscorer-dev-15b89-deployment
amplify-bk2bbasic-dev-87878-deployment
amplify-figmatest-staging-d0385-deployment
aws-codedeploy-nodejs-eu-west-2
aws-sam-cli-managed-default-samclisourcebucket-jov8sonxzg8n
cdk-hnb659fds-assets-360057177229-us-east-1
el-laep-dev-access-log
el-laep-dev-input
el-laep-dev-output
el-terraform-state
esc-laep-dev-access-log
esc-laep-dev-environment
esc-laep-dev-input
esc-laep-dev-output
lunch-and-learn-demo-data
s3images7eba0-dev
>>>

Find the AMI id:
ami-0efebcf6b293598fa


>>> ec2 = boto3.client('ec2')
>>> response = ec2.run_instances(
...     ImageId='ami-0efebcf6b293598fa',
...     InstanceType='t2.micro',
...     KeyName='acg-key-pair',
...     MinCount=1,
...     MaxCount=1
... )
>>> response
{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-0efebcf6b293598fa', 'InstanceId': 'i-0db478e8add2c99f8', 'InstanceType': 't2.micro', 'KeyName': 'acg-key-pair', 'LaunchTime': datetime.datetime(2024, 8, 5, 12, 52, 11, tzinfo=tzlocal()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'eu-west-2a', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-21-82.eu-west-2.compute.internal', 'PrivateIpAddress': '172.31.21.82', 'ProductCodes': [], 'PublicDnsName': '', 'State': {'Code': 0, 'Name': 'pending'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-c4dc46be', 'VpcId': 'vpc-1313477b', 'Architecture': 'x86_64', 'BlockDeviceMappings': [], 'ClientToken': 'ccdc9521-8c89-4318-9f74-d9b7b60bbecf', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Attachment': {'AttachTime': datetime.datetime(2024, 8, 5, 12, 52, 11, tzinfo=tzlocal()), 'AttachmentId': 'eni-attach-03139234dae0ed415', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attaching', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-aea3e4c9'}], 'Ipv6Addresses': [], 'MacAddress': '06:41:d1:9c:46:f5', 'NetworkInterfaceId': 'eni-0fc070789684407bd', 'OwnerId': '360057177229', 'PrivateDnsName': 'ip-172-31-21-82.eu-west-2.compute.internal', 'PrivateIpAddress': '172.31.21.82', 'PrivateIpAddresses': [{'Primary': True, 'PrivateDnsName': 'ip-172-31-21-82.eu-west-2.compute.internal', 'PrivateIpAddress': '172.31.21.82'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-c4dc46be', 'VpcId': 'vpc-1313477b', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-aea3e4c9'}], 'SourceDestCheck': True, 'StateReason': {'Code': 'pending', 'Message': 'pending'}, 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'MetadataOptions': {'State': 'pending', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default'}, 'CurrentInstanceBootMode': 'legacy-bios'}], 'OwnerId': '360057177229', 'ReservationId': 'r-09c2f02f841d41b09', 'ResponseMetadata': {'RequestId': 'ffbf3336-adb9-4ad2-bbc2-b69ebe22aaf1', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'ffbf3336-adb9-4ad2-bbc2-b69ebe22aaf1', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '5570', 'date': 'Mon, 05 Aug 2024 12:52:11 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
>>>


CreateEC2

Role: CreateEC2-role-z2wr2cij

update policy

{
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Action": [
        "ec2:RunInstances"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}


Code for lambda

import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)


In Lambda Configuration set up environment variables

SUBNET_ID need to find a public one.


vpc-1313477b

subnet-c4dc46be

--------------------------


Stopping EC2 instances
----------------------


lambda_start_stop_instances

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeRegions",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}

import boto3


def lambda_handler(event, context):

    # Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    # Iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

        # Get only running instances
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['running']}])

        # Stop the instances
        for instance in instances:
            instance.stop()
            print('Stopped instance: ', instance.id)


------------------


Deregistering AMIs

import datetime
from dateutil.parser import parse

import boto3


def days_old(date):
    parsed = parse(date).replace(tzinfo=None)
    diff = datetime.datetime.now() - parsed
    return diff.days


def lambda_handler(event, context):

    # Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        ec2 = boto3.client('ec2', region_name=region)
        print("Region:", region)

        amis = ec2.describe_images(Owners=['self'])['Images']

        for ami in amis:
            creation_date = ami['CreationDate']
            age_days = days_old(creation_date)
            image_id = ami['ImageId']
            print('ImageId: {}, CreationDate: {} ({} days old)'.format(
                image_id, creation_date, age_days))

            if age_days >= 2:
                print('Deleting ImageId:', image_id)

                # Deregister the AMI
                ec2.deregister_image(ImageId=image_id)


-----------------------------------

Didn't work:

- AWS Instance Scheduler
- Enabling-VPC-Flow-Logs-with-Automation
