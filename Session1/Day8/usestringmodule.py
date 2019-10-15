import sys
sys.path.append('C:\\LordKrishna\\GitHub\\LearningPython_2019\\Session1\\CustomModules')
import bannermodule
import stringmodule

program_title = 'String Modules'
menu_options = ["1. Show Charaters", "2. Show Characters V2", "3. Show Reverse String", "4. Show Swap Case", "5. Quit"]

def display_menu_options(program_title, menu_options):
    bannermodule.create_banner(program_title)
    for menu in menu_options:
        print(menu)
    bannermodule.create_footer_row()

def show_stringmodule_demo(switch, data):
    if(switch == 1):
        stringmodule.show_characters_v1(data)
    elif(switch == 2):
        stringmodule.show_characters_v2(data)
    elif(switch == 3):
        stringmodule.show_reverse_string(data)
    elif(switch == 4):
        stringmodule.show_swapcase(data)

def main():
    while(True):
        display_menu_options(program_title, menu_options)
        switch = int(input('Enter a Choice: '))

        if(switch == 5):
            print('Thank you for using the application')
            break
        
        data = input('Enter Data: ')
        show_stringmodule_demo(switch, data)

# Entry Point
main()
