import random
import re
from sympy import isprime


class ClassRabin:
    def __init__(self):  
        self.p = 0
        self.q = 0
        self.B = 0
        self.n =0
    
    # def __init__(self,p,q,B=9):
    #     self.p = p
    #     self.q = q
    #     self.B = B
    #     self.n =p*q

    def primes_3_mod_4(self):
        primes_list=[]
        for i in range(1000,100000):
            if i%4==3 and isprime(i):
                primes_list.append(i)
        return random.choices(primes_list,k=2)

    def gen_key(self):
        self.p,self.q=self.primes_3_mod_4()
        self.n=self.p*self.q
        self.B=random.randint(1,self.n)

    # def preprocess_stringv2(self,s):
    #     s=re.sub('[^a-zA-Z]',"",s) #Elimina todo lo que no sean letras(espacios,números y otros)
    #     s=s.lower()
    #     s=s[::-1]
    #     while len(s)%4!=0:
    #         s+='a'
    #     return s

    # def partition(self,s,b=4): #b es el número de bloques
    #     s=self.preprocess_stringv2(s)
    #     k=len(s)//b #k es el tamaño de cada bloque
    #     parts = [s[i:i+k] for i in range(0, len(s), k)]
    #     return parts

    # def block_convert(self,s,n):#n=pq 
    #     b=self.partition(s)
    #     num_arr=[]
    #     for bi in b:
    #         l=len(bi)
    #         num=0
    #         for i in range(l):
    #             num+=((ord(bi[i])-96))*26**i
    #         num_arr.append(num%n)
    #     return num_arr


    def preprocess_stringv3(self,s):
        s=re.sub('[^a-zA-Z]',"",s) #Elimina todo lo que no sean letras(espacios,números y otros)
        s=s.lower()
        # s=s[::-1]
        while len(s)%4!=0:
            s+='a'
        return s

    def block_convertv2(self,s,n,b=4): #Cada bloque se compone de 4 letras
        s=self.preprocess_stringv3(s)
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
        all_options=[]
        for arr_option in arr:
            dec_option=[]
            for option in arr_option:
                dec_num=[]
                cond=True
                while cond:
                    dec_num.append(option%26)
                    if option//26==0:
                        cond=False
                    option//=26
                dec_option.append(dec_num)
            dec_option=dec_option[::-1]
            final_string=[]
            for char in dec_option:
                s=''
                for n in char:
                    s+=(chr(n+97))
                final_string.append(s)
            all_options.append(final_string)
        return all_options[::-1]


    def encrypt(self,m):
        m=self.block_convertv2(m,self.n)
        m_encrypt=[(m_*(m_+self.B))%self.n for m_ in m]
        return m_encrypt


    def extended_gcd(self,a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def inverse_mod(self,a,n):
        return self.extended_gcd(a,n)[1]

    def decrypt(self,m_encrypt):
        solutions=[]
        _,a,b = self.extended_gcd(self.p,self.q)
        for c in m_encrypt:
            m_p = pow(c+(pow(self.B,2,self.n)*self.inverse_mod(4,self.n)),(self.p+1)//4,self.p)
            m_q = pow(c+(pow(self.B,2,self.n)*self.inverse_mod(4,self.n)),(self.q+1)//4,self.q)
            b_2=(-self.inverse_mod(2,self.n)*self.B)%self.n #-B/2
            r1 = (a*self.p*m_q+b*self.q*m_p)%self.n
            r2 = self.n-r1
            r3 = (a*self.p*m_q-b*self.q*m_p)%self.n
            r4 = self.n-r3
            r1=(r1+b_2)%self.n
            r2=(r2+b_2)%self.n
            r3=(r3+b_2)%self.n
            r4=(r4+b_2)%self.n
            solutions.append((r1,r2,r3,r4))
        return solutions[::-1]

# rab=ClassRabin()
# rab.gen_key()
# print('p= {}   q= {}  B= {}   n= {}'.format(rab.p,rab.q,rab.B,rab.n))
# m='This is a larger proof'
# print('Texto: {}'.format(m))
# print('Texto en bloque: {}'.format(rab.block_convertv2(m,rab.n)))
# s=rab.encrypt(m)
# print('Texto encriptado: {}'.format(s))
# print('Texto desencriptado: {}'.format(rab.decrypt(s))) 
# print('Texto desencriptado totalmente: {}'.format(rab.num_to_text(rab.decrypt(s))))