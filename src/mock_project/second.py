import requests
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import django
import fastapi
import sqlalchemy

def process_data_second():
    data = [1, 2, 3, 4, 5]
    result = sum(data)
    return result

def calculate_average_second():
    numbers = [10, 20, 30, 40, 50]
    average = sum(numbers) / len(numbers)
    return average