from __future__ import print_function,division
from visual import *

class game(object):
    def __init__(self):
        self.gameScene=display(title="3D missile command",
                           width=500,height=500,background=(0,0,0))
        self.gameOver=False
        self.ball = sphere(pos=(-5, 0, 0), radius=0.5, color=color.cyan)
    def run(self):
        self.gameScene.select()
        self.ball=self.ball
        while not self.gameOver:
            key=self.gameScene.kb.getkey()
            if key=='up':
                print("Game over")
                self.gameOver=True
        exit()
missileCommand=game()
missileCommand.run()