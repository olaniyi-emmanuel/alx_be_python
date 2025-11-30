def safe_divide(numerator, denominator): 
    try: 
        new_numerator = float(numerator)
        new_denominator = float(denominator)
    except ValueError:
        output =  f"Error: Please enter numeric values only."
        return output 
        
    
    try:
        result = f"The result of the division is {new_numerator /new_denominator}"
        return result 
    except ZeroDivisionError:
        output = f"Error: Cannot divide by zero."
        return output 

