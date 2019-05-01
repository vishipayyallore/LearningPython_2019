from tkinter import *

win = Tk()
win.title('Lable Demo')
win.geometry("250x100")
win.configure(bg='light blue')

label = Label(win, text="Hello Python", font="Verdana 10 bold",
              fg="blue", bg='light blue')
label.pack()

win.mainloop()
