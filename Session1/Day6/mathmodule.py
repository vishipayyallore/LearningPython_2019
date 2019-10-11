""" This is a math module

    NAME: mathmodule
"""
import sys

def sum_two_numbers(value1: int, value2: int) -> int:
    """Method to return sum of two numbers

        USAGE: sum = sum_two_numbers(value1, value2)
    """
    return value1 + value2

def main():
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])

    sum = sum_two_numbers(value1, value2)
    print(f'Sum: {sum}')

if __name__ == "__main__":
    main()


