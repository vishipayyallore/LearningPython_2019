""" This is a math module

    NAME: mathmodule
"""
import sys

def sum_two_numbers(value1: int, value2: int) -> int:
    """Method to return sum of two numbers

        USAGE: sum = sum_two_numbers(value1, value2)
    """
    return value1 + value2


def not_a_prime(number):
    print(f'{number} Not a Prime Number:')


def is_prime(number):
    if(number <= 1):
        not_a_prime(number)
        return

    for counter in range(1, (number+1)):
        if( (counter == 1) or (counter == number) ):
            continue
        if(number % counter == 0):
            not_a_prime(number)
            break
    else:
        print(f'{number} is a Prime Number:')


def main():
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])

    sum = sum_two_numbers(value1, value2)
    print(f'Sum: {sum}')

if __name__ == "__main__":
    main()


