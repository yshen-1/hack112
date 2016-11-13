from __future__ import print_function,division
from visual import *
from Target import Target
from Radar import Radar
from missileObject import missileObject
import math,random,time


class game(object):
    def __init__(self):
        #generates window
        self.deltaT=0.05
        self.width=800
        self.height=800
        self.sceneCenter=(0,0,0)
        self.background=(0,0,0)
        self.gameScene=display(title="3D missile command",width=self.width,
                               height=self.height,center=self.sceneCenter,
                               background=self.background)
        self.gameScene.select()

        #creating earth
        self.target = Target(0,0,0,1)

        #camera operations
        self.gameScene.lights = (distant_light(direction = ( 1, 0,  0), color = color.gray(.4)),
                                 distant_light(direction = (-1, 0,  0), color = color.gray(.5)),
                                 distant_light(direction = ( 0, 0,  1), color = color.gray(.6)),
                                 distant_light(direction = ( 0, 0, -1), color = color.gray(.7)),
                                 )
        self.gameScene.userzoom = False
        self.gameScene.userspin = False
        self.gameScene.range = ((5,5,5))

        self.camTheta = math.pi

        self.camRadius = 10

        #game variables
        self.missileList = []
        self.explosionList=[]
        self.gameOver=False
        self.dx = .1
        self.dy = -.1

        #creating radar
        self.radar = Radar()

        self.gameScene.select()


    def generateMissile(blastRadius=0):
        #To Do, make generate missiles send missiles to the launch points
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
        blastYield=0.3
        return missileObject(missileSpawnLocation, missileVelocity,
                             blastYield,blastRadius=0)
    @staticmethod
    def dist(x1,y1,z1,x2,y2,z2):
        return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    def generateCounterMissile(self,mouseInput, target):
        missileSpeed = 1
        #Get location of the launch sites
        time0=time.time()
        launchSiteList = target.findTargetLaunchPoints()
        time1=time.time()
        print("Target find time:",time1-time0)
        #See which launch site is closest to mouse input
        shortestDist = None
        closestLaunchSite = None
        for launchSite in launchSiteList:
            dist = game.dist(mouseInput.x,mouseInput.y,mouseInput.z,launchSite.x,launchSite.y,launchSite.z)
            if(shortestDist == None or dist < shortestDist):
                shortestDist = dist
                closestLaunchSite = launchSite
        time2=time.time()
        print("Launch site find time:",time2-time1)
        #Get Missile Velocity
        counterMissileVelocity = norm(mouseInput - launchSite) #Subtract the vectors
        counterMissileVelocity.mag = missileSpeed
        blastYield=0.3
        return missileObject(closestLaunchSite, counterMissileVelocity,
                             blastYield,blastRadius=0,target=mouseInput,
                             counter=True)

    def timerFired(self):
        #missle operations
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

        #camera ops
        camX = math.sin(self.camTheta) * self.camRadius
        camZ = math.cos(self.camTheta) * self.camRadius
        self.gameScene.forward = vector(camX, 0, camZ)

    def run(self):
        self.gameScene.select()
        while not self.gameOver:
            #mouse events
            if self.gameScene.mouse.events!=0:
                print("Click!")
                event=self.gameScene.mouse.getevent()
                if (event.release!=None):
                    location=event.pos
                    self.missileList.append(self.generateCounterMissile
                                            (location,self.target))

            if self.gameScene.kb.keys!=0:

                key=self.gameScene.kb.getkey()
                if key=='esc':
                    print("Game over")
                    self.gameOver=True
                elif key == "right":
                    self.camTheta -= .2
                    self.radar.updateCam(-.2)
                    self.gameScene.select()
                elif key == "left":
                    self.camTheta += .2
                    self.radar.updateCam(.2)
                    self.gameScene.select()

            
            #timer fired
            self.timerFired()

            rate(100)
        exit()
missileCommand=game()
missileCommand.run()