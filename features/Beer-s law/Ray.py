
class Ray:
    def __init__(self,start,width,p,I0,object):
        self.width=width
        self.start=start.data
        self.I0=I0
        self.I0=I0
        self.object = object
        self.b = p.data[0] - object.start
    def getstrength(self):
        if self.p.data[0] < self.object.start:
            self.I= self.I0
        if self.object.start<self.p.data[0]<self.object.end:
           self.I=pow(10,-self.object.k*self.b*self.object.c)*self.I0
        if self.p.data[0] > self.object.end:
            self.I = pow(10, -self.object.k * self.object.width * self.object.c) * self.ray.strength

        return self.I
