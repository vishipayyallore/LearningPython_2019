def modify_data(lambda_expression, listdata):
    return list(map(lambda_expression, listdata))


def main():
    names = ['shiva', 'sai', 'Azim', 'Mathews', 'samules']
    capitalize_names = modify_data(lambda x: x.capitalize(), names)
    print(capitalize_names)

    numbers = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
    multiply_by_two = modify_data(lambda x: x*2, numbers)
    print(multiply_by_two)

    no_change = modify_data(lambda x: x, numbers)
    print(no_change)


if __name__ == "__main__":
    main()
