import tkinter as tk
from tkinter import ttk


class UserForm(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Declaring Variables.
        self.user_name = tk.StringVar()
        self.greetings = tk.StringVar()

        label_user_name = ttk.Label(self, text="Enter your name:")
        text_user_name = ttk.Entry(self, textvariable=self.user_name)

        button_update_message = ttk.Button(self, text="Update", command=self.on_name_change)

        label_greetings = ttk.Label(self, textvariable=self.greetings)

        # Form Layout
        label_user_name.grid(row=0, column=0, sticky=tk.W)
        text_user_name.grid(row=0, column=1, sticky=(tk.W + tk.E))
        button_update_message.grid(row=0, column=2, sticky=tk.E)

        label_greetings.grid(row=1, column=0, columnspan=3)


    def on_name_change(self):
        if self.user_name.get().strip():
            self.greetings.set(f'Hello {self.user_name.get()}')
        else:
            self.greetings.set(f'Hello No Name')


class UserInformationApplication(tk.Tk):

    def __init__(self, screenName=None, baseName=None, className="User Information", useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName,
                         className=className, useTk=useTk, sync=sync, use=use)

        # Windows Properties
        self.title("User Information")
        self.geometry("400x150")

        # Creating the Form
        UserForm(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))


def main():
    window = UserInformationApplication()
    window.mainloop()


if __name__ == "__main__":
    main()
