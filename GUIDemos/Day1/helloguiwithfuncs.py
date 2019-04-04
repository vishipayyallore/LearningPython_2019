from tkinter import *


def say_hello():
    print("hi there, everyone!")


def create_first_gui():    
    win = Tk()
    win.title('Hello Python')
    win.geometry("250x100")
    win.configure(bg='light blue')

    label = Label(win, text="Hello Python", font="Verdana 10 bold",
                fg="blue", bg='light blue')
    label.pack()

    button = Button(win, text="Say Hello", font="Verdana 10 bold",
                    fg="orange red", command=say_hello, bg='dodger blue')
    button.pack()

    button = Button(win, text="Close Window!", font="Verdana 10 bold",
                    fg="orange red", command=win.quit, bg='dodger blue')
    button.pack()

    win.mainloop()


def main():
    create_first_gui()


main()
