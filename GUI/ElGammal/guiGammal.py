
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import ast
import sys
sys.path.insert(0,'././')
from pathlib import Path
from Main.ElGammal import ElGammal
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

from sympy import isprime



def elGammalGUI(window):
    global button_image_1,button_image_2,button_image_3,button_image_4
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    gammal=ElGammal()

    def check_prime(n):
        if n.isnumeric():
            n=int(n)
            return True if isprime(n) else False
        else:
            return False

    def calc_password():
        if check_prime(entry_1.get()) and entry_2.get().isnumeric() and entry_3.get().isnumeric():
            gammal.setKey(int(entry_1.get()),int(entry_2.get()),int(entry_3.get()))
            entry_2.delete(0,'end')
            entry_3.delete(0,'end')
            entry_2.insert(0,str(gammal.alpha))
            entry_3.insert(0,str(gammal.private_a))
            eTextBeta.set(str(gammal.beta))
            eTextM.set(str(gammal.m))	
        else:
            messagebox.showwarning("", "    Ingrese valores primos válidos    ") 

    def cipherer():
        if entry_6.get(1.0,"end-1c").replace(' ','').replace('\n','').isalpha():
            entry_7.config(state='normal')
            entry_7.delete(1.0,"end-1c")
            entry_7.insert(1.0,str(gammal.encrypt(entry_6.get(1.0,"end-1c"))))
            # entry_7.config(state='disabled')

        else:
            messagebox.showwarning("", "    Ingrese un mensaje válido    ")

    def decipherer():
        if check_prime(entry_1.get()) and entry_2.get().isnumeric() and entry_3.get().isnumeric():
            tmp=entry_7.get(1.0,"end-1c").replace(' ','').replace('\n','')
            print(tmp)
            entry_6.delete(1.0,"end-1c")
            entry_6.insert(1.0,str(gammal.num_to_text(gammal.decrypt(ast.literal_eval(tmp)))))
        else:
            messagebox.showwarning("", "    Ingrese valores válidos    ")

    def on_enterP(e):
        if entry_1.get() == 'Inserte un número primo':
            entry_1.config(fg='black')
            entry_1.delete(0, 'end')

    def on_leaveP(e):
        if entry_1.get() == '':
            entry_1.config(fg='#4d4f4e')
            entry_1.insert(0, 'Inserte un número primo') 

    def on_enterAlpha(e):
        if entry_2.get() == 'Inserte un número entre 1 y p-1':
            entry_2.config(fg='black')
            entry_2.delete(0, 'end')

    def on_leaveAlpha(e):
        if entry_2.get() == '':
            entry_2.config(fg='#4d4f4e')
            entry_2.insert(0, 'Inserte un número entre 1 y p-1') 

    def on_enterA(e):
        if entry_3.get() == 'Inserte un número entre 1 y p-2':
            entry_3.config(fg='black')
            entry_3.delete(0, 'end')

    def on_leaveA(e):
        if entry_3.get() == '':
            entry_3.config(fg='#4d4f4e')
            entry_3.insert(0, 'Inserte un número entre 1 y p-2') 

    def on_enterTextoClaro(e):
        if entry_6.get("1.0",'end-1c').replace('\n','') == 'Inserte texto claro':
           entry_6.delete('1.0', 'end-1c')

    def on_leaveTextoClaro(e):
        if entry_6.get("1.0",'end-1c').replace('\n','') == '':
           entry_6.insert('1.0', 'Inserte texto claro')

    def on_enterTextoEncr(e):
        if entry_7.get("1.0",'end-1c').replace('\n','') == 'Inserte texto encriptado, por ejemplo, [(1,2),(3,4),(5,6)]':
           entry_7.delete('1.0', 'end-1c')

    def on_leaveTextoEncr(e):
        if entry_7.get("1.0",'end-1c').replace('\n','') == '':
           entry_7.insert('1.0', 'Inserte texto encriptado, por ejemplo, [(1,2),(3,4),(5,6)]')

    canvas = Canvas(
        window,
        bg = "#E4E4EE",
        height = 692,
        width = 1191,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
  
    canvas.place(x = 0, y = 28)
    canvas.create_rectangle(
        630.0,
        0.0,
        1442.0,
        1024.0,
        fill="#164FD5",
        outline="")

    canvas.create_text(
        42.0,
        24.0-23,
        anchor="nw",
        text="ElGammal",
        fill="#000000",
        font=("Inter", 64 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [gammal.genKey(), entry_1.delete(0,'end'), entry_2.delete(0,'end'),entry_3.delete(0,'end'), entry_1.insert(0,str(gammal.p)), entry_2.insert(0,str(gammal.alpha)),
        entry_3.insert(0,str(gammal.private_a)),eTextBeta.set(str(gammal.beta)),eTextM.set(str(gammal.m)),entry_1.config(fg='black'),entry_2.config(fg='black'),entry_3.config(fg='black')],
        relief="flat"
    )
    button_1.place(
        x=668.0,
        y=184.0,
        width=207.0,
        height=65.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: calc_password(),
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
        command=lambda: decipherer(),
        relief="flat"
    )
    button_3.place(
        x=761.0,
        y=597.0,
        width=277.0,
        height=65.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: cipherer(),
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
        176.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11},
    )
    entry_1.place(
        x=55.0,
        y=147.0,
        width=489.0,
        height=57.0
    )

    entry_1.bind("<FocusIn>", on_enterP)
    entry_1.bind("<FocusOut>", on_leaveP)
    entry_1.config(fg='#4d4f4e')
    entry_1.insert('0', 'Inserte un número primo')

    canvas.create_text(
        42.0,
        118.0-28,
        anchor="nw",
        text="Primo p",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        299.5,
        274.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11},
    )
    entry_2.place(
        x=55.0,
        y=245.0,
        width=489.0,
        height=57.0
    )
    entry_2.bind("<FocusIn>", on_enterAlpha)
    entry_2.bind("<FocusOut>", on_leaveAlpha)
    entry_2.config(fg='#4d4f4e')
    entry_2.insert('0', 'Inserte un número entre 1 y p-1')

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        297.5,
        372.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11},
    )
    entry_3.place(
        x=53.0,
        y=343.0,
        width=489.0,
        height=57.0
    )
    entry_3.bind("<FocusIn>", on_enterA)
    entry_3.bind("<FocusOut>", on_leaveA)
    entry_3.config(fg='#4d4f4e')
    entry_3.insert('0', 'Inserte un número entre 1 y p-2')

    canvas.create_text(
        43.0,
        216.0-28,
        anchor="nw",
        text="Número alpha",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        765.5,
        368.5,
        image=entry_image_4
    )
    eTextBeta = StringVar()
    entry_4 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=eTextBeta,
        font={'family': 'Consolas', 'size': 11},
    )
    entry_4.place(
        x=681.0,
        y=339.0,
        width=169.0,
        height=57.0
    )

    canvas.create_text(
        43.0,
        314.0-28,
        anchor="nw",
        text="Número a(secreto)",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        1030.5,
        368.5,
        image=entry_image_5
    )
    eTextM = StringVar()
    entry_5 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=eTextM,
        font={'family': 'Consolas', 'size': 11},
    )
    entry_5.place(
        x=946.0,
        y=339.0,
        width=169.0,
        height=57.0
    )

    canvas.create_text(
        668.0,
        301.0-28,
        anchor="nw",
        text="Número beta",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        940.0,
        301.0-28,
        anchor="nw",
        text="Número m",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        294.0,
        512.0,
        image=entry_image_6
    )

    entry_6 = Text(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11}
    )
    entry_6.place(
        x=46.0,
        y=451.0,
        width=496.0,
        height=120.0,
    )
    entry_6.bind("<FocusIn>", on_enterTextoClaro)
    entry_6.bind("<FocusOut>", on_leaveTextoClaro)
    entry_6.insert('1.0', 'Inserte texto claro') 

    canvas.create_text(
        43.0,
        422.0-28,
        anchor="nw",
        text="Texto claro",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )


    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        917.5,
        512.0,
        image=entry_image_7
    )
    entry_7 = Text(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11}
    )
    entry_7.place(
        x=673.0,
        y=451.0,
        width=489.0,
        height=120.0
    )
    entry_7.bind("<FocusIn>", on_enterTextoEncr)
    entry_7.bind("<FocusOut>", on_leaveTextoEncr)
    entry_7.insert('1.0', 'Inserte texto encriptado, por ejemplo, [(1,2),(3,4),(5,6)]') 
    canvas.create_text(
        660.0,
        422.0-28,
        anchor="nw",
        text="Texto cifrado",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )
