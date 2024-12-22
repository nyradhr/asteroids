import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255), #white
            (self.x, self.y), #center
            self.radius,
            2 #line width
        )
    
    def update(self, dt):
        self.position += self.velocity * dt