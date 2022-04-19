import random
import ast
import sys

from Main.RSA import ClassRSA

sys.path.insert(0,'./')
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from GUI.ElGammal.guiGammal import elGammalGUI
from Main.rabin import ClassRabin
from sympy import isprime
from numpy import cumsum

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../GUI/Main/assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root=Tk()
root.geometry('1191x692')
root.resizable(0,0)
root.title('CriptoCodificadorInador')
icono = PhotoImage(file=relative_to_assets("icono.png"))
root.iconphoto(False, icono)

def Main():
    global image_image_1

    canvas = Canvas(
    root,
    bg = "#E4E4EE",
    height = 692-28,
    width = 1191,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 28)
    canvas.create_rectangle(
        619.0,
        9.0,
        1191.0,
        692.0,
        fill="#164FD5",
        outline="")

    canvas.create_text(
        47.0,
        47.0,
        anchor="nw",
        text="CriptoCodificadorInador",
        fill="#000000",
        font=("Inter", 48 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))

    image_1 = canvas.create_image(
        306.0,
        358.0,
        image=image_image_1
    )
    #image_image_1.place(x=0,y=0)

    """ w=Frame(root,width=400,height=240,bg='#EFAD29')
    w.place(x=0,y=28)

    #entrybox for username
    def on_enter(e):
        e1.delete(0,'end')

    def on_leave(e):
        if e1.get()=='':
            e1.insert(0,'username')

    
    e1 =Entry(w,width=28,fg='grey')
    e1.config(font=('consolas',13,'bold'))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'username')
    e1.place(x=70,y=42)



    def on_enter(e):
        e2.delete(0,'end')
    def on_leave(e):
        if e2.get()=='':
            e2.insert(0,'password')

    #entrybox for password
    e2 =Entry(w,width=28,fg='grey')
    e2.config(font=('consolas',13,'bold'))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0,'password')
    e2.place(x=70,y=120-28)



    #command when login button pressed
    def log_command():
        
        file=open('username.txt','r')
        r=file.read()
        s=r.split()
        for j in s:
            dname=j


        myfile=open('password.txt', 'r')
        read=myfile.read()
        split1=read.split()
        for i in split1:
            dpass=i

        if e1.get()==dname and e2.get()==dpass:
            messagebox.showinfo('','     Successfully Logged in     ')
            root.destroy()
        else:
            messagebox.showwarning('try again', 'retry')
    
    Button(w,width=18,height=0,text='Login',command=log_command,border=0,bg='dark red',fg='white').place(x=130,y=146) """

