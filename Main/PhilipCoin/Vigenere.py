from collections import Counter
import numpy as np

class CripVigenere:

    def __init__(self, data, key):
        self.data = data.replace(" ", "")
        self.key = key
        self.max = 20

    def encriptar(self):
        if not self.data.isalpha():
            return "Unacceptable input"
        word_ascii = np.array([ord(c) for c in self.data.lower()])
        for i in range(len(self.key)):
            pos = i
            while pos < len(self.data):
                word_ascii[pos] = (((word_ascii[pos] - 97) + (ord(self.key.lower()[i]) - 97)) % 26) + 97
                pos += len(self.key)
        encryption = [chr(c) for c in word_ascii]
        return ''.join(encryption).lower()

    def desencriptar(self):
        word_ascii = np.array([ord(c) for c in self.data.lower()])
        for i in range(len(self.key)):
            pos = i
            while pos < len(self.data):
                word_ascii[pos] = (((word_ascii[pos] - 97) - (ord(self.key.lower()[i]) - 97)) % 26) + 97
                pos += len(self.key)
        encryption = [chr(c) for c in word_ascii]
        return ''.join(encryption)

    def changeMax(self, m):
        self.max = m

    def ic(self, x):
        if len(x) == 1 or len(x) == 0:
            return 0
        freq = Counter(x)
        sum = 0
        for i in freq:
            sum += freq[i] * (freq[i] - 1)
        return sum / (len(x) * (len(x) - 1))

    def ic_average(self, x, i):
        wordsAv = []
        for j in range(i):
            wordsAv.append(self.ic(x[j::i]))
        return np.mean(wordsAv)

    def mg(self, word, n):
        indices = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                   0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                   0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                   0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
        freq = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            freq[c] = 0
        temp = Counter(''.join(word.lower()))
        for a in temp:
            freq[a] += temp[a]
        m = []
        for g in range(26):
            sum = 0
            for i in range(26):
                sum += indices[i] * freq[chr(((i + g) % 26) + 97)]
            m.append((g, abs(0.0667 - (sum / n))))
        return chr((sorted(m, key=lambda x: x[1])[0][0]) + 97)

    def criptanalisis(self):
        average = []
        for i in range(self.max):
            average.append((i + 1, abs(0.0667 - self.ic_average(self.data, i + 1))))
        possibles_ordered = sorted(average, key=lambda x: x[1])
        return [i[0] for i in possibles_ordered]

    def criptanalisis_key(self,m):
        possible_key = ''
        for i in range(m):
            y = self.data.lower()[i::m]
            possible_key += self.mg(y, len(self.data) / m)
        self.key = possible_key
        return possible_key


