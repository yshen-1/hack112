from __future__ import print_function,division
from visual import *
class missileObject(object):
    def __init__(self):
        pass
    def explode(self):
        pass
    def checkCollision(self):
        pass
class game(object):
    def __init__(self):
        self.width=500
        self.height=500
        self.sceneCenter=(0,0,0)
        self.background=(0,0,0)
        self.gameScene=display(title="3D missile command",width=self.width,
                               height=self.height,center=self.sceneCenter,
                               background=self.background)
        self.gameScene.select()
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