import pygame

size = (600, 600)
screen = None
# the titlescreen image, is only loaded when in use due to it's relatively large memory consumption
titlesprite = None

# delay between frames in seconds
framerate = 0.01666667
# catches the time lost in lag and later uses it to catch up if it accumulates too much
lagcatch = 0

# fonts
font = None
tinyfont = None

# menu mode and selection, defines GUI
mode = 0  # 0 = main, 1 = in game, 2 = name entry, 3 = scoreboard
selection = 0

# the main camera object - used to transform the world view
maincam = None
p1 = None
enemyspawndelay = 0
cowspawndelay = 0
score = 0
scoredrop = 500
scoredropper = None
hi = 0
iteration = 0

# collision groups for optomization
colcheck0 = list()
colcheck1 = list()
colcheck2 = list()
# entity lists
enemies = list()
projectiles = list()
items = list()
particles = list()
stars = list()
# data lists
powersprites = list()
sounds = list()

# used for handling input
lastkeyspr = None  # used when for name entry, shows which keys were pressed last frame, so not to repeat keystrokes
activecontr = [False, False, False, False, False, False]  # controls being actively held down
lastactivec = [False, False, False, False, False,
               False]  # controls that were held down last frame, used for menu navigation

# default controls:
controls = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_c, pygame.K_SPACE]
