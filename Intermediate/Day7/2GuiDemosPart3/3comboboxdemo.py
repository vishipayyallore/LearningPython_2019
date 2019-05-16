import tkinter as tk
from tkinter import ttk

window = None

def create_main_window():
    global window

    window = tk.Tk()
    window.title('Check Box Demo')
    window.geometry("300x100")
    window.configure(bg='light blue')

def create_combobox():
    selected_item = tk.StringVar()

    combobox_languages = ttk.Combobox(
        window,
        textvariable=selected_item,
        values=["C#", "Java", "Python"]
    )
    combobox_languages.pack()

    label_selected_language = ttk.Label(window, textvariable=selected_item)
    label_selected_language.pack()

    window.mainloop()


def main():
    create_main_window()

    create_combobox()


if __name__ == "__main__":
    main()

