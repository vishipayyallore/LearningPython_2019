


def is_prime(number):
    for counter in range(1, (number+1)):
        if( (counter == 1) or (counter == number) ):
            continue
        if(number % counter == 0):
            print(f'{number} Not a Prime Number:')
            break
    else:
        print(f'{number} is a Prime Number:')


def main():
    number = int(input('Enter a Number for Prime verification: '))
    is_prime(number)

    number = int(input('Enter a Number for Prime verification: '))
    is_prime(number)


main()