# file1.py
def add(a, b):
    return a + b

# file2.py
from file1 import add

print("Sum =", add(2, 3))