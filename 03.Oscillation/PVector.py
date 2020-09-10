import math 
import random as rnd

class PVector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def set(self, v):
        self.x = v.x
        self.y = v.y
        self.z = v.z
        return self

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def sub(self, v1, v2=None, target=None):
        if v2 == None:
            v2 = PVector(0,0,0)

        if target == None:
            target = PVector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
        else:
            target.set(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
        return target

    def mult(self, n):
        self.x *= n
        self.y *= n
        self.z *= n
    
    def div(self, n, v=None, target=None):
        if v == None:
            v = PVector(0,0,0)

        if target == None:
            target = PVector(v.x/n, v.y/n, v.z/n)
        else:
            target.set(v.x/n, v.y/n, v.z/n)
        
        return target
        
    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def magSq(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z)

    def setMag(self, len):
        self.normalize()
        self.mult(len)
        return self
        
    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)

    def limit(self, max):
        if self.magSq() > max * max:
            self.normalize()
            self.mult(max)
    
    def fromAngle(self, angle, target=None):
        if target == None:
            target = PVector(math.cos(angle), math.sin(angle),0)
        else:
            target.set(math.cos(angle), math.sin(angle),0)
        return target
    
    def random2D(self, target=None, parent=None):
        if parent == None:
            return self.fromAngle(rnd.random() * math.pi * 2, target)
        else:
            #return fromAngle(parent.random(PConstants.TAU), target);
            return self.fromAngle(rnd.random() * math.pi * 2, target)

    def copy(self):
        return PVector(self.x, self.y, self.z)

    def get(self, target = None):
        if target == None:
            return PVector(self.x, self.y, self.z)
        
        if len(target) >= 2:
            target[0] = self.x
            target[1] = self.y

        if len(target) >= 3:
            target[2] = self.z

        return target

    def heading(self):
        angle = math.atan2(self.y, self.x)
        return angle

    def heading2D(self):
        return self.heading()