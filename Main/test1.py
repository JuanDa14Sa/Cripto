from PhilipCoin.Vigenere import CripVigenere
import re

text=open('Main/VigenereText.txt','r').read()    # Lee el texto del archivo      


res = re.sub(r'[^a-zA-Z]', '', text)
res=res.lower()

num_sub=300
paragraphs = [res[x:x+num_sub] for x in range(0, len(res)-num_sub, num_sub)]
print(len(paragraphs))
# print(paragraphs)
# print(len(paragraphs))
vig=CripVigenere(paragraphs[0],'people')
vig2=CripVigenere(vig.encriptar(),'people')



for i in vig2.criptanalisis():
    print(vig2.criptanalisis_key(i))