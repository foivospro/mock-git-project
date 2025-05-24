#!/usr/bin/env python3
"""Second mock Python file with diverse imports."""

import importlib
import platform
import datetime
import time
import yaml
import json
import plistlib
import nonexistent_package
import thirdparty1, thirdparty2 as tp2
from random import choice, randint
from math import sqrt as square_root
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer
import uvicorn
import pathspec
from typing import Optional

spec = importlib.util.find_spec('ssl')
if spec is not None:
    import ssl

def main():
    print(platform.system())
    data = yaml.safe_load('x: 1')
    val = choice([1, 2, 3])
    return square_root(val)
