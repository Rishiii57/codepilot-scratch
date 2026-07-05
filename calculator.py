import unittest

def multiply(a, b):
    return a * b

def calculate_score(score):
    # Validate input: must be numeric
    if not isinstance(score, (int, float)):
        raise ValueError("Input must be a numeric value.")

    # Validate input: must not be negative
    if score < 0:
        raise ValueError("Input cannot be a negative number.")
        
    if score == 0:
        return 0
    return 100 / score
