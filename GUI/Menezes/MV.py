

def poly(x):
      val = x**3+4*x+6
      val = val % 71
      return val

class ClassMV:
    def __init__(self):
      self.alpha = 0
      self.beta = 0
      self.a = 0
      self.k = 0
      self.points = []
      for i in range(71):
          temp = poly(i)**35%71
          if temp == 1:
            val = poly(i)**18%71
            self.points.append((i,val))
            self.points.append((i,-val%71))
          self.points.append('inf')
    
    def poly(x):
      val = x**3+4*x+2
      val = val % 71
      return val
    
    def egcd(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self,a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
    
    def suma(self,x,y):
       if x == 'inf':
         return y
       if y == 'inf':
         return x
       if ((-x[1])%71 == y[1]) and (x[0]==y[0]):
         return 'inf'
       l=0
       x1=x[0]
       y1=x[1]
       x2=y[0]
       y2=y[1]
       if x == y:
         l = ((3*x1**2+4))*self.modinv(2*y1,71)
         #l = ((3*x[0]**2+9)%71)*pow(y[0], -1, 71)
         #l = l % 71
         z = (l**2-2*x1) % 71
         w = (l*(x1-z) -y1)  %71
         return (z,w)
       else:
         l = ((y2-y1)%71)*self.modinv((x2-x1)%71, 71)
         #l = ((y[1]-y[0])%71)*pow(x[1]-x[0],-1, 71)
         l = l % 71
         z = (l**2-x1-x2) % 71
         w = (l*(x1-z) -y1) % 71
         return (z,w)


    def mult(self,int, x):
      temp = x
      for i in range(int-1):
        temp = self.suma(x,temp)
      return temp
    
    def set_key(self,alpha,beta,a):
      self.alpha = alpha
      self.beta = beta
      self.a = a
    
    def cifrar(self,m,k):
      y0 = self.mult(k,self.alpha)
      temp = self.mult(k,self.beta)
      y1 = temp[0]*m[0] %71
      y2 = temp[1]*m[1] %71
      return (y0,y1,y2)

    def descifrar(self,y0,y1,y2):
      c = self.mult(self.a,y0)
      x = (self.modinv(c[0],71)*y1) % 71
      y = (self.modinv(c[1],71)*y2) % 71
      return (x,y)

''' test = ClassMV()
print(test.points[0])
print(test.points[0],test.suma(test.points[0],test.points[0]))
test.set_key((0,19),(59,17),8)
print(test.cifrar((10,7),8))
print(test.descifrar((59, 17), 68, 65)) '''
