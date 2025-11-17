"""
Simple Calculator with Match Case

"""
def simple_calculator(): 
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    operation = input("Choose the operation (+, -, *, /):")

    match operation: 
        case "+": 
            result = num1+num2
            return print(f"The result is {result}")
        case "-":
            result = num1-num2
            return print(f"The result is {result}")
        case "/": 
            result = num1/num2
            return print(f"The result is {result}")
        case "*": 
            result = num1*num2
            return print(f"The result is {result}")
    

simple_calculator()