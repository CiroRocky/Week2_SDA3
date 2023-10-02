from Shape import Shape
import pygame
import random

class Triangle(Shape):
    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Triangle', maxWidth, maxHeight)
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)

    def clickedInside(self, mousePoint):
        # Check if the mouse point is inside the triangle using barycentric coordinates
        def isInside(point, v1, v2, v3):
            def sign(p1, p2, p3):
                return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

            b1 = sign(point, (self.left, self.top), (self.left + self.width, self.top + self.height))
            b2 = sign(point, (self.left, self.top + self.height), (self.left + self.width, self.top))
            b3 = sign(point, (self.left, self.top), (self.left, self.top + self.height))

            return (b1 >= 0) and (b2 >= 0) and (b3 >= 0) or (b1 <= 0) and (b2 <= 0) and (b3 <= 0)

        return isInside(mousePoint, (self.left, self.top), (self.left + self.width, self.top), (self.left, self.top + self.height))

    def getArea(self):
        return 0.5 * self.width * self.height

    def draw(self):
        pygame.draw.polygon(self.window, self.color,
                            [(self.left, self.top),
                             (self.left + self.width, self.top),
                             (self.left, self.top + self.height)])
