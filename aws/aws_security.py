import boto3

# Function to retrieve security groups with internet access in a specific region
def security_groups_with_internet_access(region):
    # Initialize EC2 client for the specified region
    client = boto3.client("ec2", region_name=region)
    
    # Describe security groups with IP permission CIDR as "0.0.0.0/0" (internet access)
    response = client.describe_security_groups(Filters=[
      {
        "Name":"ip-permission.cidr",
        "Values": ["0.0.0.0/0"]
      }
    ])

    # Extract relevant information for each security group
    security_groups = []
    for item in response["SecurityGroups"]:
        security_groups.append({
            "Region": region,
            "GroupId": item['GroupId'],
            "GroupName": item["GroupName"],
            "VpcId": item["VpcId"]
        })
      
    return security_groups
  
# Function to retrieve RDS instances that are publicly accessible in a specific region
def rds_instance_publicly_accessible(region):
    # Initialize RDS client for the specified region
    client = boto3.client("rds", region_name=region)
    
    # Describe RDS instances
    response = client.describe_db_instances()
    db_instances = []
    
    # Extract RDS instances that are publicly accessible
    for instance in response["DBInstances"]:
        if instance["PubliclyAccessible"] == True:
            db_instances.append({
                "Region": region,
                "DBInstanceIdentifier": instance["DBInstanceIdentifier"],
                "PubliclyAccessible": str(instance["PubliclyAccessible"])
            })
      
    return db_instances
