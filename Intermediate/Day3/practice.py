import tkinter as tk
from tkinter import ttk

class SampleApp(tk.Frame):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.master = parent
        
        self.create_main_window()

    def create_main_window(self):
        self.master.title('GUI with Class')
        self.master.geometry("250x100")
        self.master.configure(bg='light blue')
        self.pack()

        style = ttk.Style()
        style.configure("TButton", foreground="green", background="blue")

        self.button_sayhello = ttk.Button(self, text="Say Hello", command= self.say_hello)
        self.button_sayhello.pack()

        self.quit = ttk.Button(self, text="Close Me", command=self.master.quit)
        self.quit.pack()

    def say_hello(self):
        print("hi there, everyone!")

def main():
    root = tk.Tk()

    app = SampleApp(parent=root)

    app.mainloop()


main()    