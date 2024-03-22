import boto3

# Function to retrieve detached EBS volumes in a specific region


def get_detached_ebs_volumes(region):
    # Initialize EC2 client for the specified region
    client = boto3.client('ec2', region_name=region)

    # Describe volumes with status "available" (detached)
    response = client.describe_volumes(
        Filters=[
            {
                "Name": 'status',
                "Values": ["available"]
            }
        ]
    )

    # Extract relevant information for each volume
    volumes = []
    for item in response.get('Volumes', []):
        volumes.append({
            'Region': region,
            'VolumeId': item['VolumeId'],
            'State': item['State'],
            'AvailabilityZone': item['AvailabilityZone'],
            'VolumeType': item['VolumeType'],
            'Size': str(item['Size'])
        })

    return volumes

# Function to retrieve GP2 EBS volumes in a specific region


def get_gp2_ebs_volumes(region):
    # Initialize EC2 client for the specified region
    client = boto3.client('ec2', region_name=region)

    # Describe volumes with type "gp2"
    response = client.describe_volumes(
        Filters=[
            {
                "Name": 'volume-type',
                "Values": ["gp2"]
            }
        ]
    )

    # Extract relevant information for each volume
    ebs_volumes = []
    for volume in response.get('Volumes', []):
        ebs_volumes.append({
            'Region': region,
            'VolumeId': volume['VolumeId'],
            'VolumeType': volume['VolumeType']
        })

    return ebs_volumes

# Function to retrieve unused Elastic IPs in a specific region


def get_unused_elastic_ips(region):
    # Initialize EC2 client for the specified region
    client = boto3.client('ec2', region_name=region)

    # Describe Elastic IPs
    response = client.describe_addresses()

    # Extract unused Elastic IPs
    not_used_ips = []
    for address in response.get('Addresses', []):
        # Check if Elastic IP is not associated with any network interface
        if "NetworkInterfaceId" not in address and address is not None:
            not_used_ips.append({
                "Region": region,
                "Address": address['PublicIp'],
                "AllocationId": address['AllocationId']
            })

    return not_used_ips


def get_volumes_attached_on_stopped_instances(region):

    try:
        # Initialize EC2 client for the specified region
        client = boto3.client('ec2', region_name=region)

        # Describe Instances
        response = client.describe_instances(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': ['stopped']
                }
            ]
        )
        volumes = []
        for reservation in response.get("Reservations"):
            for instance in reservation["Instances"]:
                for device in instance["BlockDeviceMappings"]:
                    volumes.append({"region": region, "instance": instance["InstanceId"], "device": device["DeviceName"],
                                    "volume": device["Ebs"]["VolumeId"]})
        return volumes
    except Exception as e:
        print("Ocorreu um erro")
        print(e)
