3D Missile Command
Classes:

targetObject:
    attributes:
        vpython sphere
        position
        radius
        sphere launch positions
    methods:
        checkCollision (for missile collisions)

missileObject:
    attributes:
        launchPoint (point where missile is launched from)
        blastRadius
        velocity
        position
        radius (physical radius of the sphere used to represent a missile's collision box)
    methods:
        checkCollision (for missile explosions triggering other missiles)
        explode() (explodes missile, generates animation, runs collision checks)
