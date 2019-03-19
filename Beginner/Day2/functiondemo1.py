"""
    Program to demonstrate Basics of function
"""

def add_two_numbers(value1, value2):
    return value1 + value2


def add_two_numbers_v2(value1: int, value2: int) -> int:
    return value1 + value2


def main():
    
    value1 = 10
    value2 = 20

    results = add_two_numbers(value1, value2)
    print(f"Sum of {value1} + {value2} = {results}")

    results = add_two_numbers_v2(value1, value2)
    print(f"Sum of {value1} + {value2} = {results}")

# Invoking the main method.
main()