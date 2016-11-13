from __future__ import print_function,division
from visual import *
import math

class Target(object):
    def __init__(self, x, y, z, radius):
        #initializes target
        self.position = vector(x, y, z)
        self.radius = radius
        self.launchPoints = self.findTargetLaunchPoints()
        #draws earth
        self.draw()

    def findTargetLaunchPoints(self):
        # gets the target points (8 evenly distributed points)
        points = []
        for theta in [0, math.pi/2, math.pi, math.pi*3/2]:
            for phi in [.9553, 2.186]:
                x = math.sin(phi)*math.sin(theta)*self.radius
                y = math.cos(phi)*self.radius
                z = math.sin(phi)*math.cos(theta)*self.radius
                points += [vector(x, y, z)]
        return points
  
    def checkCollision(missile):
        #checks if missle collides with earth
        missilePos = missile.position
        collisionRadius = self.radius + missile.radius
        distance = (misslePos-self.position).mag
        return distance < collisionRadius

    def draw(self):
        #draws target or earth
        sphere(pos=tuple(self.position), radius=self.radius,
               material=materials.earth)
        green = (.114, .914, .714)
        blue = (0, .69, 100)
        yellow = (1, 1, 0)
        orange = (1, .439, .263)
        colors = [orange, blue, yellow, green]
        #puts the launch points silos
        for p in range(len(self.launchPoints)):
            point = self.launchPoints[p]
            c = colors[p//2]
            print(c, point)
            cone(pos = tuple(point), radius = self.radius/10, 
                 axis = tuple(point/10), color = c)