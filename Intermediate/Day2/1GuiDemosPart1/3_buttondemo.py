import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Button Demo')
window.geometry("300x80")
window.configure(bg='light blue')

button_text = tk.StringVar()
button_text.set('Enable')

def enable_disable():
    button_text.set('Enable' if button_text.get() == 'Disable' else 'Disable')

button_enable_disable = ttk.Button(window, textvariable=button_text, command=enable_disable)
button_enable_disable.pack()


window.mainloop()
