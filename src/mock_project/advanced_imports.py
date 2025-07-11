import sys
import os
import importlib
import importlib.util
from pathlib import Path
from typing import Any, Dict, List, Optional, Union, Callable
from collections import defaultdict, namedtuple, OrderedDict
from functools import partial, reduce, wraps
from itertools import chain, combinations, permutations
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import yaml
import configparser
from dataclasses import dataclass, field
from enum import Enum, auto
import asyncio
import logging
from contextlib import contextmanager, asynccontextmanager
import pickle
import sqlite3
from urllib.parse import urlparse
import re
import hashlib
import base64
import datetime
import time
import random
import uuid
from decimal import Decimal
import math
import statistics

from .utils.helpers import helper_function, UtilityClass
from .utils import helpers as util_helpers

try:
    import requests
except ImportError:
    requests = None

try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

ConfigTuple = namedtuple('ConfigTuple', ['host', 'port', 'debug'])

class ProcessingMode(Enum):
    SEQUENTIAL = auto()
    PARALLEL = auto()
    ASYNC = auto()

@dataclass
class DataProcessor:
    mode: ProcessingMode = ProcessingMode.SEQUENTIAL
    max_workers: int = 4
    timeout: float = 30.0
    config: Dict[str, Any] = field(default_factory=dict)

class DynamicImportManager:
    def __init__(self):
        self.loaded_modules = {}
        self.config_parsers = {
            '.json': self._load_json,
            '.yaml': self._load_yaml,
            '.yml': self._load_yaml,
            '.ini': self._load_ini,
            '.toml': self._load_toml if 'toml' in sys.modules else None
        }
    
    def _load_json(self, path: str) -> Dict[str, Any]:
        with open(path, 'r') as f:
            return json.load(f)
    
    def _load_yaml(self, path: str) -> Dict[str, Any]:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def _load_ini(self, path: str) -> Dict[str, Any]:
        parser = configparser.ConfigParser()
        parser.read(path)
        return {section: dict(parser.items(section)) for section in parser.sections()}
    
    def _load_toml(self, path: str) -> Dict[str, Any]:
        import toml
        with open(path, 'r') as f:
            return toml.load(f)
    
    def dynamic_import(self, module_name: str, package: Optional[str] = None) -> Any:
        try:
            if package:
                full_name = f"{package}.{module_name}"
            else:
                full_name = module_name
            
            if full_name in self.loaded_modules:
                return self.loaded_modules[full_name]
            
            spec = importlib.util.find_spec(full_name)
            if spec is None:
                raise ImportError(f"Module {full_name} not found")
            
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self.loaded_modules[full_name] = module
            return module
        except Exception as e:
            logging.error(f"Failed to dynamically import {full_name}: {e}")
            return None
    
    def load_config_file(self, path: str) -> Optional[Dict[str, Any]]:
        file_path = Path(path)
        if not file_path.exists():
            return None
        
        extension = file_path.suffix.lower()
        loader = self.config_parsers.get(extension)
        
        if loader is None:
            logging.warning(f"No parser available for {extension} files")
            return None
        
        try:
            return loader(str(file_path))
        except Exception as e:
            logging.error(f"Failed to load config from {path}: {e}")
            return None

def complex_decorator(func_or_class=None, *, 
                     cache_size: int = 128,
                     timeout: float = 30.0,
                     retry_attempts: int = 3):
    def decorator(target):
        if isinstance(target, type):
            original_init = target.__init__
            
            @wraps(original_init)
            def new_init(self, *args, **kwargs):
                self._cache = {}
                self._timeout = timeout
                self._retry_attempts = retry_attempts
                original_init(self, *args, **kwargs)
            
            target.__init__ = new_init
            return target
        else:
            @wraps(target)
            def wrapper(*args, **kwargs):
                cache_key = str(args) + str(sorted(kwargs.items()))
                
                if hasattr(wrapper, '_cache') and cache_key in wrapper._cache:
                    return wrapper._cache[cache_key]
                
                result = target(*args, **kwargs)
                
                if not hasattr(wrapper, '_cache'):
                    wrapper._cache = {}
                
                if len(wrapper._cache) < cache_size:
                    wrapper._cache[cache_key] = result
                
                return result
            
            return wrapper
    
    if func_or_class is None:
        return decorator
    else:
        return decorator(func_or_class)

@contextmanager
def weird_context_manager(resource_name: str):
    resources = []
    try:
        resource = f"Resource_{resource_name}_{uuid.uuid4().hex[:8]}"
        resources.append(resource)
        logging.info(f"Acquired resource: {resource}")
        yield resource
    except Exception as e:
        logging.error(f"Error in context manager: {e}")
        raise
    finally:
        for resource in resources:
            logging.info(f"Released resource: {resource}")

async def async_weird_function(data: List[Any], 
                              processor: Callable[[Any], Any] = None,
                              max_concurrent: int = 10) -> List[Any]:
    if processor is None:
        processor = lambda x: x
    
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_item(item):
        async with semaphore:
            await asyncio.sleep(random.uniform(0.1, 0.5))
            return processor(item)
    
    tasks = [process_item(item) for item in data]
    return await asyncio.gather(*tasks)

class WeirdMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['_created_at'] = datetime.datetime.now()
        attrs['_id'] = uuid.uuid4()
        
        for key, value in attrs.items():
            if callable(value) and not key.startswith('_'):
                attrs[key] = complex_decorator(value)
        
        return super().__new__(cls, name, bases, attrs)

class StrangeClass(metaclass=WeirdMetaclass):
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.processor = DynamicImportManager()
    
    def process_with_sklearn(self, X, y):
        if not SKLEARN_AVAILABLE:
            raise ImportError("scikit-learn not available")
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train)
        return clf.score(X_test, y_test)
    
    def weird_computation(self, numbers: List[Union[int, float]]) -> Dict[str, Any]:
        if not numbers:
            return {}
        
        return {
            'mean': statistics.mean(numbers),
            'median': statistics.median(numbers),
            'stdev': statistics.stdev(numbers) if len(numbers) > 1 else 0,
            'hash': hashlib.sha256(str(numbers).encode()).hexdigest()[:16],
            'encoded': base64.b64encode(pickle.dumps(numbers)).decode(),
            'combinations': list(combinations(numbers[:5], 2)) if len(numbers) >= 2 else []
        }

if __name__ == "__main__":
    manager = DynamicImportManager()
    
    config_files = ['config.json', 'config.yaml', 'settings.ini', 'app.toml']
    for config_file in config_files:
        config = manager.load_config_file(config_file)
        if config:
            print(f"Loaded config from {config_file}: {type(config).__name__}")
    
    strange_obj = StrangeClass({"test": "data"})
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = strange_obj.weird_computation(test_numbers)
    print(f"Weird computation result: {result}")
    
    with weird_context_manager("test_resource") as resource:
        print(f"Using resource: {resource}")
    
    print("Complex imports example completed!")