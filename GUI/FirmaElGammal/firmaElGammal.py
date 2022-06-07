
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, END

from Main.DigitalSignatureGammal import DigitalSignatureGammal

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def  firmaElGammal(window):

    sig = DigitalSignatureGammal()
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, button_image_6, button_image_7

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def openfile(entry):
        global pathFile
        pathFile= filedialog.askopenfilename()
        if(pathFile) :
            messagebox.showinfo("", "Se cargo el archivo")
            entry.insert(END, "\nArchivo "+pathFile+ " cargado")
        else:
            messagebox.showwarning("", "No se ha cargado el archivo")
        return pathFile

    def openfirme1():
        global pathFirme1
        pathFirme1 = filedialog.askopenfilename()
        if (pathFirme1):
            messagebox.showinfo("", "Se cargo el archivo")
            entry_2.insert(END, "\nArchivo "+pathFile+ " cargado")
        else:
            messagebox.showwarning("", "No se ha cargado el archivo")
        return pathFirme1

    def openfirme2():
        global pathFirme2
        pathFirme2 = filedialog.askopenfilename()
        if (pathFirme2):
            messagebox.showinfo("", "Se cargo el archivo")
            entry_2.insert(END, "\nArchivo "+pathFile+ " cargado")
        else:
            messagebox.showwarning("", "No se ha cargado el archivo")
        return pathFirme2

    def firmar():
        if (pathFile):
            sig.gen_key()
            document = open(pathFile, 'r')
            message=document.read()
            document.close()
            r,s=sig.signature(message)
            f = open("firma2.txt", "w+")
            f.write(str(r))
            f.close()
            p = open("firma3.txt", "w+")
            p.write(str(s))
            p.close()
            entry_1.insert(END, "\nArchivo firmado correctamente.\nLa firma se encuentra en los archivos firma2.txt y firma3.txt")
        else:
            messagebox.showwarning("", "no se ha cargado un archivo")

    def comprobar():
        document = open(pathFile, 'r')
        message = document.read()
        document.close()
        firma = open(pathFirme1, 'r')
        q = firma.read()
        r = int(q)
        firma.close()
        firma2 = open(pathFirme2, 'r')
        t = firma2.read()
        s = int(t)
        firma.close()
        entry_2.insert(END,'\n'+sig.verify(message, r, s))


    canvas = Canvas(
        window,
        bg = "#E4E4EE",
        height = 692-28,
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
        24.0,
        anchor="nw",
        text="Firma Digital ElGammal",
        fill="#000000",
        font=("Inter", 64 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openfile(entry_2),
        relief="flat"
    )
    button_1.place(
        x=728.0,
        y=157.0,
        width=333.0,
        height=65.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openfile(entry_1),
        relief="flat"
    )
    button_2.place(
        x=99.0,
        y=154.0,
        width=347.0,
        height=65.0
    )

    
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: comprobar(),
        relief="flat"
    )
    button_4.place(
        x=769.0,
        y=373.0,
        width=277.0,
        height=65.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openfirme1(),
        relief="flat"
    )
    button_5.place(
        x=733.0,
        y=239.0,
        width=323.0,
        height=65.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_7 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openfirme2(),
        relief="flat"
    )
    button_7.place(
        x=733.0,
        y=305.0,
        width=323.0,
        height=65.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: firmar(),
        relief="flat"
    )
    button_6.place(
        x=157.0,
        y=371.0,
        width=260.0,
        height=65.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        290.5,
        512.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0
    )
    entry_1.place(
        x=46.0,
        y=451.0,
        width=489.0,
        height=120.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        899.5,
        512.0,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0
    )
    entry_2.place(
        x=673.0,
        y=451.0,
        width=453.0,
        height=120.0
    )
