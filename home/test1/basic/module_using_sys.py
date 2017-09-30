import sys

print(" The command line arguments are:")
for i in sys.argv:
    print(i)

print('\n\nthe PYTHONPATH is ', sys.path, '\n')

import os

print(os.getcwd())

from math import sqrt

print("square root of 16 is", sqrt(16))