def safe_divide(numerator, denominator): 
    try: 
        new_numerator = float(numerator)
        new_denominator = float(denominator)
    except ValueError: 
        return print("Error: Please enter numeric values only.")
    
    try:
        return print(f"The result of the division is {new_numerator /new_denominator}")
    except ZeroDivisionError:
        return print(f"Error: Cannot divide by zero.")

safe_divide(4, 2)