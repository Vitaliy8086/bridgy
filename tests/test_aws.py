# import __builtin__
#
# import mock
# import pytest
# import shlex
#
# from bridgy.inventory import Instance
# from bridgy.inventory.aws import AwsInventory
# from bridgy.config import Config
#
# DATA = """
# {
#     "status_code": 200,
#     "data": {
#         "Reservations": [
#             {
#                 "Instances": [
#                     {
#                         "Monitoring": {
#                             "State": "disabled"
#                         },
#                         "StateReason": {
#                             "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
#                             "Code": "Client.UserInitiatedShutdown"
#                         },
#                         "PublicDnsName": "devbox",
#                         "Platform": "windows",
#                         "State": {
#                             "Code": 80,
#                             "Name": "stopped"
#                         },
#                         "EbsOptimized": false,
#                         "LaunchTime": {
#                             "hour": 19,
#                             "__class__": "datetime",
#                             "month": 12,
#                             "second": 20,
#                             "microsecond": 0,
#                             "year": 2014,
#                             "day": 12,
#                             "minute": 35
#                         },
#                         "PrivateIpAddress": "172.31.8.185",
#                         "ProductCodes": [],
#                         "VpcId": "vpc-22de0647",
#                         "StateTransitionReason": "User initiated (2014-12-12 23:00:05 GMT)",
#                         "InstanceId": "i-e54cbaeb",
#                         "ImageId": "ami-a13d6891",
#                         "PrivateDnsName": "ip-172-31-8-185.us-west-2.compute.internal",
#                         "KeyName": "smithKeypair",
#                         "SecurityGroups": [
#                             {
#                                 "GroupName": "launch-wizard-1",
#                                 "GroupId": "sg-80572fe5"
#                             }
#                         ],
#                         "ClientToken": "sZIsp1418412919870",
#                         "SubnetId": "subnet-29798e70",
#                         "InstanceType": "t2.micro",
#                         "NetworkInterfaces": [
#                             {
#                                 "Status": "in-use",
#                                 "MacAddress": "0a:1c:55:d3:fb:bf",
#                                 "SourceDestCheck": true,
#                                 "VpcId": "vpc-22de0647",
#                                 "Description": "",
#                                 "NetworkInterfaceId": "eni-751e332c",
#                                 "PrivateIpAddresses": [
#                                     {
#                                         "PrivateDnsName": "ip-172-31-8-185.us-west-2.compute.internal",
#                                         "Primary": true,
#                                         "PrivateIpAddress": "172.31.8.185"
#                                     }
#                                 ],
#                                 "PrivateDnsName": "ip-172-31-8-185.us-west-2.compute.internal",
#                                 "Attachment": {
#                                     "Status": "attached",
#                                     "DeviceIndex": 0,
#                                     "DeleteOnTermination": true,
#                                     "AttachmentId": "eni-attach-060d900e",
#                                     "AttachTime": {
#                                         "hour": 19,
#                                         "__class__": "datetime",
#                                         "month": 12,
#                                         "second": 20,
#                                         "microsecond": 0,
#                                         "year": 2014,
#                                         "day": 12,
#                                         "minute": 35
#                                     }
#                                 },
#                                 "Groups": [
#                                     {
#                                         "GroupName": "launch-wizard-1",
#                                         "GroupId": "sg-80572fe5"
#                                     }
#                                 ],
#                                 "Ipv6Addresses": [],
#                                 "OwnerId": "803363563885",
#                                 "SubnetId": "subnet-29798e70",
#                                 "PrivateIpAddress": "172.31.8.185"
#                             }
#                         ],
#                         "SourceDestCheck": true,
#                         "Placement": {
#                             "Tenancy": "default",
#                             "GroupName": "",
#                             "AvailabilityZone": "us-west-2c"
#                         },
#                         "Hypervisor": "xen",
#                         "BlockDeviceMappings": [],
#                         "Architecture": "x86_64",
#                         "RootDeviceType": "ebs",
#                         "IamInstanceProfile": {
#                             "Id": "AIPAIGHNAOBIDH4HBJ2NI",
#                             "Arn": "arn:aws:iam::803363563885:instance-profile/smithRole"
#                         },
#                         "RootDeviceName": "/dev/sda1",
#                         "VirtualizationType": "hvm",
#                         "Tags": [
#                             {
#                                 "Value": "test-forms",
#                                 "Key": "Name"
#                             }
#                         ],
#                         "AmiLaunchIndex": 0
#                     }
#                 ],
#                 "ReservationId": "r-3aef7235",
#                 "Groups": [],
#                 "OwnerId": "803363563885"
#             },
#             {
#                 "Instances": [
#                     {
#                         "Monitoring": {
#                             "State": "disabled"
#                         },
#                         "StateReason": {
#                             "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
#                             "Code": "Client.UserInitiatedShutdown"
#                         },
#                         "PublicDnsName": "devbox",
#                         "Platform": "windows",
#                         "State": {
#                             "Code": 80,
#                             "Name": "stopped"
#                         },
#                         "EbsOptimized": false,
#                         "LaunchTime": {
#                             "hour": 22,
#                             "__class__": "datetime",
#                             "month": 12,
#                             "second": 35,
#                             "microsecond": 0,
#                             "year": 2014,
#                             "day": 12,
#                             "minute": 58
#                         },
#                         "PrivateIpAddress": "172.31.0.138",
#                         "ProductCodes": [],
#                         "VpcId": "vpc-22de0647",
#                         "StateTransitionReason": "User initiated (2014-12-12 23:00:05 GMT)",
#                         "InstanceId": "i-f7d726f9",
#                         "ImageId": "ami-a13d6891",
#                         "PrivateDnsName": "ip-172-31-0-138.us-west-2.compute.internal",
#                         "KeyName": "smithKeypair",
#                         "SecurityGroups": [
#                             {
#                                 "GroupName": "launch-wizard-1",
#                                 "GroupId": "sg-80572fe5"
#                             }
#                         ],
#                         "ClientToken": "QqAOI1418425115371",
#                         "SubnetId": "subnet-29798e70",
#                         "InstanceType": "t2.micro",
#                         "NetworkInterfaces": [
#                             {
#                                 "Status": "in-use",
#                                 "MacAddress": "0a:0c:87:8a:53:da",
#                                 "SourceDestCheck": true,
#                                 "VpcId": "vpc-22de0647",
#                                 "Description": "Primary network interface",
#                                 "NetworkInterfaceId": "eni-5af3de03",
#                                 "PrivateIpAddresses": [
#                                     {
#                                         "PrivateDnsName": "ip-172-31-0-138.us-west-2.compute.internal",
#                                         "Primary": true,
#                                         "PrivateIpAddress": "172.31.0.138"
#                                     }
#                                 ],
#                                 "PrivateDnsName": "ip-172-31-0-138.us-west-2.compute.internal",
#                                 "Attachment": {
#                                     "Status": "attached",
#                                     "DeviceIndex": 0,
#                                     "DeleteOnTermination": true,
#                                     "AttachmentId": "eni-attach-692db061",
#                                     "AttachTime": {
#                                         "hour": 22,
#                                         "__class__": "datetime",
#                                         "month": 12,
#                                         "second": 35,
#                                         "microsecond": 0,
#                                         "year": 2014,
#                                         "day": 12,
#                                         "minute": 58
#                                     }
#                                 },
#                                 "Groups": [
#                                     {
#                                         "GroupName": "launch-wizard-1",
#                                         "GroupId": "sg-80572fe5"
#                                     }
#                                 ],
#                                 "Ipv6Addresses": [],
#                                 "OwnerId": "803363563885",
#                                 "SubnetId": "subnet-29798e70",
#                                 "PrivateIpAddress": "172.31.0.138"
#                             }
#                         ],
#                         "SourceDestCheck": true,
#                         "Placement": {
#                             "Tenancy": "default",
#                             "GroupName": "",
#                             "AvailabilityZone": "us-west-2c"
#                         },
#                         "Hypervisor": "xen",
#                         "BlockDeviceMappings": [],
#                         "Architecture": "x86_64",
#                         "RootDeviceType": "ebs",
#                         "IamInstanceProfile": {
#                             "Id": "AIPAIGHNAOBIDH4HBJ2NI",
#                             "Arn": "arn:aws:iam::803363563885:instance-profile/smithRole"
#                         },
#                         "RootDeviceName": "/dev/sda1",
#                         "VirtualizationType": "hvm",
#                         "Tags": [
#                             {
#                                 "Value": "devlab-forms",
#                                 "Key": "Name"
#                             }
#                         ],
#                         "AmiLaunchIndex": 0
#                     },
#                     {
#                         "Monitoring": {
#                             "State": "disabled"
#                         },
#                         "StateReason": {
#                             "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
#                             "Code": "Client.UserInitiatedShutdown"
#                         },
#                         "PublicDnsName": "devbox",
#                         "Platform": "windows",
#                         "State": {
#                             "Code": 80,
#                             "Name": "stopped"
#                         },
#                         "EbsOptimized": false,
#                         "LaunchTime": {
#                             "hour": 22,
#                             "__class__": "datetime",
#                             "month": 12,
#                             "second": 35,
#                             "microsecond": 0,
#                             "year": 2014,
#                             "day": 12,
#                             "minute": 58
#                         },
#                         "PrivateIpAddress": "172.31.0.139",
#                         "ProductCodes": [],
#                         "VpcId": "vpc-22de0647",
#                         "StateTransitionReason": "User initiated (2014-12-12 23:00:05 GMT)",
#                         "InstanceId": "i-f4d726fa",
#                         "ImageId": "ami-a13d6891",
#                         "PrivateDnsName": "ip-172-31-0-139.us-west-2.compute.internal",
#                         "KeyName": "smithKeypair",
#                         "SecurityGroups": [
#                             {
#                                 "GroupName": "launch-wizard-1",
#                                 "GroupId": "sg-80572fe5"
#                             }
#                         ],
#                         "ClientToken": "QqAOI1418425115371",
#                         "SubnetId": "subnet-29798e70",
#                         "InstanceType": "t2.micro",
#                         "NetworkInterfaces": [
#                             {
#                                 "Status": "in-use",
#                                 "MacAddress": "0a:74:dc:26:5a:09",
#                                 "SourceDestCheck": true,
#                                 "VpcId": "vpc-22de0647",
#                                 "Description": "Primary network interface",
#                                 "NetworkInterfaceId": "eni-59f3de00",
#                                 "PrivateIpAddresses": [
#                                     {
#                                         "PrivateDnsName": "ip-172-31-0-139.us-west-2.compute.internal",
#                                         "Primary": true,
#                                         "PrivateIpAddress": "172.31.0.139"
#                                     }
#                                 ],
#                                 "PrivateDnsName": "ip-172-31-0-139.us-west-2.compute.internal",
#                                 "Attachment": {
#                                     "Status": "attached",
#                                     "DeviceIndex": 0,
#                                     "DeleteOnTermination": true,
#                                     "AttachmentId": "eni-attach-572db05f",
#                                     "AttachTime": {
#                                         "hour": 22,
#                                         "__class__": "datetime",
#                                         "month": 12,
#                                         "second": 35,
#                                         "microsecond": 0,
#                                         "year": 2014,
#                                         "day": 12,
#                                         "minute": 58
#                                     }
#                                 },
#                                 "Groups": [
#                                     {
#                                         "GroupName": "launch-wizard-1",
#                                         "GroupId": "sg-80572fe5"
#                                     }
#                                 ],
#                                 "Ipv6Addresses": [],
#                                 "OwnerId": "803363563885",
#                                 "SubnetId": "subnet-29798e70",
#                                 "PrivateIpAddress": "172.31.0.139"
#                             }
#                         ],
#                         "SourceDestCheck": true,
#                         "Placement": {
#                             "Tenancy": "default",
#                             "GroupName": "",
#                             "AvailabilityZone": "us-west-2c"
#                         },
#                         "Hypervisor": "xen",
#                         "BlockDeviceMappings": [],
#                         "Architecture": "x86_64",
#                         "RootDeviceType": "ebs",
#                         "IamInstanceProfile": {
#                             "Id": "AIPAIGHNAOBIDH4HBJ2NI",
#                             "Arn": "arn:aws:iam::803363563885:instance-profile/smithRole"
#                         },
#                         "RootDeviceName": "/dev/sda1",
#                         "VirtualizationType": "hvm",
#                         "Tags": [
#                             {
#                                 "Value": "test-account-svc",
#                                 "Key": "Name"
#                             }
#                         ],
#                         "AmiLaunchIndex": 1
#                     },
#                     {
#                         "Monitoring": {
#                             "State": "disabled"
#                         },
#                         "StateReason": {
#                             "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
#                             "Code": "Client.UserInitiatedShutdown"
#                         },
#                         "PublicDnsName": "devbox",
#                         "Platform": "windows",
#                         "State": {
#                             "Code": 80,
#                             "Name": "stopped"
#                         },
#                         "EbsOptimized": false,
#                         "LaunchTime": {
#                             "hour": 22,
#                             "__class__": "datetime",
#                             "month": 12,
#                             "second": 35,
#                             "microsecond": 0,
#                             "year": 2014,
#                             "day": 12,
#                             "minute": 58
#                         },
#                         "PrivateIpAddress": "172.31.0.142",
#                         "ProductCodes": [],
#                         "VpcId": "vpc-22de0647",
#                         "StateTransitionReason": "User initiated (2014-12-12 23:00:05 GMT)",
#                         "InstanceId": "i-f5d726fb",
#                         "ImageId": "ami-a13d6891",
#                         "PrivateDnsName": "ip-172-31-0-142.us-west-2.compute.internal",
#                         "KeyName": "smithKeypair",
#                         "SecurityGroups": [
#                             {
#                                 "GroupName": "launch-wizard-1",
#                                 "GroupId": "sg-80572fe5"
#                             }
#                         ],
#                         "ClientToken": "QqAOI1418425115371",
#                         "SubnetId": "subnet-29798e70",
#                         "InstanceType": "t2.micro",
#                         "NetworkInterfaces": [
#                             {
#                                 "Status": "in-use",
#                                 "MacAddress": "0a:9d:47:77:f4:2c",
#                                 "SourceDestCheck": true,
#                                 "VpcId": "vpc-22de0647",
#                                 "Description": "Primary network interface",
#                                 "NetworkInterfaceId": "eni-58f3de01",
#                                 "PrivateIpAddresses": [
#                                     {
#                                         "PrivateDnsName": "ip-172-31-0-142.us-west-2.compute.internal",
#                                         "Primary": true,
#                                         "PrivateIpAddress": "172.31.0.142"
#                                     }
#                                 ],
#                                 "PrivateDnsName": "ip-172-31-0-142.us-west-2.compute.internal",
#                                 "Attachment": {
#                                     "Status": "attached",
#                                     "DeviceIndex": 0,
#                                     "DeleteOnTermination": true,
#                                     "AttachmentId": "eni-attach-562db05e",
#                                     "AttachTime": {
#                                         "hour": 22,
#                                         "__class__": "datetime",
#                                         "month": 12,
#                                         "second": 35,
#                                         "microsecond": 0,
#                                         "year": 2014,
#                                         "day": 12,
#                                         "minute": 58
#                                     }
#                                 },
#                                 "Groups": [
#                                     {
#                                         "GroupName": "launch-wizard-1",
#                                         "GroupId": "sg-80572fe5"
#                                     }
#                                 ],
#                                 "Ipv6Addresses": [],
#                                 "OwnerId": "803363563885",
#                                 "SubnetId": "subnet-29798e70",
#                                 "PrivateIpAddress": "172.31.0.142"
#                             }
#                         ],
#                         "SourceDestCheck": true,
#                         "Placement": {
#                             "Tenancy": "default",
#                             "GroupName": "",
#                             "AvailabilityZone": "us-west-2c"
#                         },
#                         "Hypervisor": "xen",
#                         "BlockDeviceMappings": [],
#                         "Architecture": "x86_64",
#                         "RootDeviceType": "ebs",
#                         "IamInstanceProfile": {
#                             "Id": "AIPAIGHNAOBIDH4HBJ2NI",
#                             "Arn": "arn:aws:iam::803363563885:instance-profile/smithRole"
#                         },
#                         "RootDeviceName": "/dev/sda1",
#                         "VirtualizationType": "hvm",
#                         "Tags": [
#                             {
#                                 "Value": "devlab-pubsrv",
#                                 "Key": "Name"
#                             }
#                         ],
#                         "AmiLaunchIndex": 2
#                     },
#                     {
#                         "Monitoring": {
#                             "State": "disabled"
#                         },
#                         "StateReason": {
#                             "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
#                             "Code": "Client.UserInitiatedShutdown"
#                         },
#                         "PublicDnsName": "devbox",
#                         "Platform": "windows",
#                         "State": {
#                             "Code": 80,
#                             "Name": "stopped"
#                         },
#                         "EbsOptimized": false,
#                         "LaunchTime": {
#                             "hour": 22,
#                             "__class__": "datetime",
#                             "month": 12,
#                             "second": 35,
#                             "microsecond": 0,
#                             "year": 2014,
#                             "day": 12,
#                             "minute": 58
#                         },
#                         "PrivateIpAddress": "172.31.0.140",
#                         "ProductCodes": [],
#                         "VpcId": "vpc-22de0647",
#                         "StateTransitionReason": "User initiated (2014-12-12 23:00:05 GMT)",
#                         "InstanceId": "i-f2d726fc",
#                         "ImageId": "ami-a13d6891",
#                         "PrivateDnsName": "ip-172-31-0-140.us-west-2.compute.internal",
#                         "KeyName": "smithKeypair",
#                         "SecurityGroups": [
#                             {
#                                 "GroupName": "launch-wizard-1",
#                                 "GroupId": "sg-80572fe5"
#                             }
#                         ],
#                         "ClientToken": "QqAOI1418425115371",
#                         "SubnetId": "subnet-29798e70",
#                         "InstanceType": "t2.micro",
#                         "NetworkInterfaces": [
#                             {
#                                 "Status": "in-use",
#                                 "MacAddress": "0a:ba:50:8a:99:05",
#                                 "SourceDestCheck": true,
#                                 "VpcId": "vpc-22de0647",
#                                 "Description": "Primary network interface",
#                                 "NetworkInterfaceId": "eni-a6f0ddff",
#                                 "PrivateIpAddresses": [
#                                     {
#                                         "PrivateDnsName": "ip-172-31-0-140.us-west-2.compute.internal",
#                                         "Primary": true,
#                                         "PrivateIpAddress": "172.31.0.140"
#                                     }
#                                 ],
#                                 "PrivateDnsName": "ip-172-31-0-140.us-west-2.compute.internal",
#                                 "Attachment": {
#                                     "Status": "attached",
#                                     "DeviceIndex": 0,
#                                     "DeleteOnTermination": true,
#                                     "AttachmentId": "eni-attach-552db05d",
#                                     "AttachTime": {
#                                         "hour": 22,
#                                         "__class__": "datetime",
#                                         "month": 12,
#                                         "second": 35,
#                                         "microsecond": 0,
#                                         "year": 2014,
#                                         "day": 12,
#                                         "minute": 58
#                                     }
#                                 },
#                                 "Groups": [
#                                     {
#                                         "GroupName": "launch-wizard-1",
#                                         "GroupId": "sg-80572fe5"
#                                     }
#                                 ],
#                                 "Ipv6Addresses": [],
#                                 "OwnerId": "803363563885",
#                                 "SubnetId": "subnet-29798e70",
#                                 "PrivateIpAddress": "172.31.0.140"
#                             }
#                         ],
#                         "SourceDestCheck": true,
#                         "Placement": {
#                             "Tenancy": "default",
#                             "GroupName": "",
#                             "AvailabilityZone": "us-west-2c"
#                         },
#                         "Hypervisor": "xen",
#                         "BlockDeviceMappings": [],
#                         "Architecture": "x86_64",
#                         "RootDeviceType": "ebs",
#                         "IamInstanceProfile": {
#                             "Id": "AIPAIGHNAOBIDH4HBJ2NI",
#                             "Arn": "arn:aws:iam::803363563885:instance-profile/smithRole"
#                         },
#                         "RootDeviceName": "/dev/sda1",
#                         "VirtualizationType": "hvm",
#                         "Tags": [
#                             {
#                                 "Value": "devlab-game-svc",
#                                 "Key": "Name"
#                             }
#                         ],
#                         "AmiLaunchIndex": 3
#                     },
#                     {
#                         "Monitoring": {
#                             "State": "disabled"
#                         },
#                         "StateReason": {
#                             "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
#                             "Code": "Client.UserInitiatedShutdown"
#                         },
#                         "PublicDnsName": "devbox",
#                         "Platform": "windows",
#                         "State": {
#                             "Code": 80,
#                             "Name": "stopped"
#                         },
#                         "EbsOptimized": false,
#                         "LaunchTime": {
#                             "hour": 22,
#                             "__class__": "datetime",
#                             "month": 12,
#                             "second": 35,
#                             "microsecond": 0,
#                             "year": 2014,
#                             "day": 12,
#                             "minute": 58
#                         },
#                         "PrivateIpAddress": "172.31.0.141",
#                         "ProductCodes": [],
#                         "VpcId": "vpc-22de0647",
#                         "StateTransitionReason": "User initiated (2014-12-12 23:00:05 GMT)",
#                         "InstanceId": "i-f3d726fd",
#                         "ImageId": "ami-a13d6891",
#                         "PrivateDnsName": "ip-172-31-0-141.us-west-2.compute.internal",
#                         "KeyName": "smithKeypair",
#                         "SecurityGroups": [
#                             {
#                                 "GroupName": "launch-wizard-1",
#                                 "GroupId": "sg-80572fe5"
#                             }
#                         ],
#                         "ClientToken": "QqAOI1418425115371",
#                         "SubnetId": "subnet-29798e70",
#                         "InstanceType": "t2.micro",
#                         "NetworkInterfaces": [
#                             {
#                                 "Status": "in-use",
#                                 "MacAddress": "0a:5f:35:84:ad:b8",
#                                 "SourceDestCheck": true,
#                                 "VpcId": "vpc-22de0647",
#                                 "Description": "Primary network interface",
#                                 "NetworkInterfaceId": "eni-5bf3de02",
#                                 "PrivateIpAddresses": [
#                                     {
#                                         "PrivateDnsName": "ip-172-31-0-141.us-west-2.compute.internal",
#                                         "Primary": true,
#                                         "PrivateIpAddress": "172.31.0.141"
#                                     }
#                                 ],
#                                 "PrivateDnsName": "ip-172-31-0-141.us-west-2.compute.internal",
#                                 "Attachment": {
#                                     "Status": "attached",
#                                     "DeviceIndex": 0,
#                                     "DeleteOnTermination": true,
#                                     "AttachmentId": "eni-attach-782db070",
#                                     "AttachTime": {
#                                         "hour": 22,
#                                         "__class__": "datetime",
#                                         "month": 12,
#                                         "second": 35,
#                                         "microsecond": 0,
#                                         "year": 2014,
#                                         "day": 12,
#                                         "minute": 58
#                                     }
#                                 },
#                                 "Groups": [
#                                     {
#                                         "GroupName": "launch-wizard-1",
#                                         "GroupId": "sg-80572fe5"
#                                     }
#                                 ],
#                                 "Ipv6Addresses": [],
#                                 "OwnerId": "803363563885",
#                                 "SubnetId": "subnet-29798e70",
#                                 "PrivateIpAddress": "172.31.0.141"
#                             }
#                         ],
#                         "SourceDestCheck": true,
#                         "Placement": {
#                             "Tenancy": "default",
#                             "GroupName": "",
#                             "AvailabilityZone": "us-west-2c"
#                         },
#                         "Hypervisor": "xen",
#                         "BlockDeviceMappings": [],
#                         "Architecture": "x86_64",
#                         "RootDeviceType": "ebs",
#                         "IamInstanceProfile": {
#                             "Id": "AIPAIGHNAOBIDH4HBJ2NI",
#                             "Arn": "arn:aws:iam::803363563885:instance-profile/smithRole"
#                         },
#                         "RootDeviceName": "/dev/sda1",
#                         "VirtualizationType": "hvm",
#                         "Tags": [
#                             {
#                                 "Value": "test-game-svc",
#                                 "Key": "Name"
#                             }
#                         ],
#                         "AmiLaunchIndex": 4
#                     }
#                 ],
#                 "ReservationId": "r-108a171f",
#                 "Groups": [],
#                 "OwnerId": "803363563885"
#             },
#             {
#                 "Instances": [
#                     {
#                         "Monitoring": {
#                             "State": "disabled"
#                         },
#                         "PublicDnsName": "devbox",
#                         "State": {
#                             "Code": 16,
#                             "Name": "running"
#                         },
#                         "EbsOptimized": false,
#                         "LaunchTime": {
#                             "hour": 15,
#                             "__class__": "datetime",
#                             "month": 7,
#                             "second": 39,
#                             "microsecond": 0,
#                             "year": 2017,
#                             "day": 22,
#                             "minute": 29
#                         },
#                         "PublicIpAddress": "35.167.85.101",
#                         "PrivateIpAddress": "172.31.2.38",
#                         "ProductCodes": [],
#                         "VpcId": "vpc-22de0647",
#                         "StateTransitionReason": "",
#                         "InstanceId": "i-0f500447384e95942",
#                         "EnaSupport": true,
#                         "ImageId": "ami-835b4efa",
#                         "PrivateDnsName": "ip-172-31-2-38.us-west-2.compute.internal",
#                         "KeyName": "smithKeypair",
#                         "SecurityGroups": [
#                             {
#                                 "GroupName": "launch-wizard-2",
#                                 "GroupId": "sg-f3f24d89"
#                             }
#                         ],
#                         "ClientToken": "PlfxW1500737379183",
#                         "SubnetId": "subnet-29798e70",
#                         "InstanceType": "t2.micro",
#                         "NetworkInterfaces": [
#                             {
#                                 "Status": "in-use",
#                                 "MacAddress": "0a:6c:2a:a0:d0:9e",
#                                 "SourceDestCheck": true,
#                                 "VpcId": "vpc-22de0647",
#                                 "Description": "",
#                                 "NetworkInterfaceId": "eni-79469a79",
#                                 "PrivateIpAddresses": [
#                                     {
#                                         "PrivateDnsName": "ip-172-31-2-38.us-west-2.compute.internal",
#                                         "PrivateIpAddress": "172.31.2.38",
#                                         "Primary": true,
#                                         "Association": {
#                                             "PublicIp": "35.167.85.101",
#                                             "PublicDnsName": "devbox",
#                                             "IpOwnerId": "amazon"
#                                         }
#                                     }
#                                 ],
#                                 "PrivateDnsName": "ip-172-31-2-38.us-west-2.compute.internal",
#                                 "Attachment": {
#                                     "Status": "attached",
#                                     "DeviceIndex": 0,
#                                     "DeleteOnTermination": true,
#                                     "AttachmentId": "eni-attach-1fa8f2fd",
#                                     "AttachTime": {
#                                         "hour": 15,
#                                         "__class__": "datetime",
#                                         "month": 7,
#                                         "second": 39,
#                                         "microsecond": 0,
#                                         "year": 2017,
#                                         "day": 22,
#                                         "minute": 29
#                                     }
#                                 },
#                                 "Groups": [
#                                     {
#                                         "GroupName": "launch-wizard-2",
#                                         "GroupId": "sg-f3f24d89"
#                                     }
#                                 ],
#                                 "Ipv6Addresses": [],
#                                 "OwnerId": "803363563885",
#                                 "PrivateIpAddress": "172.31.2.38",
#                                 "SubnetId": "subnet-29798e70",
#                                 "Association": {
#                                     "PublicIp": "35.167.85.101",
#                                     "PublicDnsName": "devbox",
#                                     "IpOwnerId": "amazon"
#                                 }
#                             }
#                         ],
#                         "SourceDestCheck": true,
#                         "Placement": {
#                             "Tenancy": "default",
#                             "GroupName": "",
#                             "AvailabilityZone": "us-west-2c"
#                         },
#                         "Hypervisor": "xen",
#                         "BlockDeviceMappings": [
#                             {
#                                 "DeviceName": "/dev/sda1",
#                                 "Ebs": {
#                                     "Status": "attached",
#                                     "DeleteOnTermination": true,
#                                     "VolumeId": "vol-0e25c4d7082d237d8",
#                                     "AttachTime": {
#                                         "hour": 15,
#                                         "__class__": "datetime",
#                                         "month": 7,
#                                         "second": 40,
#                                         "microsecond": 0,
#                                         "year": 2017,
#                                         "day": 22,
#                                         "minute": 29
#                                     }
#                                 }
#                             }
#                         ],
#                         "Architecture": "x86_64",
#                         "RootDeviceType": "ebs",
#                         "RootDeviceName": "/dev/sda1",
#                         "VirtualizationType": "hvm",
#                         "Tags": [
#                             {
#                                 "Value": "test-pubsrv",
#                                 "Key": "Name"
#                             }
#                         ],
#                         "AmiLaunchIndex": 0
#                     }
#                 ],
#                 "ReservationId": "r-0b5cce1da63c818bd",
#                 "Groups": [],
#                 "OwnerId": "803363563885"
#             },
#             {
#                 "Instances": [
#                     {
#                         "Monitoring": {
#                             "State": "disabled"
#                         },
#                         "PublicDnsName": "devbox",
#                         "State": {
#                             "Code": 16,
#                             "Name": "running"
#                         },
#                         "EbsOptimized": false,
#                         "LaunchTime": {
#                             "hour": 15,
#                             "__class__": "datetime",
#                             "month": 7,
#                             "second": 39,
#                             "microsecond": 0,
#                             "year": 2017,
#                             "day": 22,
#                             "minute": 29
#                         },
#                         "PublicIpAddress": "35.167.85.102",
#                         "PrivateIpAddress": "172.31.2.39",
#                         "ProductCodes": [],
#                         "VpcId": "vpc-22de0647",
#                         "StateTransitionReason": "",
#                         "InstanceId": "i-0f500447384e95943",
#                         "EnaSupport": true,
#                         "ImageId": "ami-835b4efa",
#                         "PrivateDnsName": "ip-172-31-2-39.us-west-2.compute.internal",
#                         "KeyName": "smithKeypair",
#                         "SecurityGroups": [
#                             {
#                                 "GroupName": "launch-wizard-2",
#                                 "GroupId": "sg-f3f24d89"
#                             }
#                         ],
#                         "ClientToken": "PlfxW1500737379183",
#                         "SubnetId": "subnet-29798e70",
#                         "InstanceType": "t2.micro",
#                         "NetworkInterfaces": [
#                             {
#                                 "Status": "in-use",
#                                 "MacAddress": "0a:6c:2a:a0:d0:9d",
#                                 "SourceDestCheck": true,
#                                 "VpcId": "vpc-22de0648",
#                                 "Description": "",
#                                 "NetworkInterfaceId": "eni-79469a80",
#                                 "PrivateIpAddresses": [
#                                     {
#                                         "PrivateDnsName": "ip-172-31-2-39.us-west-2.compute.internal",
#                                         "PrivateIpAddress": "172.31.2.39",
#                                         "Primary": true,
#                                         "Association": {
#                                             "PublicIp": "35.167.85.102",
#                                             "PublicDnsName": "devbox",
#                                             "IpOwnerId": "amazon"
#                                         }
#                                     }
#                                 ],
#                                 "PrivateDnsName": "ip-172-31-2-39.us-west-2.compute.internal",
#                                 "Attachment": {
#                                     "Status": "attached",
#                                     "DeviceIndex": 0,
#                                     "DeleteOnTermination": true,
#                                     "AttachmentId": "eni-attach-1fa8f2fd",
#                                     "AttachTime": {
#                                         "hour": 15,
#                                         "__class__": "datetime",
#                                         "month": 7,
#                                         "second": 39,
#                                         "microsecond": 0,
#                                         "year": 2017,
#                                         "day": 22,
#                                         "minute": 29
#                                     }
#                                 },
#                                 "Groups": [
#                                     {
#                                         "GroupName": "launch-wizard-2",
#                                         "GroupId": "sg-f3f24d90"
#                                     }
#                                 ],
#                                 "Ipv6Addresses": [],
#                                 "OwnerId": "803363563885",
#                                 "PrivateIpAddress": "172.31.2.39",
#                                 "SubnetId": "subnet-29798e71",
#                                 "Association": {
#                                     "PublicIp": "35.167.85.102",
#                                     "PublicDnsName": "devbox",
#                                     "IpOwnerId": "amazon"
#                                 }
#                             }
#                         ],
#                         "SourceDestCheck": true,
#                         "Placement": {
#                             "Tenancy": "default",
#                             "GroupName": "",
#                             "AvailabilityZone": "us-west-2c"
#                         },
#                         "Hypervisor": "xen",
#                         "BlockDeviceMappings": [
#                             {
#                                 "DeviceName": "/dev/sda1",
#                                 "Ebs": {
#                                     "Status": "attached",
#                                     "DeleteOnTermination": true,
#                                     "VolumeId": "vol-0e25c4d7082d237d9",
#                                     "AttachTime": {
#                                         "hour": 15,
#                                         "__class__": "datetime",
#                                         "month": 7,
#                                         "second": 40,
#                                         "microsecond": 0,
#                                         "year": 2017,
#                                         "day": 22,
#                                         "minute": 29
#                                     }
#                                 }
#                             }
#                         ],
#                         "Architecture": "x86_64",
#                         "RootDeviceType": "ebs",
#                         "RootDeviceName": "/dev/sda1",
#                         "VirtualizationType": "hvm",
#                         "Tags": [
#                             {
#                                 "Value": "test-pubsrv",
#                                 "Key": "Name"
#                             }
#                         ],
#                         "AmiLaunchIndex": 0
#                     }
#                 ],
#                 "ReservationId": "r-0b5cce1da63c818be",
#                 "Groups": [],
#                 "OwnerId": "803363563885"
#             }
#         ],
#         "ResponseMetadata": {
#             "RetryAttempts": 0,
#             "HTTPStatusCode": 200,
#             "RequestId": "c18b3283-e500-423e-b0aa-b2d8feef2d96",
#             "HTTPHeaders": {
#                 "transfer-encoding": "chunked",
#                 "vary": "Accept-Encoding",
#                 "server": "AmazonEC2",
#                 "content-type": "text/xml;charset=UTF-8",
#                 "date": "Sat, 22 Jul 2017 15:38:31 GMT"
#             }
#         }
#     }
# }
#
# """
#
#
# @mock.patch("__builtin__.open", mock.mock_open(read_data=DATA))
# def test_aws_instances():
#
#     aws_obj = AwsInventory('access_key_id', 'secret_access_key', 'session_token', 'region', 'cache_dir')
#     instances = aws_obj.instances()
#     print instances
#     expected_instances = [Instance(name=u'ip-172-16-223-200', address=u'172.16.223.200'),
#                           Instance(name=u'i-04267e627f88362ed-DEV-self-formsvc', address=u'172.16.221.211'),
#                           Instance(name=u'i-0f9a3f0d9399a6c17-PROD-prfsvclmt', address=u'172.16.225.232')]
#     assert set(instances) == set(expected_instances)
