
def show_banner(value: str, times: int):
    print(value * times)


def show_forloop_demo1(end_value: int):
    show_banner('=', 100)
    
    for counter in range(end_value):
        print(counter, end=' ')
        
    print() # for new line
    
    show_banner('-', 100)


def show_forloop_demo2(end_value: int):
    show_banner('=', 100)

    for counter in range(1, end_value):
        print(counter, end=' ')
    
    print() # for new line

    show_banner('-', 100)


def show_forloop_demo3(end_value: int):
    show_banner('=', 100)

    for counter in range(0, end_value, 5):
        print(counter, end=' ')
    else:
        print('\nFinished the for loop')

    show_banner('-', 100)


def main():
    show_forloop_demo1(11)

    show_forloop_demo2(11)

    show_forloop_demo3(100)


# Invoking main method
main()