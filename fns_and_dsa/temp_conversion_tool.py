

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    """Temperature from farenheit to celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    """Temperature from celsius to farenheit"""
    fahrenheit = (celsius * CELCIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    my_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {my_temp}°F")
elif unit == "F":
    my_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {my_temp}°C")
else:
    print("Invalid temperature input. Please enter C or F ")