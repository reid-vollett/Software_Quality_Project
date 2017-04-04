import pygame

import GlobalVariables
from Circ import circ
from Img import img
from Poly import poly
from Shape import shape
from ezmath import *


# cameras are used to render world objects from a dynamic point of view
class camera:
    def __init__(this):
        '''initiales a camera object'''

        this.drawQuery = list()
        this.pos = (0, 0)
        this.angle = 0

    def orient(this, pos, angle):
        '''orients the camera to the specified settings'''
        this.pos = addPoints(pos, (GlobalVariables.size[0] / -2, GlobalVariables.size[1] / -2))
        this.pos = pos
        this.angle = angle

    def center(this):
        '''returns the coordinates of the center of the camera'''
        return addPoints(this.pos, (GlobalVariables.size[0] / -2, GlobalVariables.size[1] / -2))

    def getViewPoint(this, worldpoint):
        '''takes a point in the world and returns the position it will show up on screen'''
        av = worldpoint
        av = transform(av, multPoint(this.pos, -1), 0)
        av = transform(av, (0, 0), -this.angle)
        av = addPoints(av, multPoint(GlobalVariables.size, .5))
        return av

    def render(this):
        '''transforms the shapes in it's drawQuery to it's orientation and then renders them to the screen'''
        for dshape in this.drawQuery:
            if (type(dshape) is poly):
                this.renderPoly(dshape)
            if (type(dshape) is circ):
                this.renderCirc(dshape)
            if (type(dshape) is img):
                this.renderImg(dshape)
        # renews the draw query so it does not redraw the items from the previous frame
        this.drawQuery = list()

    def renderImg(this, dimg):
        '''renders an img object'''
        rect = dimg.surface.get_rect()
        rect.center = this.getViewPoint(dimg.pos)
        GlobalVariables.screen.blit(dimg.surface, rect)

    def renderPoly(this, dpoly):
        '''renders a poly object'''
        absverts = list()
        for vert in dpoly.getAbsVerts():
            # transforms the poly's vertices to the correct screen coordinates
            # for rendering purposes, we must first translate the vertex and then rotate it
            av = vert
            av = transform(av, multPoint(this.pos, -1), 0)
            av = transform(av, (0, 0), -this.angle)
            av = addPoints(av, multPoint(GlobalVariables.size, .5))
            absverts.append(av)
        if (dpoly.fill != None):
            # fills a polygon if it has a specified fill color
            pygame.draw.polygon(GlobalVariables.screen, dpoly.fill, absverts, 0)
        pygame.draw.polygon(GlobalVariables.screen, dpoly.color, absverts, dpoly.thickness)

    def renderCirc(this, dcirc):
        '''renders a circ object'''
        pygame.draw.circle(GlobalVariables.screen, dcirc.color, roundPoint(this.getViewPoint(dcirc.pos)), round(dcirc.scale),
                           dcirc.thickness)

    def toDraw(this, dshape):
        '''adds a shape to the draw query if it is a shape object'''
        if (not baseIs(dshape, shape)):
            return  # returns if it is not a shape type
        this.drawQuery.append(dshape)