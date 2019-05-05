

def find_factorial(number):
    if(number == 1):
        return number
    else:
        return number * find_factorial(number-1)


print(find_factorial(5))