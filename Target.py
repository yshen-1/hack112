from __future__ import print_function,division
from visual import *

#earth
class Target(object):
    def __init__(self, x, y, z, radius):
        #initialization for target
        self.position = vector(x, y, z)
        self.radius = radius

    def checkCollision(missile):
        #checks if missle hits target
        missilePos = missile.position
        collisionRadius = self.radius + missile.radius
        distance = (misslePos-self.position).mag
        return distance < collisionRadius

    def draw(self):
        #draws target
        sphere(pos=tuple(self.position), radius=self.radius, 
               material=materials.earth)
