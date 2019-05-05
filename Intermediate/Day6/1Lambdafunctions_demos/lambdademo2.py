def lambda_function(value):
    return lambda a: a * value


def main():
    number = 10

    double_number = lambda_function(2)
    print(double_number(number))

    triple_number = lambda_function(3)
    print(triple_number(number))


if __name__ == "__main__":
    main()
