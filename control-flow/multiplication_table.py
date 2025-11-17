"""
Multiplication Table Generator
"""
def multiplication_table():
    num = int(input("Enter a number to see its multiplication table: "))
    for i in range(1, 11): 
        print(f"{num} * {i} = {num * i}")

multiplication_table()