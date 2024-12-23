import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle  = random.uniform(20, 50)
            vect_1 = self.velocity.rotate(random_angle)
            vect_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            aster_1 = Asteroid(self.position.x, self.position.y, new_radius)
            aster_2 = Asteroid(self.position.x, self.position.y, new_radius)
            aster_1.velocity = vect_1 * 1.2
            aster_2.velocity = vect_2 * 1.2