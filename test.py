from __future__ import division, print_function
from visual import *

width=500
height=500
sceneCenter=(0,0,0)
background=(0,0,0)
gameScene=display(title="3D missile command",width=width,
                       height=height,center=sceneCenter,
                       background=background)
gameScene.select()
radar = cylinder(pos=(0,0,0), axis=(0, -2, 0), radius=15)
rod = cylinder(pos=(0,-.75,0), axis=(14, 0, 0), radius = 1)
gameScene.forward = vector(0, -1, -3)
