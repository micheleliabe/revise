#!/usr/bin/python3

# Import Typer for command-line interface creation
import typer

# Import Console from Rich for better terminal output formatting
from rich.console import Console

# Import pyfiglet for ASCII banner creation
import pyfiglet

# Import sub-modules for AWS, Azure, and GCP functionalities
import aws.aws as aws
import azure.azure as azure
import gcp.gcp as gcp

# Initialize Rich Console for better terminal output formatting
console = Console()

# Display ASCII banner using pyfiglet
ascii_banner = pyfiglet.figlet_format("Revise.cli")
console.print(f"[purple]{ascii_banner}")
console.print("By - Michel Dias")
console.print()

# Create a Typer application instance
app = typer.Typer()

# Add sub-commands for AWS, Azure, and GCP functionalities
app.add_typer(aws.app, name="aws")
# app.add_typer(azure.app, name="azure")
# app.add_typer(gcp.app, name="gcp")    

# Entry point of the script
if __name__ == "__main__":
    app()
