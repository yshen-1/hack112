from __future__ import print_function,division
from visual import *
import math,random

class targetLine(object):
    def __init__(self,initRadius):
        print("init!")
        self.extrusionPath=paths.circle(pos=(0,0,0),radius=initRadius/2)
        self.line=shapes.line(start=(0,0),end=(initRadius,0))
        self.ext=extrusion(shape=self.line,color=color.green)

    def timerFired(self,newRadius,planeToDraw,upVector):
        print(newRadius)
        self.line=shapes.line(start=(0,0),end=(newRadius,0))
        self.ext.shape=self.line
        planeToDraw=rotate(norm(planeToDraw),angle=3*pi/2,axis=upVector)
        self.ext.up=planeToDraw

class ui(object):
    def __init__(self,lineLength):
        self.line=targetLine(lineLength)
    def timerFired(self,newLineLength,planeToDraw,upVector):
        self.line.timerFired(newLineLength,planeToDraw,upVector)



