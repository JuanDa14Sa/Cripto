import re

from tkinter import *
from tkinter import ttk



def preprocess_string(s): #Todo a lowercase, removemos espacios en blanco y agregagamos hasta que sea divisible
    s=s.lower()
    s="".join(s.split())
    while len(s)%4!=0:
        s+='a' #Si la longitud de la cadena no es divisible por 4 entonces agregamos la letra a(al final de s) hasta que lo sea
    return s

def preprocess_stringv2(s):
    s=re.sub('[^a-zA-Z]',"",s) #Elimina todo lo que no sean letras(espacios,números y otros)
    s=s.lower()
    while len(s)%4!=0:
        s+='a'
    return s

def partition(s,b=4): #b es el número de bloques
    s=preprocess_stringv2(s)
    k=len(s)//b #k es el tamaño de cada bloque
    parts = [s[i:i+k] for i in range(0, len(s), k)]
    return parts

def block_convert(s,n):#n=pq 
    b=partition(s)
    num_arr=[]
    for bi in b:
        l=len(bi)
        num=0
        for i in range(l):
            num+=(ord(bi[l-i-1])-97)*26**i
        num_arr.append(num%n)
    return num_arr



root = Tk()
e=Entry(root,fg='green',bg='black')
e.grid(row=0,column=2)
label1=Label(root,text="Cripto").grid(row=0,column=0)


def rsa_button():
    label_=Label(root, text=block_convert(e.get(),77)).grid(row=1, column=1)

button_rsa=Button(root,text="RSA",padx=20,pady=5,command=rsa_button).grid(row=0,column=1)

root.mainloop()