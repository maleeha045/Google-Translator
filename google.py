import tkinter as tk
from tkinter import *
from tkinter import ttk
import googletrans
from googletrans import Translator


def data():
    text = Sor_txt.get(1.0, END)

    trans = Translator()
    s = comb_sor.get()
    d = comb_dest.get()
    textChange = trans.translate(text, src=s, dest=d)
    print(textChange.text)
    Des_txt.delete(1.0, END)
    Des_txt.insert(END, textChange)


root = tk.Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="Red")

lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(
    root, text="Source Text", font=("Time New Roman", 20, "bold"), fg="Black", bg="red"
)
lab_txt.place(x=100, y=100, height=20, width=300)

Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

languages = googletrans.LANGUAGES
list_text = list(languages.values())

comb_sor = ttk.Combobox(frame, values=list_text)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(frame, values=list_text)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("english")

lab_txt = Label(
    root, text="Dest Text", font=("Time New Roman", 20, "bold"), fg="Black", bg="red"
)
lab_txt.place(x=100, y=360, height=20, width=300)


Des_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
Des_txt.place(x=10, y=400, height=150, width=480)

root = mainloop()
