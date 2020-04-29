import random
from tile import Tile
from palette import Palette


class Field:

    def __init__(self):
        palette = Palette.shuffle() # palette is the list of 36 colors
        self.field = [] # field is the 2-dimensional list that store all tiles, 
        				# e.g field[i][j] is the tile in ith row and jth column
        self.x = random.randint(0, 5) # x coordinate of the tile you are standing now
        self.y = random.randint(0, 5) # y coordinate of the tile you are standing now
        

    def draw(self, screen):

    	# write code to draw full field

    def move(self, direction):
        
        # write code to move yourself




