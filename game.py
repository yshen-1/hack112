from __future__ import print_function,division
from visual import *
from Target import Target
import math

def generateMissile():
    missileSpawnLength = 20
    #make random cylindrical coordinate.
    r = 1
    z = random.uniform(-1.0, 1.0)
    theta = random.uniform(0.0, 2*math.pi)
    #convert to cartesian
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    z = z

    missileStartPos = vector(x,y,z)
    return (x,y,z)
    pass
def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)
def testGenerateMissile():
    (x,y,z) = generateMissile()
    assert(almostEqual(x**2+y**2+z**2, 1))
    print("generate missile passed!")

testGenerateMissile()

class missileObject(object):
    def __init__(self,launchLocation,velocity,blastYield,blastRadius=0):
        self.radius=0.1
        self.color=color.red
        self.blastRadius=blastRadius
        self.blastYield=blastYield
        self.velocity=velocity
        self.launchLocation=launchLocation
        self.location=launchLocation
    def spawnMissiles(self):
        pass
    def explode(self):
        pass
    def checkCollision(self):
        pass
    def timerFired(self):
        pass
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
        self.target.draw()
        self.missileList = []
        self.gameOver=False
    def run(self):
        while not self.gameOver:
            key=self.gameScene.kb.getkey()
            if key=='esc':
                print("Game over")
                self.gameOver=True

        exit()
missileCommand=game()
missileCommand.run()