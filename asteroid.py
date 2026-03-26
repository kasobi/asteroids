import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        
        child_1_velocity = self.velocity.rotate(new_angle)
        child_2_velocity = self.velocity.rotate(new_angle * -1)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        
        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child2 = Asteroid(self.position.x, self.position.y, child_radius)
        
        child1.velocity = child_1_velocity * 1.2
        child2.velocity = child_2_velocity * 1.2


