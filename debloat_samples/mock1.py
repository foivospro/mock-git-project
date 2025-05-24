#!/usr/bin/env python3
"""Mock Python file with various imports."""

import os
import sys as system
import numpy as np
import requests
import fake_module
from collections import defaultdict, namedtuple
from math import *
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
from typing import List, Dict, Tuple

try:
    import optional_module
except ImportError:
    optional_module = None

import importlib

mymod = importlib.import_module('json')

from .local_module import local_function, LocalClass
from ..parent_module import ParentClass

def example():
    cwd = os.getcwd()
    path = urlparse('https://example.com')
    arr = np.array([1, 2, 3])
    response = requests.get('https://api.example.com/data')
    return cwd, path, arr, response.status_code
