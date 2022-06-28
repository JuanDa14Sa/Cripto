import hashlib
import re
from Vigenere import ClassVigenere

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.solution = self.problem_maker()
        self.vige = ClassVigenere()
        self.problem = self.vige.encrypt(self.solution)
        self.previous_hash = previous_hash
        self.hash
    def hash_block(self):   # Calcula el hash del bloque
        hasher = hashlib.sha256()
        sha = hasher.sha256()
        sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        return sha.hexdigest()
    def problem_maker(self):
        paragraph = '''YOU don't know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain't no matter.  That book was made by Mr. Mark Twain, and he told the truth, mainly.  There was things which he stretched, but mainly he told the truth.  That is nothing.  I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary.  Aunt Polly—Tom's Aunt Polly, she is—and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.
                    Now the way that the book winds up is this:  Tom and me found the money that the robbers hid in the cave, and it made us rich.  We got six thousand dollars apiece—all gold.  It was an awful sight of money when it was piled up.  Well, Judge Thatcher he took it and put it out at interest, and it fetched us a dollar a day apiece all the year round—more than a body could tell what to do with.  The Widow Douglas she took me for her son, and allowed she would sivilize me; but it was rough living in the house all the time, considering how dismal regular and decent the widow was in all her ways; and so when I couldn't stand it no longer I lit out.  I got into my old rags and my sugar-hogshead again, and was free and satisfied.  But Tom Sawyer he hunted me up and said he was going to start a band of robbers, and I might join if I would go back to the widow and be respectable.  So I went back.
                    The widow she cried over me, and called me a poor lost lamb, and she called me a lot of other names, too, but she never meant no harm by it. She put me in them new clothes again, and I couldn't do nothing but sweat and sweat, and feel all cramped up.  Well, then, the old thing commenced again.  The widow rung a bell for supper, and you had to come to time. When you got to the table you couldn't go right to eating, but you had to wait for the widow to tuck down her head and grumble a little over the victuals, though there warn't really anything the matter with them,—that is, nothing only everything was cooked by itself.  In a barrel of odds and ends it is different; things get mixed up, and the juice kind of swaps around, and the things go better.
                    After supper she got out her book and learned me about Moses and the Bulrushers, and I was in a sweat to find out all about him; but by and by she let it out that Moses had been dead a considerable long time; so then I didn't care no more about him, because I don't take no stock in dead people.'''
        res = re.sub(r'[^a-zA-Z]', '', paragraph)
        paragraphs = [res[x:x+10] for x in range(0, len(res)-10, 10)]
    def test_problem(self, sol):
        if self.solution == sol:
            self.hash = self.hash_block()
            return True
        else:
            return False
    
