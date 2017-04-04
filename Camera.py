import pygame
from ezmath import *

from Poly import poly
from Circ import circ
from Img import img
from Shape import shape

class camera:
    def __init__(this):
        '''initiales a camera object'''
        this.drawQuery = list()
        this.pos = (0, 0)
        this.angle = 0

    def orient(this, pos, angle, size):
        '''orients the camera to the specified settings'''
        this.pos = addPoints(pos, (size[0] / -2, size[1] / -2))
        this.pos = pos
        this.angle = angle

    def center(this, size):
        '''returns the coordinates of the center of the camera'''
        return addPoints(this.pos, (size[0] / -2, size[1] / -2))

    def getViewPoint(this, worldpoint, size):
        '''takes a point in the world and returns the position it will show up on screen'''
        av = worldpoint
        av = transform(av, multPoint(this.pos, -1), 0)
        av = transform(av, (0, 0), -this.angle)
        av = addPoints(av, multPoint(size, .5))
        return av

    def render(this, size, screen):
        '''transforms the shapes in it's drawQuery to it's orientation and then renders them to the screen'''
        for dshape in this.drawQuery:
            if (type(dshape) is poly):
                this.renderPoly(dshape, size, screen)
            if (type(dshape) is circ):
                this.renderCirc(dshape)
            if (type(dshape) is img):
                this.renderImg(dshape)
        # renews the draw query so it does not redraw the items from the previous frame
        this.drawQuery = list()

    def renderImg(this, dimg, screen):
        '''renders an img object'''
        rect = dimg.surface.get_rect()
        rect.center = this.getViewPoint(dimg.pos)
        screen.blit(dimg.surface, rect)

    def renderPoly(this, dpoly, size, screen):
        '''renders a poly object'''
        absverts = list()
        for vert in dpoly.getAbsVerts():
            # transforms the poly's vertices to the correct screen coordinates
            # for rendering purposes, we must first translate the vertex and then rotate it
            av = vert
            av = transform(av, multPoint(this.pos, -1), 0)
            av = transform(av, (0, 0), -this.angle)
            av = addPoints(av, multPoint(size, .5))
            absverts.append(av)
        if (dpoly.fill != None):
            # fills a polygon if it has a specified fill color
            pygame.draw.polygon(screen, dpoly.fill, absverts, 0)
        pygame.draw.polygon(screen, dpoly.color, absverts, dpoly.thickness)

    def renderCirc(this, dcirc, screen):
        '''renders a circ object'''
        pygame.draw.circle(screen, dcirc.color, roundPoint(this.getViewPoint(dcirc.pos)), round(dcirc.scale),
                           dcirc.thickness)

    def toDraw(this, dshape):
        '''adds a shape to the draw query if it is a shape object'''
        if (not baseIs(dshape, shape)):
            return  # returns if it is not a shape type
        this.drawQuery.append(dshape)