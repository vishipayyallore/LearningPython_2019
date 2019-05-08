
# Regular functions
def get_power(number):
    return number * number


# Lambda function
power_lambda = lambda number: number * number


def main():
    number = 5

    # With Function
    print(f'With Function Call: {get_power(number)}')

    # With Lambda
    print(f'With Lambda: {power_lambda(number)}')


if __name__ == "__main__":
    main()