
# Arithmetic Operation

def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    if operation == "add":
        result = num1 + num2
        return result
    elif operation == "subtract":
        result = num1 - num2
        return result
    elif operation == "multiply":
        result = num1 * num2
        return result
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
            return result
        else:
            print(f"{num1}cannot be divide with zero")
    else:
        print("Operation is invalid.")
perform_operation(5, 6, "add")

my_result = perform_operation(5, 6, "add")
print(my_result)

