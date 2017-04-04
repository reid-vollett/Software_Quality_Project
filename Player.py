from Particle import particle
from Poly import poly
from Weapon import weapon
from ezmath import *
from src import GlobalVariables


# the player object, what the user is controlling
class player:
    def __init__(this):
        '''initializes the player'''
        this.primaryWep = weapon()  # starts with the default weapon
        this.powerWep = None
        this.pos = (0, 0)
        this.vel = (0, 0)
        this.angle = math.pi / -2
        this.rotvel = 0
        this.radius = 10
        this.health = 1
        this.powerups = []

    def update(this):
        '''updates the player instance'''
        if (this.health == None):
            return
        if (this.health <= 0):
            this.kill()
        this.pos = addPoints(this.pos, this.vel)
        this.angle += this.rotvel
        this.control()
        this.wepCheck()
        this.applySpeedLimit()
        this.curWep().update()
        # this.collisionCheck()
        this.updatePowers()

    def updatePowers(this):
        for pow in this.powerups:
            pow.pUpdate()

    def drawPowers(this):
        for pow in this.powerups:
            pow.pDraw()

    def powerEvent(this, event, params=None):
        '''tells the player's powerups that an event has been triggered'''
        for pow in this.powerups:
            pow.doPower(event, params)

    def wepCheck(this):
        '''checks if the current weapon is out of ammo and switches back to the primary when necessary'''
        if (this.curWep().ammo <= 0):
            if (this.powerWep != None):
                this.powerWep = None
            else:
                this.curWep = weapon()

    def damage(this, dmg):
        '''damages the player a specified amount'''
        if (this.health == None):
            return
            GlobalVariables.sounds[17].play()
        this.health -= dmg

    def kill(this):
        '''kills the player'''
        global iteration
        this.vel = (0, 0)
        this.health = None  # a health of None is used to determine that the player has been dead for more than a frame, used so the dead player isn't constantly exploding
        for i in range(20):
            # shoots out green particles on death
            off = randPoint(10)
            part = particle(addPoints(this.pos, off), off, (0, 255, 0))
            part.thickness = 4
            part.life = random.randrange(40, 100)
            if (randChance(50)):
                # chance the the partcle will be a darker green
                part.color = (0, 150, 0)
            GlobalVariables.particles.append(part)
        iteration = 0  # resets the global iteration to act as a makeshift timer so the transition to the end game menu isn't instantaneous

    def applySpeedLimit(this):
        '''makes sure the player doesn't go faster than a certain amount as this can cause unforseen consequences'''
        this.rotvel *= 0.93
        if (distance(this.vel) > 5):
            this.vel = multPoint(this.vel, 0.97)

    def control(this):
        '''handles the player controls'''
        acceleration = 0.15  # speed of movement
        rotspd = 0.005  # speed of aiming
        if (GlobalVariables.activecontr[0]):  # up
            this.vel = addPoints(this.vel, multPoint(xyComponent(this.angle), acceleration))
            this.thrustParticle(math.pi)
        if (GlobalVariables.activecontr[1]):  # down
            this.vel = addPoints(this.vel, multPoint(xyComponent(this.angle), -1 * acceleration))
            thrang = 1
            if (randChance(50)):
                thrang *= -1
            this.thrustParticle(thrang)
        if (GlobalVariables.activecontr[2]):  # right
            this.rotvel += rotspd
        if (GlobalVariables.activecontr[3]):  # left
            this.rotvel -= rotspd
        if (GlobalVariables.activecontr[4]):  # fire
            this.fire()

    def thrustParticle(this, reldir):
        '''emits particles to show acceleration'''
        force = multPoint(xyComponent(this.angle + reldir), 0.7)
        part = particle(addPoints(this.pos, randPoint(5)), multPoint(force, 5), (255, 150, 0))
        part.vel = addPoints(part.vel, this.vel)
        part.life = random.randrange(5, 10)
        if (randChance(50)):
            part.color = (200, 200, 0)
        part.thickness = 3
        GlobalVariables.particles.append(part)

    def curWep(this):
        '''returns a power weapon if the player has one equipped, otherwise returns it's primary weapon'''
        if (this.powerWep == None):
            return this.primaryWep
        return this.powerWep

    def fire(this):
        '''triggers the currently equipped weapon'''
        wepfire = this.curWep()
        if (wepfire.trigger(this.pos, this.angle, this.vel)):
            this.powerEvent(1, wepfire)

    def draw(this):
        '''draws the player to the global cam query'''
        if (this.health == None):
            return
        this.drawPowers()
        this.curWep().draw()
        # outline
        pshape = poly()
        pshape.color = (0, 255, 0)
        pshape.verts = [(-10, 10), (-10, -10), (15, 0)]
        pshape.pos = this.pos
        pshape.angle = this.angle
        pshape.thickness = 2
        # fill
        fshape = poly()
        fshape.color = (0, 100, 0)
        fshape.verts = pshape.verts
        fshape.pos = pshape.pos
        fshape.angle = pshape.angle
        fshape.thickness = 0
        fshape.draw(GlobalVariables.maincam)
        pshape.draw(GlobalVariables.maincam)
