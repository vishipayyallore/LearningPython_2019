
def create_header_row(header_value, count, add_new_line):
    print(header_value * count)

    if(add_new_line):
        print()

def create_footer_row(header_value = "+", count = 50):
    print()
    print(header_value * count)

def create_banner(title, top_header = "=", bottom_header = "-", count = 50):
    create_header_row(top_header, count, False)
    print(title)
    create_header_row(bottom_header, count, True)
