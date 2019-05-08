def odd_numbers(numbers):
    final_list = list(filter(lambda x: (x % 2 != 0), numbers))
    print(final_list)


def even_numbers(numbers):
    final_list = list(filter(lambda x: (x % 2 == 0), numbers))
    print(final_list)


def filter_data(lambda_expression, listdata):
    return list(filter(lambda_expression, listdata))


def main():
    numbers_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

    odd_numbers(numbers_list)

    even_numbers(numbers_list)

    odd_list = filter_data(lambda x: (x % 2 != 0), numbers_list)
    print(odd_list)

    even_list = filter_data(lambda x: (x % 2 == 0), numbers_list)
    print(even_list)

    custom_list = filter_data(lambda x: (x % 3 == 0), numbers_list)
    print(custom_list)


if __name__ == "__main__":
    main()
