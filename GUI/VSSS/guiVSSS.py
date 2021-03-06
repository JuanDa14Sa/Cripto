
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, filedialog, messagebox

import cv2
from PIL import Image, ImageTk

from Main.ImageEncrypt import ImageEncrypt


def guiVSSS(window):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    imgEncr = ImageEncrypt()
    


    global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def openMainImage():
        global pathMainImage
        pathMainImage= filedialog.askopenfilename(filetypes=(("png files", "*.png"),(("jpg files", "*.jpg"))))
        if(pathMainImage) :
            messagebox.showinfo("", "Se cargó la imagen")
            openWindow('Imagen Principal',pathMainImage)
        else:
            messagebox.showwarning("", "No se ha cargado la imagen")
        return pathMainImage

    def openFirstTransp():
        global pathFirstTransp
        pathFirstTransp= filedialog.askopenfilename(filetypes=(("png files", "*.png"),(("jpg files", "*.jpg"))))
        if(pathFirstTransp) :
            messagebox.showinfo("", "Se cargó la transparencia 1")
            openWindow('Transparencia 1',pathFirstTransp)
            # mainLabel.pack()
        else:
            messagebox.showwarning("", "No se ha cargado la imagen")
        return pathFirstTransp

    def openSecondTransp():
        global pathSecondTransp
        pathSecondTransp= filedialog.askopenfilename(filetypes=(("png files", "*.png"),(("jpg files", "*.jpg"))))
        if(pathSecondTransp) :
            messagebox.showinfo("", "Se cargó la transparencia 2")
            openWindow('Transparencia 2',pathSecondTransp)
            # mainLabel.pack()
        else:
            messagebox.showwarning("", "No se ha cargado la imagen")
        return pathSecondTransp


    def openWindow(title_,path_):
        newWindow = Toplevel(window)
        newWindow.title(title_)
    
        newWindow.geometry("300x300")
    
        img_=ImageTk.PhotoImage(Image.open(path_).resize((300,300),Image.ANTIALIAS))
        label=Label(newWindow,image=img_,width=300,height=300)
        label.pack()
        newWindow.mainloop()
        # mainLabel.pack()

    def generateTransp():
        im1,im2 = imgEncr.encoder(pathMainImage)
        #cv2.imwrite(os.path.splitext(pathMainImage)[0]+'_midresult.png', imgEncr.decoder(im1,im2))
        #cv2.imwrite(os.path.splitext(pathMainImage)[0]+'_img1.png', cv2.cvtColor(im1, cv2.COLOR_BGR2RGB))
        img = Image.fromarray(im1, 'RGB')
        img.save(os.path.splitext(pathMainImage)[0]+'_img1.png')
        img2 = Image.fromarray(im2, 'RGB')
        img2.save(os.path.splitext(pathMainImage)[0]+'_img2.png')
        #cv2.imwrite(os.path.splitext(pathMainImage)[0]+'_img2.png', cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
        messagebox.showinfo("", "Las transparencias se han generado en la ubicación del archivo")
        # openWindow('Transparencia 1',os.path.splitext(pathMainImage)[0]+'_img1.jpg')
        # openWindow('Transparencia 2',os.path.splitext(pathMainImage)[1]+'_img2.jpg')


    def overlayImages():
        if not(pathFirstTransp and pathSecondTransp):
            messagebox.showwarning("", "No se ha cargado la transparencia")
            return
        result = imgEncr.desencoder(pathFirstTransp, pathSecondTransp)
        try:
            cv2.imwrite(os.path.splitext(pathMainImage)[0]+'_result.png', cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
            messagebox.showinfo("", "Las imagen se ha revelado y guardado en la ubicación del archivo")
            openWindow('Resultado',os.path.splitext(pathMainImage)[0]+'_result.png')
        except AttributeError:
            cv2.imwrite(os.path.splitext(pathFirstTransp)[0][:-1] +'_result.png', cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
            messagebox.showinfo("", "Las imagen se ha revelado y guardado en la ubicación del archivo")
            openWindow('Resultado',os.path.splitext(pathFirstTransp)[0][:-1] +'_result.png')
        except NameError:
            cv2.imwrite(os.path.splitext(pathFirstTransp)[0][:-1] +'_result.png', cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
            messagebox.showinfo("", "Las imagen se ha revelado y guardado en la ubicación del archivo")
            openWindow('Resultado',os.path.splitext(pathFirstTransp)[0][:-1] +'_result.png')

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
        24.0,
        anchor="nw",
        text="VSSS",
        fill="#000000",
        font=("Inter", 64 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openMainImage(),
        relief="flat"
    )
    button_1.place(
        x=145.0,
        y=176.0,
        width=307.0,
        height=66.28958129882812
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: generateTransp(),
        relief="flat"
    )
    button_2.place(
        x=145.0,
        y=347.2895812988281,
        width=307.0,
        height=66.2895736694336
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: overlayImages(),
        relief="flat"
    )
    button_3.place(
        x=447.0,
        y=521.0,
        width=365.0,
        height=66.2895736694336
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openFirstTransp(),
        relief="flat"
    )
    button_4.place(
        x=741.0,
        y=180.0,
        width=357.0,
        height=59.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openSecondTransp(),
        relief="flat"
    )
    button_5.place(
        x=741.0,
        y=346.0,
        width=357.0,
        height=59.0
    )
