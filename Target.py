from __future__ import print_function,division
from visual import *
import math

class Target(object):
    def __init__(self, x, y, z, radius):
        self.position = vector(x, y, z)
        self.radius = radius
        self.launchPoints = self.findTargetLaunchPoints()
        self.draw()

    def findTargetLaunchPoints(self):
        points = []
        for theta in [0, math.pi/2, math.pi, math.pi*3/2]:
            for phi in [math.pi/4, math.pi*3/4]:
                x = math.sin(phi)*math.cos(theta)*self.radius
                y = math.sin(phi)*math.sin(theta)*self.radius
                z = math.cos(phi)*self.radius
                points += [vector(x, y, z)]
        return points
  
    def checkCollision(missile):
        missilePos = missile.position
        collisionRadius = self.radius + missile.radius
        distance = (misslePos-self.position).mag
        return distance < collisionRadius

    def draw(self):
        #draws target
        sphere(pos=tuple(self.position), radius=self.radius,
               material=materials.earth)
        colors = [color.red, color.blue, color.green, color.yellow]
        for p in range(len(self.launchPoints)):
            point = self.launchPoints[p]
            c = colors[p//2]
            print(c, point)
            sphere(pos = tuple(point), radius = self.radius/20, color = c)