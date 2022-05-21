

import math
import random

from Crypto.Util.number import getPrime
from Crypto.Hash import SHA256

class DigitalSignatureGammal:
    def __init__(self):
        self.p=0
        self.alpha=0
        self.private_a=0
        self.y=0

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
        self.alpha=random.randint(1,self.p-1)
        self.private_a=random.randint(1,self.p-2)
        self.y=pow(self.alpha,self.private_a,self.p)
    
    def hash_message(self,message):
        sha=SHA256.new()
        sha.update(message.encode('utf-8'))
        return int(sha.hexdigest(),16)
    
    def signature(self,message):
        k=random.randint(1,self.p-2)
        gcd=self.extended_gcd(k,self.p-1)
        while gcd[0]!=1:
            k=random.randint(1,self.p-2)
            gcd=self.extended_gcd(k,self.p-1)
        r=pow(self.alpha,k,self.p)
        k_inverse=gcd[1]
        s=(k_inverse*(self.hash_message(message)-self.private_a*r))%(self.p-1)
        return r,s

    def verify(self,message,r,s):
        if not(1<=r and r<=self.p-1):
            return 'La firma no es válida'
        else:
            v1=(pow(self.y,r,self.p)*pow(r,s,self.p))%self.p
            sha=SHA256.new()
            sha.update(message.encode('utf-8'))
            hm=int(sha.hexdigest(),16)
            v2=pow(self.alpha,hm,self.p)
            return 'Firma correcta' if v1==v2 else 'Firma incorrecta'


# sig=DigitalSignatureGammal()
# sig.gen_key()
# print('Clave pública: \n p:  {}  \n  alpha:  {}   \n  y:  {}'.format(sig.p,sig.alpha,sig.y))
#
# document=open(r"Main\document.txt",'r')
# message=document.read()
# document.close()
# r,s=sig.signature(message)
# print('Firma del mensaje \n  r:  {}  \n  s:  {}'.format(r,s))
# print('Verificación de la firma: {}'.format(sig.verify(message+' dehniuwdui.',r,s)))
# print('Verificación de la firma: {}'.format(sig.verify(message,r,s)))