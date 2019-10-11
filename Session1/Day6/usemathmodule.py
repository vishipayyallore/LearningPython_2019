import sys
import mathmodule
import bannermodule

program_title = 'Using Modules'
top_header = '='
bottom_header = '-'
function_footer = '+'
count = 50

def main():
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])

    bannermodule.create_banner('Addition of Numbers', top_header, bottom_header, count)
    sum = mathmodule.sum_two_numbers(value1, value2)
    print(f'Sum: {sum}')
    bannermodule.create_footer_row(function_footer, count)

main()
