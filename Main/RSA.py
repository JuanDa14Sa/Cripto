import random
import math as m
import re

class ClassRSA :
    def __init__(self):
        self.p = 0
        self.q = 0
        #self.p = 61
        #self.q = 53
        self.n = 0
        self.e = 0
        self.d = 0
        self.kPublica = ()
        self.kPrivada = ()

    def primesInRange(self):
        prime_list = []
        for n in range(100, 1000):
            isPrime = True

            for num in range(2, n):
                if n % num == 0:
                    isPrime = False
            if isPrime:
                prime_list.append(n)
        randomPrime = random.choice(prime_list)
        return randomPrime

    def generarKey (self):
        self.p = self.primesInRange()
        self.q = self.primesInRange()
        self.n = self.q * self.p
        fn = (self.p-1)*(self.q-1)
        while True:
            x = random.randint(self.n//2, self.n)
            if m.gcd(fn, x) == 1:
                self.e = x
                break
        self.d = pow(self.e, -1, fn)
        self.kPublica = (self.n, self.e)
        self.kPrivada = (self.n, self.d)

    def encriptar(self,s):
        n, e = self.kPublica
        en = s**e
        result = en % n
        return result

    def desencriptar(self,c):
        n, d = self.kPrivada
        des = (c ** d) % n
        return des

    def preprocess_stringv2(self,s):
        s=re.sub('[^a-zA-Z]',"",s)       #Elimina todo lo que no sean letras(espacios,números y otros)
        s=s.lower()
        while len(s)%3!=0:
            s+='a'
        return s

    def partition(self,s,b=3):
        s=self.preprocess_stringv2(s)
        k=len(s)//b
        parts = [s[i*3:(i+1)*3] for i in range(0, k)]
        return parts

    def block_convert(self,s):
        n=self.n
        b=self.partition(s)
        num_arr=[]
        for bi in b:
            l=len(bi)
            num=0
            for i in range(l):
                num+=(ord(bi[l-i-1])-97)*26**i
            num_arr.append(num%n)
        return num_arr

    def num_to_text(self, arr):
        all_options = []
        for option in arr:
            dec_option = []
            dec_num = []
            cond = True
            while cond:
                dec_num.append(option % 26)
                if option // 26 == 0:
                    cond = False
                option //= 26
            dec_option.append(dec_num)
            final_string = []
            for char in dec_option:
                s = ''
                for n in char:
                    s += (chr(n + 97))
                final_string.append(s)
            all_options.append(final_string)
        return all_options[::-1]