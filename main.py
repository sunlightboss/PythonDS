import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Initialize Pygame and set up OpenGL context
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Define the triangle vertices and colors
vertices = [
    (0, 1, 0),   # Top
    (-1, -1, 0), # Bottom-left
    (1, -1, 0)   # Bottom-right
]
colors = [
    (1, 0, 0), # Red
    (0, 1, 0), # Green
    (0, 0, 1)  # Blue
]

def draw_triangle():
    glBegin(GL_TRIANGLES)
    for i, vertex in enumerate(vertices):
        glColor3fv(colors[i])
        glVertex3fv(vertex)
    glEnd()

# Main animation loop
clock = pygame.time.Clock()
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Rotate the triangle
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)  # Rotate around Z-axis
    draw_triangle()
    glPopMatrix()

    # Update angle for rotation
    angle += 1
    if angle > 360:
        angle -= 360

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Cleanup
pygame.quit()