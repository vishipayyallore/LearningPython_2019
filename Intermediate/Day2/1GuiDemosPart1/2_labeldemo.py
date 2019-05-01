from tkinter import *

window = None


def create_main_window():
    global window

    window = Tk()
    window.title('Lable Demo')
    window.geometry("250x100")
    window.configure(bg='light blue')


def create_labels():
    label = Label(window, text="Hello Python", font="Verdana 10 bold",
                  fg="blue", bg='light blue')
    label.pack()

    window.mainloop()


def main():
    create_main_window()
    create_labels()


if __name__ == "__main__":
    main()
