
class Object:
        def __init__(self,high,width,start,k,c):
            self.high=high
            self.width=width
            self.start=start.data[0]
            self.end=start.data[0]+width
            self.k=k
            self.c=c
        def getup(self):
            up=self.start[1]+self.high/2
            return up
