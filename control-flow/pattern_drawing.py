"""
Drawing Patterns with Nested Loops
"""

def pattern_drawing(): 
    number = int(input("Enter the size of the pattern:."))

    while True: 
        for i in range(0, number): 
            print("*", end="")
        print("\n")

pattern_drawing()