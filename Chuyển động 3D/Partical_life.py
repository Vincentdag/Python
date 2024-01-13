import pygame
import math
import random

WIDTH = 1400
HEIGHT = 800
TIME = 0.5

Light_blue = "#23e8e8"
Gold = "#ffc908"
RGB = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

pygame.init()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Particle Life")

class Particle:
    radius = 3
    mass = 1
    repell_zone = 10
    def __init__ (self, x, y, x_vel, y_vel, color):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color

    def Box(self):
        if self.x < 0 or self.x > WIDTH:
            self.x_vel = -self.x_vel
        if self.y < 0 or self.y > HEIGHT:
            self.y_vel = -self.y_vel

    '''def friction(self):
        self.x_vel = self.x_vel*0.9
        self.y_vel = self.y_vel*0.9'''

    def Draw(self,win,others):
        self.Box()
        self.x += self.x_vel * TIME
        self.y += self.y_vel * TIME
        pygame.draw.circle(win, self.color, (self.x , self.y ), self.radius)

    def distance(self,other):
        dis_x = self.x - other.x
        dis_y = self.y - other.y 
        distance = math.sqrt(dis_x**2 + dis_y**2)
        return distance

    def Lines(self, others, win):
        lines = 0
        for other in others:
            if self == other: continue
            if self.distance(other) < 200 and lines < 3 :
                lines +=1
                pygame.draw.line(win, self.color, (self.x,self.y),(other.x, other.y), 1)

    '''def collision(self, others):
        for other in others:
            if self == other: continue
            if self.distance(other) <= 2 * self.radius:
                self.x_vel = other.y_vel
                self.y_vel = other.x_vel'''
                

    '''def Force(self, others, repell, attract):
        for other in others:
            if self == other: continue
            force = line_function(repell / self.repell_zone, self.distance(other), self.repell_zone) + triangular_function(self.distance(other),10, attract, attract / 2 + self.repell_zone)
            #force = attract/ (1+self.distance(other))
            dis_x = self.x - other.x
            dis_y = self.y - other.y 
            force_x = force * dis_x / self.distance(other)
            force_y = force *dis_y / self.distance(other)
            self.x_vel += (force_x / self.mass) * TIME
            self.y_vel += (force_y / self.mass) * TIME'''

def trimp_function(x,a,b):
    if a < x < b: y = 1
    else: y = 0
    return y

def triangular_function(x,a,b,c):
    y = -(abs(2 * (a / b) * x -c) - a)* trimp_function(x, -b / 2 + c, b / 2 + c)
    return y

def line_function(theta, x, c):
    y = (x * math.tan(theta) - c) * trimp_function(x,0,c)
    return y

def random_excluding_0(a,b):
    x = 0
    while x == 0: x = random.randint(a,b)
    return x

def part_list(amount, color):
    list = []
    for i in range(0,amount,1):
        x = random.randint(0,WIDTH)
        y = random.randint(0,HEIGHT)
        x_vel = random_excluding_0(-3,3)
        y_vel = random_excluding_0(-3,3)
        part = Particle(x, y, x_vel, y_vel, color)
        list.append(part)
    return list

def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill("black")

    '''gold_parts = part_list(60, Gold)'''
    light_blue_parts = part_list(100, Light_blue)


    while run:
        clock.tick(100)
        WIN.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        '''for part in gold_parts:
            part.Draw(WIN, light_blue_parts)
            part.Lines(light_blue_parts,WIN)'''


        for part in light_blue_parts:
            part.Draw(WIN,light_blue_parts)
            part.Lines(light_blue_parts,WIN)
            #part.Force(light_blue_parts, 50,50)
            #part.friction()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()