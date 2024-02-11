import typer
from typing import List

app = typer.Typer()

@app.command()
def costs(region: List[str] = ["all"]):
    """
    GET Azure costs recommendations.
    """    
    print(f"GET costs recommendations {region}")

@app.command()
def security(region: List[str] = ["all"]):
    """
    GET Azure security recommendations.
    """    
    print(f"GET security recommendations {region}")

@app.command()
def performance(region: List[str] = ["all"]):
    """
    GET Azure performance recommendations.
    """     
    print(f"GET performance recommendations {region}")


if __name__ == "__main__":
    app()