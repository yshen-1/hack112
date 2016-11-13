from __future__ import division, print_function
from visual import *
#bouncing ball
ball = sphere(pos=(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
ball.velocity=vector(25,0,0)
deltat=0.005
t=0
while t<3:
    ball.pos=ball.pos+ball.velocity*deltat
    if ball.pos.x>wallR.pos.x or ball.pos.x<-10:
        ball.velocity*=-1
    t+=deltat
    rate(100)