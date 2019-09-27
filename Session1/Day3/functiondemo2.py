program_title = 'Addition of numbers'

def create_header_row(header_value, count):
    print(header_value * count)

def create_banner(title):
    create_header_row('=', 50)
    print(title)
    create_header_row('-', 50)

def add_two_numbers(value1, value2):
    create_banner(program_title)
    return value1 + value2

def add_two_numbers_v1(value1: int, value2: int) -> int: # Just type hint
    create_banner(program_title)
    return value1 + value2

sum = add_two_numbers(2, 4)
print(f'Output: {sum}')
create_header_row('-', 50)

sum = add_two_numbers_v1('Apple', 4) # This throws Exception
