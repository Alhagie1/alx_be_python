

number = int(input("Enter a number to see its multiplication table:"))
current_number = 1

for current_number in range(current_number, 11):
    result = current_number * number
    print(f"{current_number} * {number} = {result}")
    current_number += 1