import tkinter as tk

window = tk.Tk()
window.title('Multi Line Text Box Demo')
window.geometry("700x500")
window.configure(bg='light blue')

multiline_text = tk.Text(window)

# 1st line starting
multiline_text.insert('1.0', "This is Text box.")

# 1st line 8th Character
multiline_text.insert('1.8', 'Multi-line ')

multiline_text.pack()

window.mainloop()
