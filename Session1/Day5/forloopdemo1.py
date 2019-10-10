def display_design(char, end_range):
    for value in range(1, end_range+1):
        print(char * value)

def display_reverse_design(char, end_range):
    for value in range(end_range, 0, -1):
        print(char * value)

def main():
    char = input('Enter a Character: ')
    end_range = int(input('Enter Number: '))

    display_design(char, end_range)
    display_reverse_design(char, end_range)

main()