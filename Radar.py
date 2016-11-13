from __future__ import print_function,division
from visual import *

class Radar(object):
    def __init__(self):
        #generates a new window for radar
        self.width=300
        self.height=300
        self.sceneCenter=(0,0,0)
        self.background=(0,0,0)

        self.radarScene=display(title="Radar",width=self.width,
                               height=self.height,center=self.sceneCenter,
                               background=self.background)

        self.radarScene.select()
        self.radarScene.forward = vector(0, -1, -3)
        self.radarScene.userZoom = False
        self.radarScene.userSpin = False
        #draws the cylinder for radar
        cylinder(pos=(0,0,0), axis=(0,-2,0),
                 radius=15, color = (0,1,.5))
        self.camRadius = 20
        self.camTheta = 0
        cylinder(pos=(0,-.75,0),axis=(14,0,0),radius=1)

    def update(self, target, missleList, cameraMove):
        #updates and draws missles
        self.radarScene.select()
        (targetX, targetY, targetZ) = target.position
        maxSpawnDistance = 15
        for missle in missleList:
            
            (miX,miY,miZ) = missle.pos
            
            modelX = (miX - targetX) * (1/maxSpawnDistance) * 15
            modelY = (miY - targetY) * (1/maxSpawnDistance) * 15
            
            sphere(pos=(modelX,modelY,0), radius = 3, color = color.red)

    # def test(self):
    #     pass
        # while True:
        #     if self.radarScene.kb.keys!=0:
        #         key=self.radarScene.kb.getkey()
        #         if key=='esc':
        #             print("Game over")
        #             self.gameOver=True
        #         elif key == "right":
        #             print('1')
        #             self.camTheta += .2
        #         elif key == "left":
        #             print('1')
        #             self.camTheta -= .2

        #     camX = math.sin(self.camTheta) * self.camRadius
        #     camZ = math.cos(self.camTheta) * self.camRadius
        #     self.radarScene.forward = vector(camX, -1, camZ)

r = Radar()
# r.test()


