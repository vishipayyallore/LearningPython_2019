def filter_data(lambda_expression, listdata):
    return list(filter(lambda_expression, listdata))


def main():
    names = ['a','bb','ccc','dd']
    two_char_names = filter_data(lambda x : len(x) == 2, names)
    print(two_char_names)

    twoorthree_char_names = filter_data(lambda x : len(x) >= 2, names)
    print(twoorthree_char_names)


if __name__ == "__main__":
    main()