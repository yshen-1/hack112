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
                               background=self.background,x=800,y=450)

        self.radarScene.select()
        # adds lights to scene
        self.radarScene.lights = (distant_light(direction = ( 0, 1,  0), color = color.gray(.4)),
                                  distant_light(direction = ( 0, 1, -1), color = color.gray(.2)),
                                  distant_light(direction = ( 0, 1,  1), color = color.gray(.2)),
                                  distant_light(direction = (-1, 1,  0), color = color.gray(.2)),
                                  distant_light(direction = ( 1, 1,  0), color = color.gray(.2)),)
        # sets default perspective
        self.radarScene.forward = vector(0, -1, -3)
        self.radarScene.userZoom = False
        self.radarScene.userSpin = False
        #draws the cylinder for radar
        cylinder(pos=(0,0,0), axis=(0,-2,0),
                 radius=15, color = (.18, .49, .196))
        #draws the rods for navigation
        green = (.114, .914, .714)
        blue = (0, .69, 100)
        yellow = (1, 1, 0)
        orange = (1, .439, .263)
        cylinder(pos=(0,-.85,0),axis=(14.5,0,0),radius=1, color = green)
        cylinder(pos=(0,-.85,0),axis=(0,0,14.5),radius=1, color = yellow)
        cylinder(pos=(0,-.85,0),axis=(-14.5,0,0),radius=1, color = blue)
        cylinder(pos=(0,-.85,0),axis=(0,0,-14.5),radius=1, color = orange)

        #gets the intial camera view
        self.camRadius = 20
        self.camTheta = 0
        camX = math.sin(self.camTheta) * self.camRadius
        camZ = math.cos(self.camTheta) * self.camRadius
        self.radarScene.forward = vector(camX, -10, camZ)

        #for the test code
        self.gameOver = False

    def updateMis(self, target, missleList):
        #updates and draws missles
        self.radarScene.select()
        (targetX, targetY, targetZ) = target.position
        maxSpawnDistance = 15
        for missle in missleList:
            
            (miX,miY,miZ) = missle.pos
            
            modelX = (miX - targetX) * (1/maxSpawnDistance) * 15
            modelY = (miY - targetY) * (1/maxSpawnDistance) * 15
            
            sphere(pos=(modelX,modelY,0), radius = 3, color = color.red)

    def updateCam(self,dCamTheta):
        self.camTheta += dCamTheta
        camX = math.sin(self.camTheta) * self.camRadius
        camZ = math.cos(self.camTheta) * self.camRadius
        self.radarScene.forward = vector(camX, -10, camZ)

    def test(self):
        while not self.gameOver:
            if self.radarScene.kb.keys!=0:
                key=self.radarScene.kb.getkey()
                if key=='esc':
                    print("Game over")
                    self.gameOver=True
                elif key == "right":
                    
                    self.camTheta += .2
                elif key == "left":
                    
                    self.camTheta -= .2

            camX = math.sin(self.camTheta) * self.camRadius
            camZ = math.cos(self.camTheta) * self.camRadius
            self.radarScene.forward = vector(camX, -10, camZ)

            rate(100)
        exit()

