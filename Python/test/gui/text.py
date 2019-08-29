from tkinter import *

root = Tk()

text = Text(width=650, height=450,fg='black', wrap=WORD)

text.pack()
root.title("Jeeno Text")
root.geometry("650x450+300+200")
root.mainloop()
