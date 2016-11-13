3D Missile Command
Classes:

targetObject: (earth)
    attributes:
        vpython sphere
        sphere launch positions (domes on the target, center of each octant of earth)
    methods:
        checkCollision (for missile collisions)
	draw (earth and dome)

missileObject:
    attributes:
        launchPoint (point where missile is launched from)
        blastRadius
        velocity
    methods:
        checkCollision (for missile explosions triggering other missiles)
        explode() (explodes missile, generates animation, runs collision checks)