def RSA():

    Rsa = ClassRSA();
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("../GUI/RSA/assets")
    global button_image_1, button_image_2, button_image_3

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def if_integer(string):

        if string[0] == ('-', '+'):
            return string[1:].isdigit()

        else:
            return string.isdigit()

    def comprobar():
        if entry_1.get()=="" or entry_2.get()=="" or entry_3.get()=="" or entry_4.get()=="" or entry_5.get()=="" :
            messagebox.showwarning("", "No puede ir un campo vacio")
            return False
        if if_integer(entry_1.get()) and if_integer(entry_2.get()) and if_integer(entry_3.get()) and if_integer(entry_4.get()) and if_integer(entry_5.get()):
            pass
        else:
            messagebox.showwarning("", "Verifique los campos de la clave, solo enteros")
            return False
        if isprime(int(entry_1.get())) and isprime(int(entry_2.get())):
            pass
        else:
            messagebox.showwarning("", "P o Q no son primos")
            return False
        return True

    def on_enter(e):
        if entry_2.get()=='Inserte un primo válido o genere una clave':
            entry_2.delete(0,'end')

    def on_leave(e):
        if entry_2.get()=='':
            entry_2.insert(0,'Inserte un primo válido o genere una clave')

    def borrarCampos():
        entry_1.delete(0, "end")
        entry_2.delete(0, "end")
        entry_3.delete(0, "end")
        entry_4.delete(0, "end")
        entry_5.delete(0, "end")

    def generarClave():
        Rsa.generarKey()
        borrarCampos()
        entry_1.insert(0, Rsa.p)
        entry_2.insert(0, Rsa.q)
        entry_3.insert(0, Rsa.d)
        entry_4.insert(0, Rsa.n)
        entry_5.insert(0, Rsa.e)

    def capturarClave():
        Rsa.p = int(entry_1.get())
        Rsa.q = int(entry_2.get())
        Rsa.d = int(entry_3.get())
        Rsa.n = int(entry_4.get())
        Rsa.e = int(entry_5.get())

    def encriptar():
        entry_7.delete('1.0',END)
        m = Rsa.preprocess_stringv2(entry_6.get('1.0',END))
        if(comprobar()):
            capturarClave()
            if(m==""):
                messagebox.showwarning("", "Texto a cifrar no puede ir vacio")
            else :
                text = Rsa.block_convert(m)
                encr = []
                for t in text:
                    encr.append(Rsa.encriptar(t))
                des = ','.join(map(str, encr))
                entry_7.insert(END,des)
        else :
            return False

    def desencriptar():
        entry_6.delete('1.0', END)
        m = entry_7.get('1.0', END).replace(' ','').replace('\n','')
        if (comprobar()):
            capturarClave()
            if (m == ""):
                messagebox.showwarning("", "Texto a descifrar no puede ir vacio")
            else:
                decrip = list(map(int,m.split(",")))
                desencr = []
                for t in decrip:
                    desencr.append(Rsa.desencriptar(t))
                textEncrip = Rsa.num_to_text(desencr)
                des = "".join("".join(item) for item in textEncrip)[::-1]
                entry_6.insert(END, des)
        else:
            return False

    canvas = Canvas(
        root,
        bg="#E4E4EE",
        height=692-28,
        width=1191,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=28)
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
        text="RSA",
        fill="#000000",
        font=("Inter", 64 * -1)
    )

    canvas.create_text(
        228.0,
        74.0,
        anchor="nw",
        text="Privado",
        fill="#000000",
        font=("Inter", 36 * -1)
    )

    canvas.create_text(
        834.0,
        141.0,
        anchor="nw",
        text="Público",
        fill="#000000",
        font=("Inter", 36 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: generarClave(),
        relief="flat"
    )
    button_1.place(
        x=761.0,
        y=61.0,
        width=277.0,
        height=65.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: desencriptar(),
        relief="flat"
    )
    button_2.place(
        x=759.0,
        y=629.0,
        width=260.0,
        height=65.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: encriptar(),
        relief="flat"
    )
    button_3.place(
        x=169.0,
        y=629.0,
        width=260.0,
        height=65.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        290.5,
        176.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11}
    )
    entry_1.bind("<FocusIn>", on_enter)
    entry_1.bind("<FocusOut>", on_leave)
    entry_1.insert(0, 'Inserte un primo válido o genere una clave')
    entry_1.place(
        x=46.0,
        y=175.0,
        width=489.0,
        height=57.0,
    )

    canvas.create_text(
        42.0,
        118.0,
        anchor="nw",
        text="Primo p",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        290.5,
        274.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11}
    )
    entry_2.bind("<FocusIn>", on_enter)
    entry_2.bind("<FocusOut>", on_leave)
    entry_2.insert(0, 'Inserte un primo válido o genere una clave')
    entry_2.place(
        x=46.0,
        y=273.0,
        width=489.0,
        height=57.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        290.5,
        384.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11}
    )
    entry_3.place(
        x=46.0,
        y=383.0,
        width=489.0,
        height=57.0
    )

    canvas.create_text(
        43.0,
        216.0,
        anchor="nw",
        text="Primo q",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        917.5,
        274.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11}
    )
    entry_4.place(
        x=673.0,
        y=273.0,
        width=489.0,
        height=57.0
    )

    canvas.create_text(
        43.0,
        314.0,
        anchor="nw",
        text="Número d",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        917.5,
        372.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11}
    )
    entry_5.place(
        x=673.0,
        y=371.0,
        width=489.0,
        height=57.0
    )

    canvas.create_text(
        660.0,
        207.0,
        anchor="nw",
        text="Número n",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        660.0,
        311.0,
        anchor="nw",
        text="Número e",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        290.5,
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
        y=479.0,
        width=489.0,
        height=120.0
    )

    canvas.create_text(
        43.0,
        422.0,
        anchor="nw",
        text="Texto claro",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        899.5,
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
        y=479.0,
        width=453.0,
        height=120.0
    )

    canvas.create_text(
        660.0,
        422.0,
        anchor="nw",
        text="Texto cifrado",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )


