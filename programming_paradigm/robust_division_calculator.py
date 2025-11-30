def safe_divide(numerator, denominator): 
    try: 
        new_numerator = float(numerator)
        new_denominator = float(denominator)
    except ValueError: 
        print("Error: Please enter numeric values only.")
        return 
    
    try:
        result = new_numerator /new_denominator
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
        return 

safe_divide(4, 2)