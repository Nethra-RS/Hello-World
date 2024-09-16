import math
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        raise ValueError("cannot divide by zero")
    return x/y
def squareroot(x):
    return math.sqrt(x)
