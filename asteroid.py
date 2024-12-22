import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255), #white
            self.position, #center
            self.radius,
            2 #line width
        )
    
    def update(self, dt):
        self.position += self.velocity * dt