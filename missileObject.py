from __future__ import print_function,division
from visual import *
import math,random

class explosion(object):
    def __init__(self,location,blastRadius,blastYield):
        self.over=False
        self.color=color.yellow
        self.location=location
        self.blastRadius=blastRadius
        self.blastYield=blastYield
        self.explosion=sphere(pos=self.location,
                              radius=self.blastRadius+0.001,color=self.color)
    def timerFired(self):
        self.explosion.radius+=0.01
        if (self.explosion.radius>self.blastYield):
            self.over=True
            self.explosion.visible=False
            del self.explosion
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
                                radius=self.radius,color=self.color, make_trail = True)
        self.missileBody.trail_object.color=color.orange
    def spawnMissiles(self):
        pass
    def timerFired(self,deltaT,targetRadius):
        self.missileBody.pos+=self.velocity*deltaT
        if mag(vector(self.missileBody.pos))<targetRadius:
            print("Explosion!")
            self.destroyed=True
            missileLocation=self.missileBody.pos
            blastRadius=0
            blastYield=self.blastYield
            self.missileBody.visible=False
            self.missileBody.trail_object.visible=False
            del self.missileBody.trail_object
            del self.missileBody
            del self.missileBody.trail_object
            return explosion(missileLocation,blastRadius,blastYield)

