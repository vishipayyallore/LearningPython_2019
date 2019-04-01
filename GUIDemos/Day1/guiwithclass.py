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
        self.button_sayhello = tk.Button(
            self, text="Say Hello", font="Verdana 10 bold", fg="orange red", command=self.say_hello, bg='dodger blue')
        self.button_sayhello.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              font="Verdana 10 bold", command=self.master.destroy, bg='dodger blue')
        self.quit.pack()


    def say_hello(self):
        print("hi there, everyone!")


def main():
    root = tk.Tk()
    app = SampleApp(master=root)
    app.mainloop()


main()
