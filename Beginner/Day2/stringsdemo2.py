
def show_banner(value: str, times: int):
    print(value * times)


def show_all_characters(stringvalue: str):
    show_banner('=', 100)
    
    for character in stringvalue:
        print(character, sep=' ', end = ' ')
    
    print('\n')
    show_banner('-', 100)
    print('\n')


def main():
    show_all_characters("Shiva Sai")

    show_all_characters("Mohd Azim")

    show_all_characters("Samule Mathews")


# Invoking main method.
main()