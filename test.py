from __future__ import division, print_function
from visual import *
scene.range = 5 # fixed size, no autoscaling
ball = sphere(pos=(-3,0,0), color=color.cyan)
cube = box(pos=(+3,0,0), size=(2,2,2), color=color.red)
drag_pos = None # no object picked yet

def grab(evt):
    global drag_pos
    if evt.pick == ball:
        drag_pos = evt.pickpos
        scene.bind('mousemove', move, ball)
        scene.bind('mouseup', drop)

def move(evt, obj):
    global drag_pos
    # project onto xy plane, even if scene rotated:
    new_pos = scene.mouse.project(normal=(0,0,1))
    if new_pos != drag_pos: # if mouse has moved
        # offset for where the ball was touched:
        obj.pos += new_pos - drag_pos
        drag_pos = new_pos # update drag position

def drop(evt):
    scene.unbind('mousemove', move)
    scene.unbind('mouseup', drop)

scene.bind('mousedown', grab)