from __future__ import print_function,division
from visual import *
import math,random


class missileObject(object):
    def __init__(self,launchLocation,velocity,blastYield,blastRadius=0):
        self.destroyed=False
        self.radius=0.1
        self.color=color.red
        self.blastRadius=blastRadius
        self.blastYield=blastYield
        self.velocity=velocity
        self.launchLocation=launchLocation
        self.missileBody=sphere(pos=tuple(launchLocation),
                                radius=self.radius,color=self.color)
    def spawnMissiles(self):
        pass
    def explode(self):
        print("Explosion!")
        self.destroyed=True
        #(locationX,locationY,locationZ) = self.missileBody.pos
        #explosionList += (locationX,locationY,locationZ,self.blastRadius)
        explosion=sphere(pos=self.missileBody.pos,
                         radius=self.blastRadius+0.001,color=color.green)
        self.missileBody.visible=False
        del self.missileBody
        while self.blastRadius<self.blastYield:
            print("Exploding!")
            self.blastRadius+=0.01
            explosion.radius=self.blastRadius
            rate(100)
        explosion.visible = False
        del explosion
    def timerFired(self,deltaT,targetRadius):
        self.missileBody.pos+=self.velocity*deltaT
        if mag(vector(self.missileBody.pos))<targetRadius:
            self.explode()
