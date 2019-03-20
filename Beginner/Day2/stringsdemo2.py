
def show_banner(value: str, times: int):
    print(value * times)


def show_all_characters(stringvalue: str):
    show_banner('=', 100)
    
    for character in stringvalue:
        print(character)
    
    show_banner('-', 100)


def show_all_characters_v2(stringvalue: str):
    show_banner('=', 100)
    
    for character in stringvalue:
        print(character, sep=' ', end = ' ')
    
    print('\n')
    show_banner('-', 100)
    print('\n')


def main():
    show_all_characters("ABCD")

    # To Showcase Error condition. Wrong Function Name
    # show_all_characters_("ABCD")

    show_all_characters_v2("Shiva Sai")

    show_all_characters_v2("Mohd Azim")

    show_all_characters_v2("Samule Mathews")


# Invoking main method.
main()