from __future__ import print_function,division
from visual import *
from Target import Target
from missileObject import missileObject
import math,random

'''
explosionList = []
def dist(x1,y1,x2,y2,z1,z2):
    return sqrt((x1-x2)**2 + (y1-y2)**2+(z1-z2))
def checkCollision(missileX,missileY,missileZ):
    for explosion in explosionList:
        (explosionX,explosionY,explosionZ explosionRadius) = explosion
        if(dist(missileX,missileY,explosionX,explosionY) < explosionRadius):
            return True
    return False
'''

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
        self.missileList = []
        self.explosionList=[]
        self.gameOver=False

    def generateMissile(blastRadius=0):
        #Generate a random spawn location and velocity
        missileSpawnLength = 6
        missileSpeed = 0.5
        missileError = 0.1
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
        blastYield=0.2
        return missileObject(missileSpawnLocation, missileVelocity,
                             blastYield,blastRadius=0)

    def timerFired(self):
        if random.randint(0,100)<1:
            self.missileList.append(self.generateMissile())
            if self.gameScene.autoscale:
                self.gameScene.autoscale=False
        for missile in self.missileList:
            result=missile.timerFired(self.deltaT,self.target.radius)
            if result!=None:
                self.explosionList.append(result)
        for explosion in self.explosionList:
            explosion.timerFired()
        self.missileList=[self.missileList[i] for i in
                          range(len(self.missileList))
                          if not self.missileList[i].destroyed]
        self.explosionList=[self.explosionList[i] for i in
                            range(len(self.explosionList))
                            if not self.explosionList[i].over]
    def run(self):
        while not self.gameOver:
            if self.gameScene.kb.keys!=0:
                key=self.gameScene.kb.getkey()
                if key=='esc':
                    print("Game over")
                    self.gameOver=True
            self.timerFired()
            rate(100)
        exit()
missileCommand=game()
missileCommand.run()