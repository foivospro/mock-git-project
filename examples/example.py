# Case 1: classic import
import time
# Case 2: import with alias
import random as rd
# Case 3: import specific functions
from math import sqrt, pi, sin
# Case 4: unused import
import shutil
# Case 5: many imports in one line
import collections
# Case 6: import with alias and specific functions
from math import sqrt as sqr
# Case 7: import with alias and specific functions
from math import sqrt as sq, pi as p
# Case 8: import with aliases
# We don't care about importing the same module multiple times
# because Python caches the modules in sys.modules dictionary
import time as t, random as rd
from sklearn.cluster import KMeans


print('Square root of 16:', sqrt(16))
print('Random number between 1 and 10:', rd.randint(1, 10))
time.sleep(1)
print('Waiting for 2 seconds...')
print(bool(re.search('\\d', 'Hello 123 World')))