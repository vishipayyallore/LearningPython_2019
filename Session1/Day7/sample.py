import sys

value1 = sys.argv[1]

while(True):
    value = input('Enter a Number for Prime verification (Q for Quit): ')

    if(value.strip().upper() == 'Q'):
        print('Thank you for using the application')
        break

    print(value)
