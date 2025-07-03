import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from flask import Flask
from django.conf import settings
from fastapi import FastAPI
from sqlalchemy import create_engine
import psycopg2
import redis
from celery import Celery
from pydantic import BaseModel
import click
from rich.console import Console
import typer
import httpx
import aiohttp
import pytest
import asyncio
from bs4 import BeautifulSoup
import lxml
import openpyxl
from PIL import Image
import boto3
from google.cloud import storage
from azure.storage.blob import BlobServiceClient
import paramiko
from cryptography.fernet import Fernet
import jwt
from passlib.hash import bcrypt
import bcrypt as bcrypt_lib

__version__ = "0.1.0"

def get_version():
    return __version__