def rabin():

    global button_image_1,button_image_2,button_image_3,button_image_4
    rab = ClassRabin()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("../GUI/Rabin/assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
    root,
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
        text="Rabin",
        fill="#000000",
        font=("Inter", 64 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [rab.gen_key(), entry_1.delete(0,'end'), entry_2.delete(0,'end'), entry_3.delete(0,'end'),
        entry_6.delete(0,'end'), entry_1.insert(0,str(rab.p)), entry_2.insert(0,str(rab.q)),
        entry_6.insert(0,str(rab.B)), eText.set(str(rab.n))],
        relief="flat"
    )
    button_1.place(
        x=780.0,
        y=147.0+28,
        width=277.0,
        height=65.0
    )

    def cipherer():
        if is_a_good_prime(entry_1.get()) and is_a_good_prime(entry_2.get()):
            if entry_6.get().isnumeric():
                rab.p = int(entry_1.get())
                rab.q = int(entry_2.get())
                rab.n=rab.p*rab.q
                eText.set(str(rab.n))
                temp = int(entry_6.get())
                entry_6.delete(0,'end')
                entry_6.insert(0, str(temp%rab.n))
                if entry_4.get("1.0",END).replace(' ','').replace('\n','').isalpha():
                    entry_7.config(state='normal')
                    entry_7.delete(1.0,END)
                    entry_7.insert(1.0,str(rab.encrypt(entry_4.get("1.0",END))))
                    entry_7.config(state='disabled')
                else:
                    messagebox.showwarning("", "    ingrese un mensaje válido    ")
            else:
                messagebox.showwarning("", "    ingrese un valor válido de B    ")
        else:
            messagebox.showwarning("", "    ingrese valores primos válidos    ")






    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: cipherer(),
        relief="flat"
        )
    button_2.place(
        x=69.0,
        y=597.0+28,
        width=160.0,
        height=65.0
    )

    def decipherer():
        if is_a_good_prime(entry_1.get()) and is_a_good_prime(entry_2.get()):
            if entry_6.get().isnumeric():
                rab.p = int(entry_1.get())
                rab.q = int(entry_2.get())
                rab.n=rab.p*rab.q
                eText.set(str(rab.n))
                temp = int(entry_6.get())
                entry_6.delete(0,'end')
                entry_6.insert(0, str(temp%rab.n))
                result = rab.num_to_text(rab.decrypt(ast.literal_eval(entry_4.get("1.0",END).replace(' ','').replace('\n',''))))
                # result = rab.decrypt(ast.literal_eval(entry_4.get("1.0",END).replace(' ','').replace('\n','')))
                # Aqui usar rab.num_to_text(rab.decrypt)
                entry_5.config(state='normal')
                entry_5.delete('1.0',END)
                t=''
                block_separation=[0]
                for i in range(len(result)):
                    l= str(result[i][0])
                    t += l +" "
                    block_separation.append(len(l))
                print(block_separation)
                block_separation=cumsum(block_separation)
                print(block_separation)
                entry_5.insert(END, t+'\n')
                posible_colors=['black','red']
                tag=''
                for i in range(len(result)):
                    tag+='a'
                    entry_5.tag_add(tag, "1."+str(block_separation[i]), "1."+str(block_separation[i+1]+1))
                    entry_5.tag_config(tag, foreground=posible_colors[i%2])
                entry_5.config(state='disabled')
                t = ''
            else:
                messagebox.showwarning("", "    ingrese un valor válido de B    ")
        else:
            messagebox.showwarning("", "    ingrese valores primos válidos    ")


    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decipherer(),
        relief="flat"
        )
    button_4.place(
        x=260.0,
        y=597.0+28,
        width=160.0,
        height=65.0
    )

    def is_a_good_prime(p):
        if p.isnumeric():
            p = int(p)
            if p%4==3 and isprime(p):
                return True
            else:
                return False
        else:
            return False


    def calc_n():
        if entry_1.get().isnumeric() and is_a_good_prime(entry_1.get()):
            rab.p=int(entry_1.get())
        if entry_2.get().isnumeric() and is_a_good_prime(entry_2.get()):
            rab.q=int(entry_2.get())
        if entry_1.get().isnumeric() and entry_2.get().isnumeric() and is_a_good_prime(entry_1.get()) and is_a_good_prime(entry_2.get()):
            rab.n=rab.p*rab.q
            eText.set(str(rab.n))
            if entry_6.get().isnumeric():
                temp = int(entry_6.get())
                entry_6.delete(0,'end')
                entry_6.insert(0, str(temp%rab.n))
        else:
            eText.set('Alguno de los valores no es un primo adecuado')

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=calc_n,
        relief="flat"
    )
    button_3.place(
        x=806.0,
        y=239.0+28,
        width=236.0,
        height=51.0
    )

    def on_enter(e):
        if entry_1.get()=='Inserte un primo válido o genere una clave':
            entry_1.delete(0,'end')
    def on_leave(e):
        if entry_1.get()=='':
            entry_1.insert(0,'Inserte un primo válido o genere una clave')

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
        font={'family': 'Consolas', 'size': 11}
    )
    entry_1.bind("<FocusIn>", on_enter)
    entry_1.bind("<FocusOut>", on_leave)
    entry_1.insert(0,'Inserte un primo válido o genere una clave')
    entry_1.place(
        x=55.0,
        y=147.0+28,
        width=489.0,
        height=57.0
    )

    canvas.create_text(
        42.0,
        118.0,
        anchor="nw",
        text="Primo p",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    def on_enter(e):
        if entry_2.get()=='Inserte un primo válido o genere una clave':
            entry_2.delete(0,'end')
    def on_leave(e):
        if entry_2.get()=='':
            entry_2.insert(0,'Inserte un primo válido o genere una clave')

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
        font={'family': 'Consolas', 'size': 11}
    )
    entry_2.bind("<FocusIn>", on_enter)
    entry_2.bind("<FocusOut>", on_leave)
    entry_2.insert(0,'Inserte un primo válido o genere una clave')
    entry_2.place(
        x=55.0,
        y=245.0+28,
        width=489.0,
        height=57.0
    )

    canvas.create_text(
        43.0,
        216.0,
        anchor="nw",
        text="Primo q",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        299.5,
        374.5,
        image=entry_image_3
    )
    eText = StringVar()
    entry_3 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font={'family': 'Consolas', 'size': 11},
        textvariable=eText,
        state='disabled'
    )
    entry_3.place(
        x=55.0,
        y=345.0+28,
        width=489.0,
        height=57.0
    )
    entry_3.configure(disabledbackground="#C4C4C4", disabledforeground="black")

    canvas.create_text(
        43.0,
        318.0,
        anchor="nw",
        text="Número n",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        299.5,
        512.0,
        image=entry_image_4
    )
    entry_4 = Text(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        padx=5,
        pady=5,
        font={'family': 'Consolas', 'size': 12}
    )

    scrollbar_4=Scrollbar(root,orient='vertical',command=entry_4.yview)
    scrollbar_4.place(x=544.0,y=451.0+28,height=120.0)
    entry_4.configure(yscrollcommand=scrollbar_4.set)
    entry_4.place(
        x=55.0,
        y=451.0+28,
        width=489.0,
        height=120.0
    )


    canvas.create_text(
        43.0,
        422.0,
        anchor="nw",
        text="Texto claro o cifrado",
        fill="#164FD5",
        font=("Inter", 24 * -1)
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        917.5,
        512.0,
        image=entry_image_5
    )
    entry_5 = Text(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        # justify='center', #no sirve de nada pero no deja que se ponga el scrollbar que tiene líos con las imágenes
        #padx=5,
        #pady=5,
        font={'family': 'Consolas', 'size': 12},
        wrap=CHAR
    )

    scrollbar_5=Scrollbar(root,orient='vertical',command=entry_5.yview)
    scrollbar_5.place(x=1120.0,y=451.0+28,height=120.0)
    entry_5.configure(yscrollcommand=scrollbar_5.set)
    entry_5.place(
        x=673.0,
        y=451.0+28,
        width=453.0,
        height=120.0
    )
    entry_5.config(state='disabled')
    canvas.create_text(
        677.0,
        422.0,
        anchor="nw",
        text="Texto descifrado",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
    entry_bg_4 = canvas.create_image(
    895.5,
    374.5,
    image=entry_image_6
    )
    entry_6 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font={'family': 'Consolas', 'size': 11}
    )
    entry_6.place(
    x=673.0,
    y=345.0+28,
    width=100.0,
    height=57.0
    )
    canvas.create_text(
    667.0,
    315.0,
    anchor="nw",
    text="Número B",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
    )


    entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
    entry_bg_4 = canvas.create_image(
    895.5,
    374.5,
    image=entry_image_6
    )
    entry_7 = Text(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font={'family': 'Consolas', 'size': 11}
    )
    entry_7.place(
    x=673.0+100.0+53.0,
    y=345.0+28,
    width=300.0,
    height=57.0
    )
    canvas.create_text(
    667.0+100.0+53.0,
    315.0,
    anchor="nw",
    text="Texto cifrado",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
    )
    entry_7.config(state='disabled')

    """ f=Frame(root,width=400,height=240,bg='dark red')
    f.place(x=0,y=28)

    def on_enter(e):
        e5.delete(0,'end')
    def on_leave(e):
        if e5.get()=='':

            e5.insert(0,'username')
    #entrybox for username
    e5 =Entry(f,width=28,fg='grey')
    e5.config(font=('consolas',13,'bold'))
    e5.bind("<FocusIn>", on_enter)
    e5.bind("<FocusOut>", on_leave)
    e5.insert(0,'username')
    e5.place(x=70,y=70-28)



    def on_enter(e):
        e6.delete(0,'end')
    def on_leave(e):
        if e6.get()=='':
            e6.insert(0,'enter new password')

    #entrybox for password
    e6 =Entry(f,width=28,fg='grey')
    e6.config(font=('consolas',13,'bold'))
    e6.bind("<FocusIn>", on_enter)
    e6.bind("<FocusOut>", on_leave)
    e6.insert(0,'enter password')
    e6.place(x=70,y=120-28)

    def entry_done():
        f1=open('username.txt','a')
        f1.truncate(0)
        f1.write(e5.get())
        f1.write(' ')

        f2=open('password.txt','a')
        f2.truncate(0)
        f2.write(e6.get())
        f2.write(' ')
    
        messagebox.showinfo("", "   Password changed successfuly   ")
    

    Button(f,width=18,height=0,text='Reset',command=entry_done,border=0,fg='white',bg='#EFAD29').place(x=130,y=174-28)
 """

Main()

#Main_buttons
Button(root, width=18, height=0, text='I N I C I O', pady=4, command=Main, border=0, bg='#EFAD29', fg='white', activebackground='#EFAD29', activeforeground='white').place(x=0, y=0)
Button(root,width=19,height=0,text='R S A',pady=4,border=0,command=RSA,bg='purple',fg='white',activebackground='purple',activeforeground='white').place(x=130,y=0)
Button(root,width=19,height=0,text='R A B I N',pady=4,border=0,command=rabin,bg='#E4E4EE',fg='black',activebackground='#164FD5',activeforeground='white').place(x=266,y=0)
Button(root,width=19,height=0,text='E L G A M M A L',pady=4,border=0,command=lambda:elGammalGUI(root),bg='#E4E4EE',fg='black',activebackground='#164FD5',activeforeground='white').place(x=370,y=0)
root.mainloop()
