from Shape import Shape
import pygame
import random

class Square(Shape):
    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Square', maxWidth, maxHeight)
        self.side = random.randint(10, 100)

    def clickedInside(self, mousePoint):
        # Check if the mouse point is inside the square
        return self.left <= mousePoint[0] <= self.left + self.side and self.top <= mousePoint[1] <= self.top + self.side

    def getArea(self):
        return self.side ** 2

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.left, self.top, self.side, self.side))
