import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import click
import rich
import typer
import httpx

__version__ = "0.1.0"

def get_version():
    return __version__