import sys
from utilitiesmodule import *

def add_two_numbers(value1: int, value2: int) -> int:
    try:
        return value1 + value2
    except TypeError as error:
        print('Error at add_two_numbers()', error)

def main():
    banner_length = 100
    
    value1 = sys.argv[1]
    value2 = sys.argv[2]

    banner("Addition", banner_length)
    results = add_two_numbers(value1, value2)
    print(f'Sum = {results}')
    banner_v2(banner_length)
    print(__name__)

if(__name__ == '__main__'):
    main()