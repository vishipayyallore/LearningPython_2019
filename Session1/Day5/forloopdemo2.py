def display_tables(number, start, end):
    for counter in range(start, end+1):
        print(f'{number} * {counter} = {number * counter}')


def main():
    number = int(input('Enter Number: '))
    start = int(input('Enter Start: '))
    end = int(input('Enter End: '))
    
    display_tables(number, start, end)


main()
