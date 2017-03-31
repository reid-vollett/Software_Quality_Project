
from gameFunctions import *

import enemy
import poly
import motherCowDeath
import alien
import enemyBullet

class motherCow(enemy):
    def __init__(this, pos):
        enemy.__init__(this, pos)
        this.buildForm()
        this.radius = 45
        this.health = 25
        this.angle = 0
        this.spawnwait = 60
        this.vel = randCirc(1)
        if (randChance(50)):
            this.rot = -.01
        else:
            this.rot = .01

    def buildForm(this):
        this.form = poly()
        verts = [ \
            (20, 0), (19, 1), (18, 1), (16, 3), (16, 5), (17, 6), (17, 7), (16, 7), (15, 6), (13, 6), (11, 8), (11, 9),
            (10, 10), (9, 9), (9, 8), (7, 6), (5, 6), (4, 7), (3, 7), (3, 6), (4, 5), (4, 3), (2, 1), (1, 1), (0, 0), \
            (1, -1), (2, -1), (4, -3), (4, -5), (3, -6), (3, -7), (4, -7), (5, -6), (7, -6), (9, -8), (9, -9),
            (10, -10), (11, -9), (11, -8), (13, -6), (15, -6), (16, -7), (17, -7), (17, -6), (16, -5), (16, -3),
            (18, -1), (19, -1) \
            ]
        for vert in verts:
            this.form.verts.append(subtractPoints(vert, (10, 0)))

    def kill(this, sounds, particles):
        enemy.kill(this)
        sounds[11].play()
        getPoints(750)
        body = motherCowDeath(this.pos, this.vel)
        particles.append(body)

    def update(this, sounds, enemies, projectiles):
        enemy.update(this)
        this.angle += this.rot
        this.spawnwait -= 1
        if (this.spawnwait <= 0):
            sounds[16].play()
            this.spawnwait = 120
            al = alien(this.pos)
            enemies.append(al)
            for i in range(8):
                ang = math.pi * 2 * (i / 8) + this.angle
                pos = multPoint(xyComponent(ang), this.radius)
                pos = addPoints(this.pos, pos)
                proj = enemyBullet(pos, ang, 4)
                projectiles.append(proj)

    def draw(this, maincam):
        this.form.angle = this.angle
        this.form.pos = this.pos
        this.form.color = (255, 150, 0)
        this.form.thickness = 2
        this.form.fill = (50, 20, 0)
        this.form.scale = 5
        maincam.toDraw(this.form)
