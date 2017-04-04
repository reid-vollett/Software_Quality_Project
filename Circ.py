from Shape import shape

class circ(shape):
    def __init__(this, size=10):
        '''initializes a circ object, not used very often because pygame handles rendering circle outlines very poorly'''
        shape.__init__(this)
        this.scale = size

    def draw(this, cam, maincam):
        '''adds the circ object to the camera's draw query'''
        maincam.toDraw(this)