import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Orbiting Bodies")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Body class
class Body:
    def __init__(self, cx, cy, sma, smi, speed):
        self.cx, self.cy = cx, cy
        self.sma, self.smi = sma, smi
        self.speed = speed * 20
        self.angle = 15

    def update(self):
        self.angle = (self.angle + self.speed) % 360
        x = self.cx + self.sma * math.cos(math.radians(self.angle))
        y = self.cy + self.smi * math.sin(math.radians(self.angle))
        return x, y

# Create bodies
bodies = [Body(width / 2, height / 2, 50 + i * 25, 25 + i * 12.5, 0.1 - i * 0.015) for i in range(7)]

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(black)

    for body in bodies:
        x, y = body.update()
        pygame.draw.ellipse(window, white, (x, y, 6, 6))
    
    pygame.draw.ellipse(window, white, (bodies[0].cx, bodies[0].cy, 10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
