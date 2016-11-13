3D Missile Command
Classes:

targetObject:
    attributes:
        vpython sphere
        sphere launch positions
    methods:
        checkCollision (for missile collisions)

missileObject:
    attributes:
        launchPoint (point where missile is launched from)
        blastRadius
        velocity
    methods:
        checkCollision (for missile explosions triggering other missiles)
        explode() (explodes missile, generates animation, runs collision checks)