import sys
from utilitiesmodule import *

def add_two_numbers(value1: int, value2: int) -> int:
    try:
        return value1 + value2
    except TypeError as error:
        print('Error at add_two_numbers()', error)


def main(value1, value2):
    banner_length = 100
    
    banner("Addition", banner_length)
    results = add_two_numbers(value1, value2)
    print(f'Sum = {results}')
    banner_v2(banner_length)


if( __name__ == '__main__'):
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])

    main(value1, value2)

