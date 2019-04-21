"""Module to have basic math functions
"""

def banner(message, header='=', footer='-'):
    """Method to divide two divide_two_numbers

        ARGUMENTS: 
            Value1: first value
            Value2: second value
    """

    length = len(message) + 1

    print()
    print(header * length)
    print(message)
    print(footer * length)


def banner_v2(length, footer='*'):
    """Method to divide two divide_two_numbers

        ARGUMENTS: 
            Value1: first value
            Value2: second value
    """

    print(footer * length)
    print()


if __name__ == "__main__":
    pass
    # Update this program
