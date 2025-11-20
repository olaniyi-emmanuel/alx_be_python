FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit): 
    convert_to_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return print(f"{fahrenheit}\u00B0F is {convert_to_celsius}\u00B0C") 

def convert_to_fahrenheit(celsius): 
    convert_to_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return print(f"{celsius}\u00B0C is {convert_to_fahrenheit}\u00B0F")

while True: 
    
    temp_value = int(input(f"Enter the temperature to convert: "))
    temp = input(f"Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if not temp_value:
        print('Invalid temperature degree ')
    else:

        if temp == "C":
            convert_to_fahrenheit(temp_value)
        elif temp == "F": 
            convert_to_celsius(temp_value)
        else:
            print('Invalid temperature degree ')
        
