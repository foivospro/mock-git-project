import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import click
import rich
import typer
import httpx
import seaborn as sns
import flask
import django
import fastapi
import os

def fetch_data():
    response = requests.get("https://httpbin.org/json")
    return response.json() if response.status_code == 200 else {}

def process_data():
    data = [1, 2, 3, 4, 5]
    arr = np.array(data)
    df = pd.DataFrame({"values": data})

    result = {
        "sum": arr.sum(),
        "mean": arr.mean(),
        "dataframe_size": len(df)
    }

    return result

def calculate_average():
    numbers = [10, 20, 30, 40, 50]
    average = sum(numbers) / len(numbers)
    return average

@click.command()
@click.option('--verbose', is_flag=True, help='Verbose output')
def main(verbose):
    if verbose:
        print("Mock project is running in verbose mode!")
    else:
        print("Mock project is running!")

    api_data = fetch_data()
    processed = process_data()
    avg = calculate_average()

    if verbose:
        console = rich.console.Console()
        console.print(f"API Data: {api_data}", style="green")
        console.print(f"Processed: {processed}", style="blue")
        console.print(f"Average: {avg}", style="yellow")
    else:
        print(f"Processed: {processed}")
        print(f"Average: {avg}")

    return {"api": api_data, "processed": processed, "average": avg}

if __name__ == "__main__":
    main()