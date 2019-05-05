
# Regular functions
def get_power(number):
    return number * number


# Lambda function
power_lambda = lambda number: number * number


def main():
    print(power_lambda(5))


if __name__ == "__main__":
    main()