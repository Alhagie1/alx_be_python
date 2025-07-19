




number = int(input("Enter a number to see its multiplication table: "))
numbers = range(1, 11)
current_number = 1
for current_number in numbers:
    X = number
    Y = current_number
    Z = X * Y
    print(f"{X} * {Y} = {Z}")
    