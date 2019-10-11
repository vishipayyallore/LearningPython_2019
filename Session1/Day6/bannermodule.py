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
