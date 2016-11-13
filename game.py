from __future__ import print_function,division
from visual import *
from Target import Target

import math,random


explosionList = []
def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
def checkCollision(missileX,missileY):
    for explosion in explosionList:
        (explosionX,explosionY, explosionRadius) = explosion
        if(dist(missileX,missileY,explosionX,explosionY) < explosionRadius):
            return True
    return False

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
        self.destroyed=True
        (locationX,locationY,locationZ) = self.missileBody.pos
        explosionList += (locationX,locationY,locationZ,self.blastRadius)
        
        explosion=sphere(pos=self.missileBody.pos,
                         radius=self.blastRadius,color=color.green)
        del self.missileBody

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
        self.target = Target(0,0,0,1)
        self.targetSphere=self.target.draw()
        self.missileList = []
        self.gameOver=False

    def generateMissile(blastYield=2, blastRadius=0):
        #Generate a random spawn location and velocity
        missileSpawnLength = 5
        missileSpeed = 0.1
        missileError = 0.05
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
        #Add some random error to the missileVelocity
        xVel += random.uniform(-missileError,missileError)
        yVel += random.uniform(-missileError,missileError)
        zVel += random.uniform(-missileError,missileError)
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
        return missileObject(missileSpawnLocation, missileVelocity,
                             blastYield,blastRadius=0)

    def timerFired(self):
        print("Timer fired!")
        if random.randint(0,10)<3:
            self.missileList.append(self.generateMissile())
            print("Missile spawned!")
        for missile in self.missileList:
            missile.timerFired(self.deltaT)
        self.missileList=[self.missileList[i] for i in
                          range(len(self.missileList))
                          if not self.missileList[i].destroyed]


    def run(self):
        while not self.gameOver:
            key=self.gameScene.kb.getkey()
            if key=='esc':
                print("Game over")
                self.gameOver=True
            self.timerFired()
            rate(100)
            #self.drawAll()
        exit()
missileCommand=game()
missileCommand.run()