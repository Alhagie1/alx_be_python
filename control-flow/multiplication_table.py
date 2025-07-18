

number = int(input("Enter a number to see its multiplication table:"))
current_number = 1

for current_number in range(current_number, 11):
    X = number
    Y = current_number
    Z = X * Y
    print(f"{X} * {Y} = {Z}")
    