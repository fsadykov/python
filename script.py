
def printHello(data):
    print("Hello 1" + data )

def add(x, y):
    """Add Fundction"""
    return x + y

def subtract(x, y):
    """Subtract Fundction"""
    return x - y

def multiply(x, y):
    """Multiply Fundction"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y
