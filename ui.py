from __future__ import print_function,division
from visual import *
import math,random

class targetRing(object):
    def __init__(self,initRadius):
        print("init!")
        self.ring=shapes.arc(radius=initRadius,angle1=0,angle2=2*pi)
        self.ext=extrusion(shape=self.ring,up=(0,0,1))
    def timerFired(self,newRadius):
        #print(newRadius)
        self.ring.radius=newRadius
        self.ext.shape=self.ring

class ui(object):
    def __init__(self,ringRadius):
        self.ring=targetRing(ringRadius)
    def timerFired(self,newRingRadius):
        self.ring.timerFired(newRingRadius)

