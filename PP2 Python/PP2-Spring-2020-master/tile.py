import pygame


class Tile:
    size = 100
    highlight = (255, 215, 0)
    thickness = 10

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.active = True

    def draw(self, screen, x, y):
        if self.active:
            pygame.draw.rect(screen, self.color, (self.size * self.x, self.size * self.y,
                                                  self.size, self.size))
        if self.x == x and self.y == y:
            pygame.draw.rect(screen, self.highlight, (self.size * self.x, self.size * self.y,
                                                      self.thickness, self.size))
            pygame.draw.rect(screen, self.highlight, (self.size * self.x, self.size * self.y,
                                                      self.size, self.thickness))
            pygame.draw.rect(screen, self.highlight, (self.size * (self.x + 1) - self.thickness, self.size * self.y,
                                                      self.thickness, self.size))
            pygame.draw.rect(screen, self.highlight, (self.size * self.x, self.size * (self.y + 1) - self.thickness,
                                                      self.size, self.thickness))
