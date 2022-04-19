import sys
from GUI.Main.guiMain import guiMain
from GUI.Menezes.guiMV import guiMV
from GUI.RSA.guiRSA import guiRSA
from tkinter import Tk, Button, PhotoImage
from GUI.ElGammal.guiGammal import elGammalGUI
from GUI.Rabin.guiRabin import guiRabin


class login :

    def __init__(self):

        self.root=Tk()
        self.root.geometry('1191x692')
        self.root.resizable(0,0)
        self.root.title('CriptoCodificadorInador')
        self.icono = PhotoImage(file="icono.png")
        self.root.iconphoto(False, self.icono)

        t = guiMain(self.root)

        # Main_buttons
        buttonInicio = Button(self.root, width=18, height=0, text='I N I C I O', pady=4, command= lambda : guiMain(self.root), border=0.5,
                              bg='#E4E4EE', fg='black', activeforeground='white', activebackground='#508484')
        buttonRSA = Button(self.root, width=18, height=0, text='R S A', pady=4, border=0.5, command=lambda : guiRSA(self.root), bg='#E4E4EE',
                           fg='black', activeforeground='white', activebackground='#508484')
        buttonRabin = Button(self.root, width=18, height=0, text='R A B I N', pady=4, border=0.5, command=lambda : guiRabin(self.root),
                             bg='#E4E4EE', fg='black', activeforeground='white', activebackground='#508484')
        buttonGammal = Button(self.root, width=18, height=0, text='E L G A M M A L', pady=4, border=0.5,
                              command=lambda: elGammalGUI(self.root), bg='#E4E4EE', fg='black', activeforeground='white',
                              activebackground='#508484')
        buttonEGMV = Button(self.root, width=18, height=0, text='E G M V', pady=4, border=0.5, command=lambda: guiMV(self.root),
                            bg='#E4E4EE', fg='black', activeforeground='white', activebackground='#508484')

        buttonInicio.place(x=0, y=0)
        buttonRSA.place(x=130, y=0)
        buttonRabin.place(x=266, y=0)
        buttonGammal.place(x=400, y=0)
        buttonEGMV.place(x=535, y=0)

        self.changeOnHover(buttonInicio, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonRSA, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonRabin, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonGammal, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonEGMV, "#164FD5", "#E4E4EE")

        self.root.mainloop()

    def changeOnHover(self,button, colorOnHover, colorOnLeave):

        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover,fg='white'))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave,fg='black'))
