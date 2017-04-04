import GlobalVariables
from Enemy import enemy
from Particle import particle
from Poly import poly
from gameFunctions import *


class asteroid(enemy):
    def __init__(this, pos, radius):
        '''initializes an asteroid object'''
        enemy.__init__(this, pos)
        this.radius = radius
        this.health = this.radius / 10 + 1
        this.form = poly.circleGon(7, radius)

    def kill(this):
        '''destroys the asteroid object'''
        enemy.kill(this)
        global score
        if (this.radius > 10):
            GlobalVariables.sounds[8].play()
            # splits into 3 smaller pieces
            for i in range(3):
                p = randPoint(1)
                a1 = asteroid(addPoints(this.pos, multPoint(p, this.radius)), this.radius / 2)
                a1.vel = multPoint(p, 2)
                GlobalVariables.enemies.append(a1)
        else:
            GlobalVariables.sounds[9].play()
        for i in range(3 + int(this.radius / 5)):
            # emits particles of death
            part = particle(addPoints(this.pos, randPoint(this.radius)), 0, (200, 120, 90), 4)
            if (randChance(50)):
                part.color = (130, 100, 50)
            part.vel = multPoint(subtractPoints(part.pos, this.pos), 0.3)
            part.life = random.randrange(50, 75)
            GlobalVariables.particles.append(part)
        getPoints(math.ceil(this.radius / 20) * 10)  # worth more points the bigger the asteroid

    def itemDrop(this):
        '''only has a chance to drop an item if is large enough'''
        if (this.radius > 10):
            enemy.itemDrop(this)

    def draw(this):
        '''renders the current asteroid instance'''
        this.form.pos = this.pos
        this.form.fill = (75, 50, 25)
        this.form.thickness = 2
        this.form.color = (150, 100, 50)
        GlobalVariables.maincam.toDraw(this.form)