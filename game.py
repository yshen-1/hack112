from __future__ import print_function,division
from visual import *
from Target import Target
import math
import random


class Target(object):
    def __init__(self, x, y, z, radius):
        #initilaizatoin for target
        self.position = vector(x, y, z)
        self.radius = radius

    def checkCollision(missile):
        #checks if missle hits target
        missilePos = missile.position
        collisionRadius = self.radius + missile.radius
        distance = (misslePos-self.position).mag
        return distance < collisionRadius

    def draw(self):
        #draws sphere
        return sphere(pos=tuple(self.position), radius=self.radius,
               material=materials.earth)


class missileObject(object):
    def __init__(self,launchLocation,velocity,blastYield,blastRadius=0):
        self.radius=0.1
        self.color=color.red
        self.blastRadius=blastRadius
        self.blastYield=blastYield
        self.velocity=velocity
        self.launchLocation=launchLocation
        self.location=launchLocation
        self.missileBody=sphere(pos=tuple(launchLocation),
                                radius=self.radius,color=self.color)
    def spawnMissiles(self):
        pass
    def explode(self):
        explosion=sphere(pos=tuple(self.location),
                         radius=self.blastRadius,color=color.red)
        while self.blastRadius<self.blastYield:
            self.blastRadius+=0.01
            explosion.radius=self.blastRadius
        del explosion
    def timerFired(self,deltaT):
        self.location=self.location+self.velocity*deltaT

class game(object):
    def __init__(self):
        self.deltaT=0.05
        self.width=500
        self.height=500
        self.sceneCenter=(0,0,0)
        self.background=(0,0,0)
        self.gameScene=display(title="3D missile command",width=self.width,
                               height=self.height,center=self.sceneCenter,
                               background=self.background)
        self.gameScene.select()
        self.target = Target(0,0,0,2)
        self.targetSphere=self.target.draw()
        self.missileList = []
        self.gameOver=False

    def generateMissile(blastYield=2, blastRadius=0):
        #Generate a random spawn location and velocity
        missileSpawnLength = 20
        missileSpeed = 3
        # make random unit vector in cylindrical coordinate.
        r = 1
        z = random.uniform(-1.0, 1.0)
        theta = random.uniform(0.0, 2 * math.pi)
        # convert to cartesian
        xPos = math.sqrt(1 - z ** 2) * math.cos(theta)
        yPos = math.sqrt(1 - z ** 2) * math.sin(theta)
        zPos = z
        #Generate the missileVelocity (invert the position vector)
        xVel = -xPos
        yVel = -yPos
        zVel = -zPos
        #Add magnitude to the velocity unit vector
        xVel *= missileSpeed
        yVel *= missileSpeed
        zVel *= missileSpeed
        missileVelocity = vector(xVel, yVel, zVel)

        #Add magnitude to the position unit vector:
        xPos *= missileSpawnLength
        yPos *= missileSpawnLength
        zPos *= missileSpawnLength
        missileSpawnLocation = vector(xPos, yPos, zPos)
        return missile(missileSpawnLocation, missileVelocity, blastYield,blastRadius=0)

    def timerFired(self):
        for i in range(len(self.missileList)):
            if missile.timerFired():

    def run(self):
        while not self.gameOver:
            key=self.gameScene.kb.getkey()
            if key=='esc':
                print("Game over")
                self.gameOver=True
            self.timerFired()
            #self.drawAll()
        exit()
missileCommand=game()
missileCommand.run()