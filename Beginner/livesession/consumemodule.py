from mathmodule import (add_two_numbers, divide_two_numbers)
from utilitiesmodule import *
from stringmodule import *

def perform_add():
    banner('Add Example', 100)
    try:
        value1 = int(input('Enter Value 1: '))
        value2 = int(input('Enter Value 2: '))
        results = add_two_numbers(value1, value2)
        print(results)
    except ValueError as error:
        print('Error at perform_add()', error)
    banner_v2(100)

def main():
    while True:
        choice = input("(A)dd, (S)pace Strip, (M)ask, (Q)uit >>> ").strip().upper()

        if(choice == 'Q'):
            print('\nClosing the application')
            break
        
        if(choice == 'A'):
            perform_add()
        if(choice == 'S'):
            results = string_strip("One Two Three Four")
            print(f'Computed: {results}')
        if(choice == 'M'):
            string_mask("Hafeez")
        else:
            print('\nInvalid Input. Please try again')
    else:
        print("\nThank you for using the application!")

main()

    # add = add_two_numbers(10, 20)
    # print(add)

    # add = add_two_numbers(10, 'a')
    # print(add)