from Shape import shape

class img(shape):
    def __init__(this, surface):
        '''initializes an img instance, an image type shape that can be rendered in the world'''
        shape.__init__(this)
        this.surface = surface