from tkinter import *
from tkinter.ttk import *

def say_hello():
    print("hi there, everyone!")


win = Tk()
win.title('Hello Python')
win.geometry("250x100")
win.configure(bg='light blue')

label = Label(win, text="Hello Python", font="Verdana 10 bold")
label.pack()

style = Style()
style.configure("TButton", foreground="green", background="blue")

button = Button(win, text="Say Hello",  command=say_hello)
button.pack()

button = Button(win, text="Close Window!", command=win.quit )
button.pack()

win.mainloop()
