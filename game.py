from __future__ import print_function,division
from visual import *
from Target import Target

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
        self.ball = sphere(pos=(0, 0, 0), radius=2, material=materials.earth)
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