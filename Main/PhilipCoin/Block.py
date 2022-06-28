from Crypto.Hash import SHA256
import re
from Transaction import Transaction
from Vigenere import CripVigenere
import random

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = [data]
        self.solution = None
        self.size = 3
        self.vige = None
        self.vige2 = None
        self.previous_hash = previous_hash
        self.hash=None
        self.problem_maker()   # Genera el problema

    def hash_block(self):   # Calcula el hash del bloque
        sha=SHA256.new()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

    def problem_maker(self):
        text=open('Main/PhilipCoin/VigenereText.txt','r').read() 
        res = re.sub(r'[^a-zA-Z]', '', text)
        res=res.lower()
        keys=open('Main/PhilipCoin/keys.txt','r').read()
        keys=keys[1:-2].replace('\'',"").split(',')
        keys=[k.strip() for k in keys]
        num_sub=300
        paragraphs = [res[x:x+num_sub] for x in range(0, len(res)-num_sub, num_sub)]
        to_decode=paragraphs[random.randint(0,len(paragraphs)-1)]
        self.solution=random.choice(keys)
        self.vige=CripVigenere(to_decode,self.solution)
        self.vige2=CripVigenere(self.vige.encriptar(),self.solution)

    def test_problem(self, sol):
        if self.solution == sol:
            self.hash = self.hash_block()
            return True
        else:
            return False

    def add_transaction(self, transaction):
        self.data.append(transaction)
    
