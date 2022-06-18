import math
import random

from Crypto.Util.number import getPrime
from Crypto.Hash import SHA256

class DigitalSignatureRSA:
    def __init__(self):
        self.p=0
        self.q=0
        self.n=0
        self.e=0
        self.private_d=0

    def extended_gcd(self,a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def inverse_mod(self,a,n):
        return self.extended_gcd(a,n)[1]

    def gen_key(self):
        self.p=getPrime(512)
        self.q=getPrime(512)
        self.n=self.p*self.q
        phi=(self.p-1)*(self.q-1)
        e=random.randint(2,phi-1)
        gcd=self.extended_gcd(e,phi)
        while gcd[0]!=1:
            e=random.randint(2,phi-1)
            gcd=self.extended_gcd(e,phi)
        self.e=e
        self.private_d=gcd[1]%phi
        print('Clave pública: \n n:  {}  \n  e:  {}'.format(self.n,self.e))
    

    def hash_message(self,message):
        sha=SHA256.new()
        sha.update(message.encode('utf-8'))
        return int(sha.hexdigest(),16)
    
    def signature(self,message):
        m_=self.hash_message(message)
        s=pow(m_,self.private_d,self.n)
        return s

    def check_redundancy(self,m_): ##Verificar si m_ está en el rango de la función de redundancia
        return True

    def verify(self,s,message):
        h=self.hash_message(message)
        h_=pow(s,self.e,self.n)
        return 'Firma correcta' if h==h_ else 'Firma incorrecta'
        
    # def redundancy_function(self,message):
    #     return int(message.encode('ASCII').hex(),16)%self.n ##Implementar una buena función de redundancia

    # def inverse_redundancy(self,m_):
    #     return m_.to_bytes((m_.bit_length()+7)//7, 'big').decode('ASCII') ##Depende de la implementación de la función de redundancia


# sig=DigitalSignatureRSA()
# sig.gen_key()
# print('Clave pública: \n n:  {}  \n  e:  {}'.format(sig.n,sig.e))
#
# document=open(r"Main\document.txt",'r')
# message=document.read()
# document.close()
#
# s=sig.signature(message)
# print('Firma: ',s)
# print('Verificación: ',sig.verify(s,message))
# print('Verificación: ',sig.verify(s,message+'dfa.')) #Prueba de firma incorrecta