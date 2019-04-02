import tkinter as tk


class SampleApp(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)

        self.master = master
        self.master.title('GUI with Class')
        self.master.geometry("250x100")
        self.master.configure(bg='light blue')
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        self.button_sayhello = self.create_button(
            "Say Hello", "orange red", 'dodger blue', self.say_hello)
        self.button_sayhello.pack()

        self.quit = self.create_button(
            "Close Me", "red", 'dodger blue', self.master.destroy)
        self.quit.pack()

    def create_button(self, label_text, fore_color, back_color, execute_function):
        return tk.Button(self, text=label_text, fg=fore_color,
                         font="Verdana 10 bold", command=execute_function, bg=back_color)

    def say_hello(self):
        print("hi there, everyone!")


def main():
    root = tk.Tk()
    app = SampleApp(master=root)
    app.mainloop()


main()
