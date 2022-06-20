import cv2
import numpy as np
#import cv

class ImageEncrypt:

    def __init__(self):
        self.K = [0, 0, 0]
        self.W = [255, 255, 255]
        self.R = [255, 0, 0]
        self.G = [0, 255, 0]
        self.B = [0, 0, 255]
        self.Y = [255, 255, 0]
        self.M = [255, 0, 255]
        self.C = [0, 255, 255]


    def mat16(self,c):
        if c == self.K:
          temp = np.array([[self.K,self.C,self.K,self.W,self.K,self.W,self.K,self.Y,self.K,self.Y,self.K,self.W,self.M,self.Y,self.M,self.C],[self.W,self.K,self.C,self.K,self.Y,self.K,self.W,self.K,self.Y,self.K,self.W,self.K,self.C,self.M,self.Y,self.M]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==self.W:
          temp = np.array([[self.W,self.W,self.W,self.M,self.M,self.Y,self.Y,self.Y,self.C,self.C,self.K,self.K,self.K,self.K,self.K,self.K],[self.W,self.W,self.W,self.M,self.M,self.Y,self.Y,self.Y,self.C,self.C,self.K,self.K,self.K,self.K,self.K,self.K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==self.R:
          temp = np.array([[self.Y,self.M,self.Y,self.M,self.Y,self.W,self.K,self.C,self.K,self.C,self.K,self.W,self.K,self.W,self.K,self.K],[self.M,self.Y,self.M,self.Y,self.W,self.K,self.C,self.K,self.C,self.K,self.W,self.K,self.W,self.K,self.Y,self.K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==self.G:
          temp = np.array([[self.Y,self.C,self.Y,self.C,self.Y,self.W,self.K,self.M,self.K,self.M,self.K,self.W,self.K,self.W,self.K,self.K],[self.C,self.Y,self.C,self.Y,self.Y,self.K,self.M,self.K,self.M,self.K,self.W,self.K,self.W,self.K,self.W,self.K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==self.B:
          temp = np.array([[self.M,self.C,self.M,self.C,self.W,self.Y,self.K,self.Y,self.K,self.Y,self.K,self.W,self.K,self.W,self.K,self.K],[self.C,self.M,self.C,self.M,self.Y,self.K,self.Y,self.K,self.Y,self.K,self.W,self.K,self.W,self.K,self.W,self.K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==self.Y:
          temp = np.array([[self.Y,self.W,self.Y,self.W,self.Y,self.W,self.K,self.C,self.K,self.C,self.K,self.M,self.K,self.M,self.K,self.K],[self.W,self.Y,self.W,self.Y,self.W,self.Y,self.C,self.K,self.C,self.K,self.M,self.K,self.M,self.K,self.K,self.K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==self.M:
          temp = np.array([[self.M,self.W,self.M,self.W,self.W,self.Y,self.K,self.Y,self.K,self.Y,self.C,self.K,self.C,self.K,self.K,self.K],[self.W,self.M,self.W,self.M,self.W,self.K,self.Y,self.K,self.Y,self.K,self.K,self.C,self.K,self.C,self.K,self.Y]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==self.C:
          temp = np.array([[self.C,self.W,self.C,self.W,self.W,self.Y,self.K,self.Y,self.K,self.Y,self.K,self.M,self.K,self.M,self.K,self.K],[self.W,self.C,self.W,self.C,self.W,self.K,self.Y,self.K,self.Y,self.K,self.M,self.K,self.M,self.K,self.Y,self.K]])
          return temp[:, np.random.permutation(temp.shape[1])]

    def tone_remover(self,pixel):
        r, g, b = pixel
        if abs(255 - r) <= abs(r):
            r = 255
        else:
            r = 0
        if abs(255 - g) <= abs(g):
            g = 255
        else:
            g = 0
        if abs(255 - b) <= abs(b):
            b = 255
        else:
            b = 0
        return r, g, b

    def setcolors(self, pic):
        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]):
                pic[i][j] = self.tone_remover(pic[i][j])

    def encoder(self, pe):
        p = cv2.imread(pe)
        self.setcolors(p)
        im1 = np.zeros((p.shape[0] * 4, p.shape[1] * 4, 3), np.uint8)
        im2 = np.zeros((p.shape[0] * 4, p.shape[1] * 4, 3), np.uint8)
        for x in range(p.shape[0]):
            for y in range(p.shape[1]):
                m = self.mat16([p[x][y][0], p[x][y][1], p[x][y][2]])
                if m is None:
                    print(m, x,y, p[x][y][0], p[x][y][1], p[x][y][2])
                
                for i in range(4):
                    for j in range(4):
                        im1[4 * x + i][4 * y + j] = m[0][4 * i + j]
                        im2[4 * x + i][4 * y + j] = m[1][4 * i + j]
        return im1, im2


    def desencoder(self, im1, im2):
        p = cv2.imread(im1)
        q = cv2.imread(im2)
        n = len(p)
        m = len(p[0])
        result = np.zeros((p.shape[0], p.shape[1], 3), np.uint8)
        for i in range(n):
            for j in range(m):
                pixel = []
                for k in range(3):
                    pixel1 = p[i][j][k]
                    if(p[i][j][k]==q[i][j][k]):
                        pixel.append(p[i][j][k])
                    else:
                        pixel.append(0)
                result[i][j] = pixel
                pixel.clear()
        return result

