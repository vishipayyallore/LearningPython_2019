import sys
sys.path.append('C:\\LordKrishna\\GitHub\\LearningPython_2019\\Session1\\CustomModules')
import mathmodule
import bannermodule

program_title = 'Is Prime Validation'

def main():

    bannermodule.create_banner(program_title)
    
    while(True):
        value = input('Enter a Number for Prime verification (Q for Quit): ')

        if(value.strip().upper() == 'Q'):
            print('Thank you for using the application')
            break

        if(value.isnumeric()):
            mathmodule.is_prime(int(value))
        else:
            print('Invalid Input. Please try again!')

    bannermodule.create_footer_row()

main()