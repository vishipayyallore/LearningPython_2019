"""Module to have basic math functions
"""

def add_two_numbers(value1: int, value2: int) -> int:
    """Method to add two add_two_numbers

        ARGUMENTS: 
            Value1: first value
            Value2: second value
    """

    try:
        return value1 + value2
    except TypeError as error:
        print('Error at add_two_numbers()', error)


def divide_two_numbers(value1: int, value2: int) -> float:
    """Method to divide two divide_two_numbers

        ARGUMENTS: 
            Value1: first value
            Value2: second value
    """

    try:
        return value1 / value2
    except ZeroDivisionError as error:
        print('Error at divide_two_numbers()', error)


if __name__ == "__main__":
    pass
    # Update this program
