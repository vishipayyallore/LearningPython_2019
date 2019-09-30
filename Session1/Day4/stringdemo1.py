program_title = 'String Demos'
top_header = '='
bottom_header = '-'
function_footer = '+'
count = 50

def create_header_row(header_value, count, add_new_line):
    print(header_value * count)

    if(add_new_line):
        print()

def create_footer_row(header_value, count):
    print()
    print(header_value * count)

def create_banner(title, top_header, bottom_header, count):
    create_header_row(top_header, count, False)
    print(title)
    create_header_row(bottom_header, count, True)

def display_all_items(data: str, end_value: str):
    for value in data:
        print(value, end=end_value)
    print()

def display_all_words(data: str, end_value: str):
    for word in data.split():
        print(word, end=end_value)

def show_all_items_demo():
    data = input('Enter your Name: ')
    end_value = input('Enter End Value: ')

    create_banner('Displaying All Characters', top_header, bottom_header, count)
    display_all_items(data, end_value)
    create_footer_row(function_footer, count)

def show_all_words_demo():
    data = input('Enter a Long String data: ')
    end_value = input('Enter End Value: ')

    create_banner('Displaying All Words', top_header, bottom_header, count)
    display_all_words(data, end_value)
    create_footer_row(function_footer, count)

def main():
    show_all_items_demo()
    show_all_words_demo()

# Program Entry Point
main()
