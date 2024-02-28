# Import necessary libraries
import typer
from typing import List
from rich.console import Console

# Import AWS-related modules
from aws import aws_costs
from aws import aws_security
from aws import utils

# Initialize Rich Console for better terminal output formatting
console = Console()

# Create a Typer application instance
app = typer.Typer()

# Define a command to fetch AWS cost recommendations


@app.command()
def costs(region: List[str] = ["all"],):
    """
    GET costs recommendations.
    """

    # Fetch AWS regions if "all" is provided as an argument
    regions = region
    if len(regions) == 1 and regions[0] == 'all':
        with console.status("Getting AWS Regions", spinner="aesthetic"):
            regions = utils.get_aws_regions_of_account()

    # Initialize lists to store information about AWS resources
    account_detached_ebs_volumes = []
    account_gp2_ebs_volumes = []
    account_unused_elastic_ips = []

    # Iterate over each region to fetch relevant cost information
    for region in regions:
        with console.status(f"Getting unused EBS volumes on region {region}...", spinner="aesthetic"):
            region_detached_ebs_volumes = aws_costs.get_detached_ebs_volumes(
                region)
            if region_detached_ebs_volumes:
                account_detached_ebs_volumes.extend(
                    region_detached_ebs_volumes)

        with console.status(f"Getting GP2 volumes on region {region}...", spinner="aesthetic"):
            region_gp2_volumes = aws_costs.get_gp2_ebs_volumes(region)
            if region_gp2_volumes:
                account_gp2_ebs_volumes.extend(region_gp2_volumes)

        with console.status(f"Getting unused Elastic IPs on region {region}...", spinner="aesthetic"):
            region_unused_elastic_ips = aws_costs.get_unused_elastic_ips(
                region)
            if region_unused_elastic_ips:
                account_unused_elastic_ips.extend(region_unused_elastic_ips)

    # Display recommendations for each type of AWS resource if applicable
    if account_detached_ebs_volumes:
        title_detached_volumes = "Detached EBS volumes"
        recommendation_detached_volumes = "Delete unnecessary volumes, but be cautious to do so carefully to avoid the loss of important data."
        utils.display_table(account_detached_ebs_volumes,
                            title_detached_volumes, recommendation_detached_volumes)

    if account_gp2_ebs_volumes:
        title_gp2_volumes = "GP2 volumes"
        recommendation_gp2_volumes = "Evaluate the possibility of migrating volumes to gp3"
        utils.display_table(account_gp2_ebs_volumes,
                            title_gp2_volumes, recommendation_gp2_volumes)

    if account_unused_elastic_ips:
        title_unused_elastic_ips = "Unused Elastic IP addresses"
        recommendation_unused_elastic_ips = "Check the possibility of releasing IP addresses"
        utils.display_table(account_unused_elastic_ips,
                            title_unused_elastic_ips, recommendation_unused_elastic_ips)

# Define a command to fetch security recommendations


@app.command()
def security(region: List[str] = ["all"]):
    """
    GET security recommendations.
    """

    regions = region
    if len(regions) == 1 and regions[0] == 'all':
        with console.status("Getting AWS Regions", spinner="aesthetic"):
            regions = utils.get_aws_regions_of_account()

    account_security_group_with_internet_access = []
    account_rds_instance_publicly_accessible = []

    for region in regions:
        with console.status(f"Getting security groups containing rules allowing inbound traffic from the internet (0.0.0.0/0) on region {region}...", spinner="aesthetic"):
            security_group_with_internet_access = aws_security.security_groups_with_internet_access(
                region)
            if security_group_with_internet_access:
                account_security_group_with_internet_access.extend(
                    security_group_with_internet_access)

        with console.status(f"Getting RDS instances publicly accessible on region {region}...", spinner="aesthetic"):
            region_rds_instance_publicly_accessible = aws_security.rds_instance_publicly_accessible(
                region)
            if region_rds_instance_publicly_accessible:
                account_rds_instance_publicly_accessible.extend(
                    region_rds_instance_publicly_accessible)

    # Display security recommendations if applicable
    if account_security_group_with_internet_access:
        title_security_group_with_internet_access = "Security groups that have inbound rules allowing all traffic originating from the internet (0.0.0.0/0)."
        recommendation_security_group_with_internet_access = "Review and limit inbound rules to specific IP ranges or sources whenever possible to reduce the attack surface"
        utils.display_table(account_security_group_with_internet_access,
                            title_security_group_with_internet_access, recommendation_security_group_with_internet_access)

    if account_rds_instance_publicly_accessible:
        title_rds_instance_publicly_accessible = "RDS Instances Publicly accessible"
        recommendation_rds_instance_publicly_accessible = "Disabling public IP assignment for RDS instances and implementing secure connectivity options such as VPC endpoints and strict security group rules, you can reduce the attack surface and strengthen the overall security of your AWS environment."
        utils.display_table(account_rds_instance_publicly_accessible,
                            title_rds_instance_publicly_accessible, recommendation_rds_instance_publicly_accessible)


# Entry point of the script
if __name__ == "__main__":
    app()
