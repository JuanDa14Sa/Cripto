import random
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from rabin import ClassRabin
from sympy import isprime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root=Tk()
root.geometry('1191x692')
root.resizable(0,0)
root.title('CriptoCodificadorInador')
icono = PhotoImage(file=relative_to_assets("icono.png"))
root.iconphoto(False, icono)
def login():
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

#signup

def signup():
    q=Frame(root,width=400,height=240,bg='purple')
    q.place(x=0,y=28)

    def on_enter(e):
        e3.delete(0,'end')
    def on_leave(e):
        if e3.get()=='':

            e3.insert(0,'enter username')
    #entrybox for username
    e3 =Entry(q,width=28,fg='grey')
    e3.config(font=('consolas',13,'bold'))
    e3.bind("<FocusIn>", on_enter)
    e3.bind("<FocusOut>", on_leave)
    e3.insert(0,'enter username')
    e3.place(x=70,y=70-28)



    def on_enter(e):
        e4.delete(0,'end')
    def on_leave(e):
        if e4.get()=='':
            e4.insert(0,'enter password')

    #entrybox for password
    e4 =Entry(q,width=28,fg='grey')
    e4.config(font=('consolas',13,'bold'))
    e4.bind("<FocusIn>", on_enter)
    e4.bind("<FocusOut>", on_leave)
    e4.insert(0,'enter password')
    e4.place(x=70,y=120-28)




    def entry_done():
        f1=open('username.txt','a')
        f1.truncate(0)
        f1.write(e3.get())
        f1.write(' ')

        f2=open('password.txt','a')
        f2.truncate(0)
        f2.write(e4.get())
        f2.write(' ')
    
        messagebox.showinfo("", "    successfully registered    ")
    

    Button(q,width=18,height=0,text='Signup',command=entry_done,border=0,fg='purple',bg='white').place(x=130,y=174-28)



def rabin():

    global button_image_1,button_image_2,button_image_3
    rab = ClassRabin()



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
        command=lambda: [rab.gen_key(), entry_1.delete(0,'end'), entry_2.delete(0,'end'), entry_3.delete(0,'end'),entry_6.delete(0,'end'), entry_1.insert(0,str(rab.p)), entry_2.insert(0,str(rab.q)),entry_6.insert(0,str(rab.B)), eText.set(str(rab.n))],
        relief="flat"
    )
    button_1.place(
        x=780.0,
        y=147.0+28,
        width=277.0,
        height=65.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print('yes'),
        # [
        #     if isprime(entry_1.get()) and entry_1.get()%4==3:
        #         rab.p=int(entry_1.get())
        #     else:
        # ]
        relief="flat"
        )
    button_2.place(
        x=169.0,
        y=597.0+28,
        width=260.0,
        height=65.0
    )

    def calc_n():
        rab.p=int(entry_1.get())
        rab.q=int(entry_2.get())
        rab.n=rab.p*rab.q
        eText.set(str(rab.n))
        rab.B=random.randint(1,rab.n)
        entry_6.delete(0,'end')
        entry_6.insert(0,str(rab.B))

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
        font={'family': 'Consolas', 'size': 12}
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
        text="Texto cifrado",
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
    width=445.0,
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
    def on_enter(e):
        if entry_6.get()=='Inserte un número valido o genere una clave':
            entry_6.delete(0,'end')
    def on_leave(e):
        if entry_6.get()=='':
            entry_6.insert(0,'Inserte un número valido o genere una clave')

    entry_6.bind("<FocusIn>", on_enter)
    entry_6.bind("<FocusOut>", on_leave)
    entry_6.insert(0,'Inserte un número valido o genere una clave')
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
login()

#Main_buttons
Button(root,width=18,height=0,text='I N I C I O',pady=4,command=login,border=0,bg='#EFAD29',fg='white',activebackground='#EFAD29',activeforeground='white').place(x=0,y=0)
Button(root,width=19,height=0,text='R S A',pady=4,border=0,command=signup,bg='purple',fg='white',activebackground='purple',activeforeground='white').place(x=130,y=0)
Button(root,width=19,height=0,text='R A B I N',pady=4,border=0,command=rabin,bg='#E4E4EE',fg='black',activebackground='#164FD5',activeforeground='white').place(x=266,y=0)
root.mainloop()
