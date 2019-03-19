"""
    Program to demonstrate Basics of function
"""

def add_two_numbers(value1, value2):
    return value1 + value2


def add_two_numbers_v2(value1: int, value2: int) -> int:
    return value1 + value2
    

def main():
    
    value1 = int(input("Enter Value 1: "))
    value2 = int(input("Enter Value 2: "))

    results = add_two_numbers(value1, value2)
    print(f"Sum (V1) of {value1} + {value2} = {results}")

    results = add_two_numbers_v2(value1, value2)
    print(f"Sum  (V2) of {value1} + {value2} = {results}")

    # We will use this scnario for Exception handling
    results = add_two_numbers_v2(value1, "S")
    print(f"Sum of {value1} + {value2} = {results}")

# Invoking the main method.
main()
