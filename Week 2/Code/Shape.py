from abc import ABC, abstractmethod
import random

class Shape(ABC):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self, window, shapeType, maxWidth, maxHeight):
        self.window = window
        self.shapeType = shapeType
        self.color = random.choice([self.RED, self.GREEN, self.BLUE])
        self.left = random.randint(1, maxWidth - 100)
        self.top = random.randint(25, maxHeight - 100)

    @abstractmethod
    def clickedInside(self, mousePoint):
        raise NotImplementedError

    @abstractmethod
    def getArea(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

    def getType(self):
        return self.shapeType
