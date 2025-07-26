

FARRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELCIUS_TO_FARENHEIT_FACTOR = 9/5

def convert_to_celcius(temp_in_farenheit):
    """Temperature from farenheit to celcius"""
    temp_in_celcius = (temp_in_farenheit - 32) * FARRENHEIT_TO_CELCIUS_FACTOR
    return temp_in_celcius
def convert_to_farenheit(temp_in_celcius):
    """Temperature from celcius to farenheit"""
    temp_in_farenheit = (temp_in_celcius * CELCIUS_TO_FARENHEIT_FACTOR) + 32
    return temp_in_farenheit

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celcius or Farenheit? (C/F): ").strip().upper()

if unit == "C":
    my_temp = convert_to_farenheit(temperature)
    print(f"{temperature}°C is {my_temp}°F")
elif unit == "F":
    my_temp = convert_to_celcius(temperature)
    print(f"{temperature}°F is {my_temp}°C")
else:
    print("Invalid temperature input. Please enter C or F ")