import sys

from GUI.BlockChain.guiBlockChain import guiBlockChain
from GUI.FirmaElGammal.firmaElGammal import firmaElGammal
from GUI.FirmaRSA.firmaRSA import firmaRSA
from GUI.Main.guiMain import guiMain
from GUI.Menezes.guiMV import guiMV
from GUI.RSA.guiRSA import guiRSA
from tkinter import Tk, Button, PhotoImage
from GUI.ElGammal.guiGammal import elGammalGUI
from GUI.Rabin.guiRabin import guiRabin
from GUI.VSSS.guiVSSS import guiVSSS


class login :

    def __init__(self):

        self.root=Tk()
        self.root.geometry('1191x692')
        self.root.resizable(0,0)
        self.root.title('CriptoCodificadorInador')
        self.icono = PhotoImage(file="Main\icono.png")
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

        buttonFRSA = Button(self.root, width=18, height=0, text='FIRMA RSA', pady=4, border=0.5,
                            command=lambda: firmaRSA(self.root),
                            bg='#E4E4EE', fg='black', activeforeground='white', activebackground='#508484')

        buttonFGammal = Button(self.root, width=18, height=0, text='FIRMA GAMMAL', pady=4, border=0.5,
                            command=lambda: firmaElGammal(self.root),
                            bg='#E4E4EE', fg='black', activeforeground='white', activebackground='#508484')
        buttonVSSS = Button(self.root, width=18, height=0, text='VSSS', pady=4, border=0.5,
                            command=lambda: guiVSSS(self.root),
                            bg='#E4E4EE', fg='black', activeforeground='white', activebackground='#508484')
        buttonBlockChain = Button(self.root, width=18, height=0, text='BLOCKCHAIN', pady=4,
                              command=lambda: guiBlockChain(self.root), border=0.5,
                              bg='#E4E4EE', fg='black', activeforeground='white', activebackground='#508484')

        buttonInicio.place(x=0, y=0)
        buttonRSA.place(x=130, y=0)
        buttonRabin.place(x=266, y=0)
        buttonGammal.place(x=400, y=0)
        buttonEGMV.place(x=535, y=0)
        buttonFRSA.place(x=670, y=0)
        buttonFGammal.place(x=805, y=0)
        buttonVSSS.place(x=940, y=0)
        buttonBlockChain.place(x=1070, y=0)

        self.changeOnHover(buttonInicio, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonRSA, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonRabin, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonGammal, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonEGMV, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonFRSA, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonFGammal, "#164FD5", "#E4E4EE")
        self.changeOnHover(buttonVSSS, "#164FD5", "#E4E4EE")

        self.root.mainloop()

    def changeOnHover(self,button, colorOnHover, colorOnLeave):

        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover,fg='white'))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave,fg='black'))
