def filter_data(lambda_expression, listdata):
    return list(filter(lambda_expression, listdata))


def main():
    names = ['Li', 'Yo', 'Shiva', 'Ali', 'Shyam']

    two_char_names = filter_data(lambda x: len(x) == 2, names)
    print(two_char_names)

    three_and_above_char_names = filter_data(lambda x: len(x) >= 3, names)
    print(three_and_above_char_names)

    only_five_char_names = filter_data(lambda x: len(x) == 5, names)
    print(only_five_char_names)


if __name__ == "__main__":
    main()
