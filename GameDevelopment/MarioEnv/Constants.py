import os

#GAME CONSTANTS
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 800
HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
RATIO = SCREEN_HEIGHT/240
BACKGROUND_WIDTH, BACKGROUND_HEIGHT = int(3400*RATIO), int(240*RATIO)
TILE_SIZE = int(16*RATIO)
MARGIN = 5
PATH = os.getcwd()
PATH = os.path.join(PATH, PATH + '\Images')

#CHARACTER CONSTANTS
STARTING_POSITION = (5*TILE_SIZE, SCREEN_HEIGHT - 3*TILE_SIZE)
VELOCITY = 1
Y_VELOCITY = 5
GRAVITY = 0.05
LIMIT = 100
PEACH_POS = (0, 0) #TBD

#BOWSER CONSTANTS
BOWSER_POSITION = (10*TILE_SIZE, SCREEN_HEIGHT - 4*TILE_SIZE)
ACTION_RADIUS = 7*TILE_SIZE
BOWSER_VEL = 0.5
BOWSER_THRUST = 0.5
FLAME_SPEED = 0.5
FLAME_DISTANCE = 15*TILE_SIZE

#SPRITE CONSTANTS
PIPES_POSITION = [(6, 20*TILE_SIZE, SCREEN_HEIGHT - 6*TILE_SIZE)] #[[size, pos_x, pos_y]]
CLOUD_POSITIONS = []
GROUND_POSITIONS = [(x, y) for y in range(BACKGROUND_HEIGHT - 2*TILE_SIZE, BACKGROUND_HEIGHT, TILE_SIZE) for x in range(0, BACKGROUND_WIDTH, TILE_SIZE)]
BRICK_POSITIONS=[]
BRICK_POSITIONS = [(pos[0]*TILE_SIZE, pos[1]*TILE_SIZE) for pos in BRICK_POSITIONS]
STAIRS_POSITION = []
COIN_POSITIONS = [(25*TILE_SIZE, SCREEN_HEIGHT - 6*TILE_SIZE)]
GOOMBA_SPEED = 1
SKELLY_SPEED = 1
GOOMBAS_POSITION = [(15*TILE_SIZE, SCREEN_HEIGHT - 3*TILE_SIZE)]
