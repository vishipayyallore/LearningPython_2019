
def show_banner(value: str, times: int):
    print(value * times)


def show_strings_demo1():
    first_name = "Mohd"
    last_name = 'Azim'
    person_description = """
                        My Name is 
                        Mohd Azim
                        """

    show_banner('*', 50)
    print(first_name)
    print(last_name)
    print(person_description)                     
    show_banner('-', 50)


def show_strings_demo2():
    first = "First's"
    last = 'Last"s'

    show_banner('=', 100)
    print(f'Contains both Single and Double Quotes: {first} {last}')
    show_banner('-', 100)


def main():
    show_strings_demo1()

    show_strings_demo2()


# Invoking the main method.
main()
