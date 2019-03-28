def add_two_numbers(value1: int, value2: int) -> int:
    try:
        return value1 + value2
    except TypeError as error:
        print('Error at add_two_numbers()', error)


def main():
    results = add_two_numbers(10, 20)
    print(f'Sum = {results}')

    print(__name__)

main()

