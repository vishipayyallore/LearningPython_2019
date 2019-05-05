
def odd_numbers():
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
    final_list = list(filter(lambda x: (x%2 != 0) , li)) 
    print(final_list)


def even_numbers():
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
    final_list = list(filter(lambda x: (x%2 == 0) , li)) 
    print(final_list)


def filter_data(lambda_expression, listdata):
    return list(filter(lambda_expression, listdata))


def main():
    odd_numbers()

    even_numbers()

    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
    odd_list = filter_data(lambda x: (x%2 != 0) , li)
    print(odd_list)

    even_list = filter_data(lambda x: (x%2 == 0) , li)
    print(even_list)

    custom_list = filter_data(lambda x: (x%3 == 0) , li)
    print(custom_list)


if __name__ == "__main__":
    main()