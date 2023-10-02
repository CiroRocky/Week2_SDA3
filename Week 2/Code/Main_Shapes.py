import pygame
from Circle import Circle
from Triangle import Triangle
from Square import Square
import random

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
N_SHAPES = 10

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shapes Example")

# Create shapes
shapesList = []
for _ in range(N_SHAPES):
    shape_type = random.choice(['Circle', 'Triangle', 'Square'])
    if shape_type == 'Circle':
        shape = Circle(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    elif shape_type == 'Triangle':
        shape = Triangle(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    else:
        shape = Square(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    shapesList.append(shape)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for shape in shapesList:
                if shape.clickedInside(mouse_pos):
                    print(f"Clicked on {shape.getType()} with area {shape.getArea()}")

    # Draw shapes and update display
    window.fill(WHITE)
    for shape in shapesList:
        shape.draw()
    pygame.display.flip()

# Quit pygame
pygame.quit()
