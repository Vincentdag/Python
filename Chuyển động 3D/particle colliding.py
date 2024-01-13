import pygame
import random
pygame.init()



WIDTH = 800
HEIGH = 800
TIME =  1
Lightblue = "#23e8e8"
WIN = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption("partical_colliding")

class Particle:
    
    def __init__ (self, position, velocity, color, radius):
        
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color
        self.collision_status = False

    def distance(self, other):
        dx = self.position[0] - other.position[0]
        dy = self.position[1] - other.position[1]
        distance = (dx**2 + dy**2)**0.5
        return distance
    
    def collision_check(self, other):
        if self.distance(other) <= self.radius + other.radius:
            return True
        else: return False

    def velocity_update(self, other):
        a = self.velocity[0]
        self.velocity[0] = (self.radius**2 - other.radius**2) * self.velocity[0] / (self.radius**2 + other.radius**2) + 2 * other.radius**2 * other.velocity[0] / (self.radius**2 + other.radius**2)
        other.velocity[0] = -(self.radius**2 - other.radius**2) * other.velocity[0] / (self.radius**2 + other.radius**2) + 2 * self.radius**2 * a / (self.radius**2 + other.radius**2)
        b = self.velocity[1]
        self.velocity[1] = (self.radius**2 - other.radius**2) * self.velocity[1] / (self.radius**2 + other.radius**2) + 2 * other.radius**2 * other.velocity[1] / (self.radius**2 + other.radius**2)
        other.velocity[1] = -(self.radius**2 - other.radius**2) * other.velocity[1] / (self.radius**2 + other.radius**2) + 2 * self.radius**2 * b / (self.radius**2 + other.radius**2)


    def boundary(self):
        if self.position[0] <= 0 + self.radius and self.velocity[0] < 0:
            self.velocity[0] *= -1
        if self.position[0] >= WIDTH - self.radius and self.velocity[0] > 0:
            self.velocity[0] *= -1
        if self.position[1] <= 0 + self.radius and self.velocity[1] < 0:
            self.velocity[1] *= -1
        if self.position[1] >= HEIGH - self.radius and self.velocity[1] > 0:
            self.velocity[1] *= -1
    
    def direction(self, others):

        self.boundary()


        for other in others:
            if self != other and self.collision_check(other):
                if self.collision_status == False:
                    self.collision_status = True
                    other.collision_status = True
                    self.velocity_update(other)
                    break
                else: break
        else: self.collision_status = False

    def position_update(self):
        self.position[0] += self.velocity[0] * TIME     
        self.position[1] += self.velocity[1] * TIME

    def Draw(self, win):
        pygame.draw.circle(win, self.color, self.position, self.radius)

def create(color,number):
    part_list = []
    for i in range(0, number):
        radius = random.randint(10,50)
        position = [random.randint(0,WIDTH), random.randint(0,HEIGH)]
        velocity = [random.randint(-2,2), random.randint(-2,2)]
        part_list.append(Particle(position, velocity, color, radius))
    return part_list

def main():
    run = True
    clock = pygame.time.Clock()

    Lightblue_list = create(Lightblue,20)

    while run:

        clock.tick(100)
        WIN.fill("black")

        for part in Lightblue_list:
            part.direction(Lightblue_list)
            part.position_update()
        for part in Lightblue_list:
            part.Draw(WIN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    
    pygame.quit()
        

if __name__ == "__main__":
    main()
