import tkinter as tk
from tkinter import ttk

class SampleApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.create_main_window()

        self.configure_style()

        self.create_widgets()

    def create_main_window(self):
        self.master.title('GUI with Class')
        self.master.geometry("250x100")
        self.master.configure(bg='light blue')
        self.pack()


    def configure_style(self):
        style = ttk.Style()
        style.configure("TButton", foreground="green", background="blue")


    def create_widgets(self):
        self.button_sayhello = self.create_button("Say Hello", "orange red", 'dodger blue', self.say_hello)
        self.button_sayhello.pack()

        self.quit = self.create_button("Close Me", "red", 'dodger blue', self.master.quit)
        self.quit.pack()


    def create_button(self, label_text, fore_color, back_color, execute_function):
        return ttk.Button(self, text=label_text, command=execute_function)


    def say_hello(self):
        print("hi there, everyone!")


def main():
    root = tk.Tk()
    app = SampleApp(master=root)
    app.mainloop()


main()
