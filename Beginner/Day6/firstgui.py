from tkinter import *

win = Tk()
win.title('Hello Python')
win.geometry("250x100")

label = Label(win, text="Hello Python", font="Verdana 10 bold", fg = "blue")
label.pack()

button = Button(win, text="Click Here!", font="Verdana 10 bold", fg = "green")
button.pack()

win.mainloop()
