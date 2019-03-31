from tkinter import *

win = Tk()
win.title('Hello Python')
win.geometry("250x100")
win.configure(bg = 'light blue')

label = Label(win, text="Hello Python", font="Verdana 10 bold", fg = "blue", bg = 'light blue')
label.pack()

button = Button(win, text="Close Window!", font="Verdana 10 bold", fg = "orange red", command=win.quit, bg = 'dodger blue')
button.pack()

win.mainloop()
