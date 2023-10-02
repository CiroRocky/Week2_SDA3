from Shape import Shape
import math
import random
import pygame

class Circle(Shape):
    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Circle', maxWidth, maxHeight)
        self.radius = random.randint(10, 50)
        self.centerX = self.left + self.radius
        self.centerY = self.top + self.radius

    def clickedInside(self, mousePoint):
        distance = math.sqrt((mousePoint[0] - self.centerX) ** 2 + (mousePoint[1] - self.centerY) ** 2)
        return distance <= self.radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.centerX, self.centerY), self.radius)
