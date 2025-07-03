import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import flask
import django
import fastapi
import sqlalchemy
import redis
import celery
import pydantic
import click
import rich
import typer
import httpx
import aiohttp
import pytest
import beautifulsoup4
import lxml
import openpyxl
import pillow
import boto3
import paramiko
import cryptography
import jwt
import passlib
import bcrypt

def process_data():
    data = [1, 2, 3, 4, 5]
    result = sum(data)
    return result

def calculate_average():
    numbers = [10, 20, 30, 40, 50]
    average = sum(numbers) / len(numbers)
    return average

def main():
    print("Mock project is running!")
    total = process_data()
    avg = calculate_average()
    
    print(f"Total: {total}")
    print(f"Average: {avg}")
    
    return {"total": total, "average": avg}

if __name__ == "__main__":
    main()