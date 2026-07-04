def divide(a, b):
    # Bug: what if b is 0?
    return a / b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def calculate_score(score):
    # Handle the case where score is 0 to prevent ZeroDivisionError
    if score == 0:
        return 0
    return 100 / score
