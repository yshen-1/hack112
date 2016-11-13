from __future__ import print_function,division
from visual import *
from Target import Target
import math



class Target(object):
    def __init__(self, x, y, z, radius):
        self.position = vector(x, y, z)
        self.radius = radius

    def checkCollision(missile):
        missilePos = missile.position
        collisionRadius = self.radius + missile.radius
        distance = (misslePos-self.position).mag
        return distance < collisionRadius

    def draw(self):
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

    def generateMissile(velocity=3, blastYield=2, blastRadius=0):
        missileSpawnLength = 20
        # make random unit vector in cylindrical coordinate.
        r = 1
        z = random.uniform(-1.0, 1.0)
        theta = random.uniform(0.0, 2 * math.pi)
        # convert to cartesian
        x = math.sqrt(1 - z ** 2) * math.cos(theta)
        y = math.sqrt(1 - z ** 2) * math.sin(theta)
        z = z
        # Add magnitude to the unit vector:
        x *= missileSpawnLength
        y *= missileSpawnLength
        z *= missileSpawnLength
        missileSpawnLocation = vector(x, y, z)
        return missile(missileSpawnLocation, velocity, blastYield,
                       blastRadius=0)

    def timerFired(self):
        for i in range(len(self.missileList:
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