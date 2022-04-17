from sympy import isprime
import random
import re

class ElGammal:
    def __init__(self):
        self.p=0
        self.alpha=0
        self.private_a=0
        self.beta=0

        # self.p=11
        # self.alpha=2
        # self.private_a=3
        # self.beta=8


    def genKey(self):
        primes_list=[i for i in range(650,10000) if isprime(i)] #El rango es para codificar el bloque sin colisión
        self.p=random.choice(primes_list)
        self.alpha=random.randint(0,self.p-1)
        self.private_a=random.randint(0,self.p-1)
        self.beta=pow(self.alpha,self.private_a,self.p)
        self.m=random.randint(0,self.p-1)
    
    def setKey(self,p,alpha,private_a):
        self.p=p
        self.alpha=alpha%p
        self.private_a=private_a%p
        self.beta=pow(self.alpha,self.private_a,self.p)
        self.m=random.randint(0,self.p-1)
    


    def preprocess_stringv3(self,s):
        s=re.sub('[^a-zA-Z]',"",s) #Elimina todo lo que no sean letras(espacios,números y otros)
        s=s.lower()
        # s=s[::-1]
        while len(s)%2!=0:
            s+='a'
        return s

    def block_convertv2(self,s,n,b=2): #Cada bloque se compone de 4 letras
        s=self.preprocess_stringv3(s)
        # s=s[::-1]
        b=[s[i:i+b] for i in range(0,len(s),b)]
        num_arr=[]
        for bi in b:
            l=len(bi)
            num=0
            for i in range(l):
                num+=((ord(bi[i])-97))*26**i
            num_arr.append(num%n)
        return num_arr

    def num_to_text(self,arr):
        decimal_text=[]
        final_text=[]
        for block in arr:
            dec_num=[]
            cond=True
            while cond:
                dec_num.append(block%26)
                if block//26==0:
                    cond=False
                block//=26
            decimal_text.append(dec_num)
        final_string=[]
        for char in decimal_text:
            s=''
            for n in char:
                s+=(chr(n+97))
            final_string.append(s)
        final_text.append(final_string)
        message=''
        for s in final_text[0]:
            message+=s
        return message

    def encrypt(self,x): #x es el mensaje a cifrar
        x_=self.block_convertv2(x,self.p)
        encrypt_m=[]
        for x in x_:
            y1=pow(self.alpha,self.m,self.p)
            y2=(pow(self.beta,self.m,self.p)*x)%self.p
            encrypt_m.append((y1,y2))
        return encrypt_m

    def extended_gcd(self,a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def inverse_mod(self,a,n):
        return self.extended_gcd(a,n)[1]

    def decrypt(self,ys):
        sol=[]
        for ys_ in ys:
            y1,y2=ys_
            sol.append(y2*(self.inverse_mod(pow(y1,self.private_a,self.p),self.p))%self.p)
        return sol

# gammal=ElGammal()
# gammal.genKey()
# m='This is a long proof'
# print(gammal.preprocess_stringv3(m))
# print(gammal.block_convertv2(m,gammal.p))
# e=gammal.encrypt(m)
# print(e)
# d=gammal.decrypt(e)
# print(d)
# print(gammal.num_to_text(d))

