import tkinter as tk
from tkinter import ttk

window = None

def create_main_window():
    global window

    window = tk.Tk()
    window.title('Check Box Demo')
    window.geometry("300x100")
    window.configure(bg='light blue')

def create_spinner():
    current_value = tk.DoubleVar()

    spinner_control = tk.Spinbox(
        window,
        from_=1.0,
        to=100.0,
        increment=.05,
        textvariable=current_value
    )
    spinner_control.pack()

    label_spinner_value = ttk.Label(window, textvariable=current_value)
    label_spinner_value.pack()

    window.mainloop()


def main():
    create_main_window()

    create_spinner()


if __name__ == "__main__":
    main()


