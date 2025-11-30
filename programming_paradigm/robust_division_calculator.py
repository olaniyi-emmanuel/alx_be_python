def safe_divide(numerator, denominator): 
    try: 
        new_numerator = float(numerator)
        new_denominator = float(denominator)
    except ValueError: 
        return print("Error: Please enter numeric values only.")
        
    
    try:
        result = new_numerator /new_denominator
        return print(f"The result of the division is {result}") 
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
        return

