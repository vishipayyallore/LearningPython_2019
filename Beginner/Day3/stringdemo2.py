"""
"""

def weight_convertor():
    weight = float(input("Enter you weight: "))
    unit = input("(L)bs OR (K)gs: Default (Kgs) ").upper()
    converted = 0.0
    convert_with = 0.45

    if(unit.strip() is ''):
        unit = 'K'

    if(unit == "L"):
        converted = weight * convert_with
        print(f"{weight} Kgs converted into {converted} Lbs")
    elif(unit == "K"):
        converted = weight / convert_with
        print(f"{weight} Lbs converted into {converted} Kgs")
    else:
        print(f"{weight} without conversion")


def password_verifier():
    password = input("Enter Password (8 - 12 characters): ")

    if( len(password) < 8):
        print("Password must be minimum 8 characters")
    elif( len(password) > 12):
        print("Password must be less than 12 characters")
    else:
        if(password.find(' ') >= 0):
            print('Invalid Password')
        else:
            print('Valid Password')


def traverse_items(value):
    for part in value.split():
        print(part, end= ' | ')

    print() # For generating empty line


def main():
    
    name = input("Enter Long Name/Strings: ")
    traverse_items(name)

    name = input("Enter Long Name/Strings: ")
    traverse_items(name)

    password_verifier()

    weight_convertor()


# Invoking the main method
main()
        
