#  A Robust division program


# The function with parameters numerator and denominator
def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    # The Zero division error handle 
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    # The Non- numeric value error handle
    except ValueError:
        return "Error: Please enter numeric values only."

