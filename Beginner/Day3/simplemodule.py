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
        