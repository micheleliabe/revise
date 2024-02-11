import boto3
from rich.console import Console
from rich.table import Table, box

# Initialize Rich Console for better terminal output formatting
console = Console()

# Function to get AWS regions enabled for the AWS account
def get_aws_regions_of_account():
    # Initialize Boto3 client for the account
    client = boto3.client("account")
    
    # List regions enabled for the account
    response = client.list_regions(
        RegionOptStatusContains=['ENABLED', 'ENABLED_BY_DEFAULT']
    )

    # Extract region names from the response
    regions = [region['RegionName'] for region in response.get('Regions', [])]
    return regions

# Function to display data in a tabular format with a title and optional recommendation
def display_table(data, title, recommendation=None):
    # Create a Rich Table with specified title and formatting
    table = Table(
        title=f"[bold purple]{title}", show_header=True, show_lines=True, box=box.ROUNDED,
        title_justify='left'
    )
    
    # Extract column names from the data
    columns = data[0].keys()
    
    # Add columns to the table
    for column in columns:
        table.add_column(column)
    
    # Add rows to the table
    for region in data:
        row = []
        # Populate each row with values from the region dictionary
        for key, value in region.items():
            row.append(value)
        table.add_row(*row)
        
    # Print the table using Rich Console
    console.print(table)
    
    # Print recommendation if provided
    if recommendation:
        console.print(f"\n [purple]Recommendation: \n  [white]- {recommendation}")
    
    # Add a newline after printing the table
    console.print()
