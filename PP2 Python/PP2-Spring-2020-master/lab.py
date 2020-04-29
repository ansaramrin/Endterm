import pygame
import sys
import random
from pygame.locals import *

running = True

class Tilemap:
    tilemap = []
    ht = None # ht = highlight texture

    def __init__(self, height, width, tilesize, textures):
        self.height = height # How many tiles high it is
        self.width = width # How many tiles wide it is
        self.tilesize = tilesize # How many pixels each tile is
        self.textures = textures # The textures
        self.size = (self.width*self.tilesize,self.height*self.tilesize)

    def generate_random(self):
        # Generate a random tilemap
        self.tilemap = [[random.randint(0, len(
            self.textures)-1) for e in range(self.width)] for e in range(
                self.height)]

    def draw(self, display, mouse=None):
        mouse = mouse
        # Draw the map
        for row in range(self.width):
            for column in range(self.height):



                texture = self.textures[self.tilemap[row][column]]
                # Highlight a tile (this is where the problem is)
                if self.ht != None:
                    if mouse[0] >= (column*self.tilesize) and mouse[0] <= (
                        column*self.tilesize)+self.tilesize:
                        if mouse[1] >= (row*self.tilesize) and mouse[1] <= (
                            row*self.tilesize)+self.tilesize:
                            texture = self.ht

                display.blit(texture,
                             (column*self.tilesize, row*self.tilesize))




tilemap = Tilemap(10,10,40,
                  # Load the textures
                  {0: pygame.image.load("tile1.png"),
                   1: pygame.image.load("tile2.png")
                   }
                  )

tilemap.generate_random() # Generate a random tilemap

pygame.init()
DISPLAYSURF = pygame.display.set_mode((tilemap.size))
# Load the highlighter
tilemap.ht = pygame.image.load("highlight.png").convert_alpha()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Draw the tilemap
        tilemap.draw(DISPLAYSURF, pygame.mouse.get_pos())

    pygame.display.update()
