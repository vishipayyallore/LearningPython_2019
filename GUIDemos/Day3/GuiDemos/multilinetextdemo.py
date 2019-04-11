import tkinter as tk

window = tk.Tk()
multiline_text = tk.Text(window)

# 1st line starting
multiline_text.insert('1.0', "This is Text box.")

# 1st line 8th Character
multiline_text.insert('1.8', 'Multi-line ')

multiline_text.pack()

window.mainloop()
