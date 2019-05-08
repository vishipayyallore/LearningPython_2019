
def fibo_recursion(value):
    if value <= 1:
        return value
    else:
        return(fibo_recursion(value-1) + fibo_recursion(value-2))
       

def main():
    number = 6

    print(f'Fibonacci of {number} are ....')
    for i in range(number):
        print(f'{fibo_recursion(i)}', end= ' ')

if __name__ == "__main__":
    main()

