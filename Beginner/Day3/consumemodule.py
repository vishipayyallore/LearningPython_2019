from simplemodule import is_prime

def main():
    while True:
        value = input('Enter a Number for Prime verification (Q for Quit): ')

        if( value.strip().upper() == 'Q'):
            print('Thanks for using our application')
            break
        
        if(value.isnumeric()):
            is_prime(int(value))
        else:
            print('Invalid Input. Please try again!')


# Invoking the main method.
main()