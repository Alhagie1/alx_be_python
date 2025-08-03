#  A Robust division program


# The function with parameters numerator and denominator
def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        print(f"The result of the division is {result}")
    
    # The Zero division error handle 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    # The Non- numeric value error handle
    except ValueError:
        print("Error: Please enter numeric values only.")

