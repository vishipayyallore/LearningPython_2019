import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Combo Box Demo')
window.geometry("300x100")
window.configure(bg='light blue')

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
