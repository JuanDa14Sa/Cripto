
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import ast
from pathlib import Path
import random

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import END, Tk, Canvas, Entry, Text, Button, PhotoImage

from numpy import arange

from MV import ClassMV

#from Main.MV import ClassMV


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


mene = ClassMV()

window = Tk()

window.geometry("1191x692")
window.configure(bg = "#E4E4EE")


canvas = Canvas(
    window,
    bg = "#E4E4EE",
    height = 692,
    width = 1191,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    630.0,
    0.0,
    1442.0,
    1024.0,
    fill="#164FD5",
    outline="")

canvas.create_text(
    42.0,
    24.0,
    anchor="nw",
    text="Menezes-Vanstone",
    fill="#000000",
    font=("Inter", 64 * -1)
)

def gen_key():
    k = random.randint(0, 70)
    alpha = mene.points[random.randint(0,69)]
    while alpha == 'inf':
        alpha = mene.points[random.randint(0,69)]
    a = random.randint(0, 30)
    beta = mene.mult(a, alpha)
    entry_4.delete('0','end')
    entry_4.insert('0', str(k))
    entry_1.delete('0','end')
    entry_1.insert('0', str(alpha))
    entry_2.delete('0','end')
    entry_2.insert('0', str(a))
    entry_3.delete('0','end')
    entry_3.insert('0', str(beta))
    mene.set_key(alpha,beta,a)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gen_key(),
    relief="flat"
)
button_1.place(
    x=668.0,
    y=184.0,
    width=207.0,
    height=65.0
)

def cal_key():
    x = entry_1.get()
    x = ast.literal_eval(x)
    if entry_4.get().isnumeric():
        if entry_2.get().isnumeric():
            beta=mene.mult(int(entry_2.get()),x)
            mene.set_key(x,beta, int(entry_2.get()))
            entry_3.delete('0','end')
            entry_3.insert('0',str(beta))

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: cal_key(),
    relief="flat"
)
button_2.place(
    x=932.0,
    y=184.0,
    width=207.0,
    height=65.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=761.0,
    y=597.0,
    width=277.0,
    height=65.0
)

def encr():
    x = entry_5.get("1.0",END).replace(' ','').replace('\n','')
    x = list(ast.literal_eval(x))
    if len(x)%2 == 1:
        x.append(0)
    x = [(x[i], x[i + 1]) for i in arange(0, len(x), 2)]
    temp = ''
    for i in x:
        temp += str(mene.cifrar((i[0],i[1]),int(entry_4.get())))+' - '
    entry_6.delete('1.0',END)
    entry_6.insert('1.0', temp[:-2])
    
    

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: encr(),
    relief="flat"
)
button_4.place(
    x=169.0,
    y=597.0,
    width=260.0,
    height=65.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    299.5,
    274.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_1.place(
    x=55.0,
    y=245.0,
    width=489.0,
    height=57.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    297.5,
    372.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_2.place(
    x=53.0,
    y=343.0,
    width=489.0,
    height=57.0
)

canvas.create_text(
    43.0,
    216.0,
    anchor="nw",
    text="Número alpha",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    765.5,
    368.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_3.place(
    x=681.0,
    y=339.0,
    width=169.0,
    height=57.0
)

canvas.create_text(
    43.0,
    314.0,
    anchor="nw",
    text="Número a(secreto)",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    140.5,
    178.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_4.place(
    x=56.0,
    y=149.0,
    width=169.0,
    height=57.0
)

canvas.create_text(
    668.0,
    301.0,
    anchor="nw",
    text="Número beta",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    43.0,
    116.0,
    anchor="nw",
    text="Número k",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    294.0,
    512.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_5.place(
    x=46.0,
    y=451.0,
    width=496.0,
    height=120.0
)

canvas.create_text(
    43.0,
    422.0,
    anchor="nw",
    text="Lista de números separada por comas",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    917.5,
    512.0,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_6.place(
    x=673.0,
    y=451.0,
    width=489.0,
    height=120.0
)

canvas.create_text(
    660.0,
    422.0,
    anchor="nw",
    text="Lista de números separada por guiones",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
