import tkinter as tk


def create_main_window():
    window = tk.Tk()
    window.title('Window Demo')
    window.geometry("300x80")
    window.configure(bg='light blue')

    window.mainloop()


def main():
    create_main_window()


if __name__ == "__main__":
    main()
