

def find_factorial(number):
    if(number == 1):
        return number
    else:
        return number * find_factorial(number-1)

def main():
    number = int(input('Enter a positive number for its factorial: '))
    
    print(f'Factorial of {number} is {find_factorial(number)}')


if __name__ == "__main__":
    main()