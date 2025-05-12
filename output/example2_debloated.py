# Dummy script with various imports

import math
import numpy as np
import random
from collections import defaultdict
from datetime import datetime
import json
from math import pi as p
from math import sqrt as sq

# Some code that uses the imports

def example_function():
    print(os.getcwd())
    print(sys.version)
    print(math.sqrt(16))
    print(np.array([1, 2, 3]))
    print(pd.DataFrame({'A': [1, 2], 'B': [3, 4]}))
    print(random.randint(1, 10))
    print(defaultdict(int))
    print(datetime.now())
    print(re.search('\\d+', 'hello 123 world'))
    print(json.dumps({'key': 'value'}))
    print(p)
    print(sq(25))
    print(path.exists('/some/path'))

# Unused import (should be removed by debloater)
import unused_module

# Call the function
example_function()