import tkinter as tk
from tkinter import ttk

window = None
button_text = None


def create_main_window():
    global window, button_text

    window = tk.Tk()
    window.title('Button Demo')
    window.geometry("300x80")
    window.configure(bg='light blue')

    button_text = tk.StringVar()
    button_text.set('Enable')


def create_buttons():
    button_enable_disable = ttk.Button(window, textvariable=button_text, command=enable_disable)
    button_enable_disable.pack()

    window.mainloop()

def enable_disable():
    button_text.set('Enable' if button_text.get() == 'Disable' else 'Disable')


def main():
    create_main_window()

    create_buttons()

if __name__ == "__main__":
    main()

