import sys
sys.path.append('C:\\LordKrishna\\GitHub\\LearningPython_2019\\Session1\\CustomModules')
import bannermodule
import personmodule
import mathmodule

program_title = 'Using Tuples'

def main():
    bannermodule.create_banner(program_title)

    person1 = personmodule.get_person_details()
    personmodule.display_person_details(person1)

    print()
    person2 = (102, "Mohd Azim", False, 2345.67)
    personmodule.display_person_details(person2)
    
    bannermodule.create_footer_row()

    print()
    bannermodule.create_banner('Addition of Numbers', "#", "*")
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])

    sum = mathmodule.sum_two_numbers(value1, value2)
    print(f'\nSum: {sum}')

    bannermodule.create_footer_row()

main()