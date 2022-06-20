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
        K =[0,0,0]
        W =[255,255,255]
        R =[255,0,0]
        G =[0,255,0]
        B =[0,0,255]
        Y =[255,255,0]
        M =[255,0,255]
        C =[0,255,255]
        if c==K:
          temp = np.array([[K,C,K,W,K,W,K,Y,K,Y,K,W,M,Y,M,C],[W,K,C,K,Y,K,W,K,Y,K,W,K,C,M,Y,M]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==W:
          temp = np.array([[W,W,W,M,M,Y,Y,Y,C,C,K,K,K,K,K,K],[W,W,W,M,M,Y,Y,Y,C,C,K,K,K,K,K,K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==R:
          temp = np.array([[Y,M,Y,M,Y,W,K,C,K,C,K,W,K,W,K,K],[M,Y,M,Y,W,K,C,K,C,K,W,K,W,K,Y,K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==G:
          temp = np.array([[Y,C,Y,C,Y,W,K,M,K,M,K,W,K,W,K,K],[C,Y,C,Y,Y,K,M,K,M,K,W,K,W,K,W,K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==B:
          temp = np.array([[M,C,M,C,W,Y,K,Y,K,Y,K,W,K,W,K,K],[C,M,C,M,Y,K,Y,K,Y,K,W,K,W,K,W,K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==Y:
          temp = np.array([[Y,W,Y,W,Y,W,K,C,K,C,K,M,K,M,K,K],[W,Y,W,Y,W,Y,C,K,C,K,M,K,M,K,K,K]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==M:
          temp = np.array([[M,W,M,W,W,Y,K,Y,K,Y,C,K,C,K,K,K],[W,M,W,M,W,K,Y,K,Y,K,K,C,K,C,K,Y]])
          return temp[:, np.random.permutation(temp.shape[1])]
        if c==C:
          temp = np.array([[C,W,C,W,W,Y,K,Y,K,Y,K,M,K,M,K,K],[W,C,W,C,W,K,Y,K,Y,K,M,K,M,K,Y,K]])
          return temp[:, np.random.permutation(temp.shape[1])]
 
    def tone_remover(self,pixel):
        r,g,b=pixel
        if abs(255-r)<=abs(r):
            r=255
        else:
            r=0   
        if abs(255-g)<=abs(g):
            g=255
        else:
            g=0 
        if abs(255-b)<=abs(b):
            b=255
        else:
            b=0
        return r,g,b 

    def setcolors(self,pic):
        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]):
                pic[i][j]=self.tone_remover(pic[i][j])

    def encoder(self,pe):
        p = cv2.imread(pe)
        self.setcolors(p)
        im1 = np.zeros((p.shape[0]*4,p.shape[1]*4,3), np.uint8)
        im2 = np.zeros((p.shape[0]*4,p.shape[1]*4,3), np.uint8)
        for x in range(p.shape[0]):
            for y in range(p.shape[1]):
                m = self.mat16([p[x][y][0],p[x][y][1],p[x][y][2]])
                for i in range(4):
                    for j in range(4):
                        im1[4*x+i][4*y+j] = m[0][4*i+j]
                        im2[4*x+i][4*y+j] = m[1][4*i+j]
        return im1,im2

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

    def decoder(self, im1, im2):
        p = im1
        q = im2
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

