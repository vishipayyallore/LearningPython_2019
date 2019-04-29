def NumberPowerTwo(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


def main():
    number = 5

    print('Using in for loop')
    for val in NumberPowerTwo(number):
        print(val)


if __name__ == "__main__":
    main()
