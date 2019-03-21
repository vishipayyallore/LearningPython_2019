"""Program to demonstrate the Index of strings
"""


def show_characters_from_positivieindex(string_value):
    for index in range(len(string_value)):
        print(string_value[index], end=' ')
    print()


def show_characters_from_negativeindex(string_value):
    endcount = -1 * (len(string_value) + 1)
    for index in range(-1, endcount, -1):
        print(string_value[index], end=' ')
    print()


def main():
    
    name = input("Enter your name: ")
    show_characters_from_positivieindex(name)

    show_characters_from_negativeindex(name)


# invoking the main method
main()
