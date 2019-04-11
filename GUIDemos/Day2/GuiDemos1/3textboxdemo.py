import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Text Box Demo')
window.geometry("250x100")
window.configure(bg='light blue')

user_name = tk.StringVar()
user_name.set('No Name')

textbox_user_name = ttk.Entry(
    window,
    textvariable=user_name
)
textbox_user_name.pack()

label_user_name = ttk.Label(window, textvariable=user_name)
label_user_name.pack()

window.mainloop()
