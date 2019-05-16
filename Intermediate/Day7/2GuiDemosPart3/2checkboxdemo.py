import tkinter as tk
from tkinter import ttk

window = None

def create_main_window():
    global window

    window = tk.Tk()
    window.title('Check Box Demo')
    window.geometry("300x100")
    window.configure(bg='light blue')

def create_checkbox():
    is_manager = tk.BooleanVar()

    checkbox_is_manager = ttk.Checkbutton(
        text="Is Manager",
        variable=is_manager
    )
    checkbox_is_manager.pack()

    label_is_manager = ttk.Label(window, textvariable=is_manager)
    label_is_manager.pack()

    window.mainloop()


def main():
    create_main_window()

    create_checkbox()


if __name__ == "__main__":
    main()

