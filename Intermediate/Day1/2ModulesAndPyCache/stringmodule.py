"""Module to have basic math functions
"""

def string_strip(stringvalue: str):
    """Method to divide two divide_two_numbers

        ARGUMENTS: 
            Value1: first value
            Value2: second value
    """
    return "".join(stringvalue.split())


def string_mask(stringvalue: str):
    """Method to divide two divide_two_numbers

        ARGUMENTS: 
            Value1: first value
            Value2: second value
    """
    for char in stringvalue:
        print(ord(char), end=' | ')


if __name__ == "__main__":
    pass
    # Update this program