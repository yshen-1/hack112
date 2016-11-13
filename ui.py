from __future__ import print_function,division
from visual import *
import math,random

class targetRing(object):
    def __init__(self,initRadius):
        self.ring=shapes.arc(radius=initRadius,angle1=0,angle2=2*pi)
        extrusion(shape=self.ring)
    def timerFired(self,newRadius):
        self.ring.radius=newRadius

class ui(object):
    def __init__(self,ringRadius):
        self.ring=targetRing(ringRadius)