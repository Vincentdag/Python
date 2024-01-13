from math import *
import pygame

pygame.init()

Lightblue = "#23e8e8"
WIDTH, HEIGH = 800, 800
WIN = pygame.display.set_mode([WIDTH,HEIGH])
pygame.display.set_caption("Spinning cube")

def exp(x):
    return sum([x**n / factorial(n) for n in range(0,170)])

def matrix_multi(a, b):
    c = []
    Row_a = len(a)
    Col_a = len(a[1])
    Col_b = len(b[0])
    for i in range(0, Row_a):
        c.append([])
        for k in range(0, Col_b):
            x = 0
            for j in range(0, Col_a):
                x += a[i][j] * b[j][k]
            c[i].append(x)
    return c

def matrix_add(a,b):
    Row_a = len(a)
    Col_a = len(a[0])
    c = [[n for n in range(0,Col_a)] for _ in range(0, Row_a) ]
    for i in range(0,Row_a):
        for j in range(0, Col_a):
            c[i][j] = a[i][j] + b[i][j]
    return c

def matrix_sub(a,b):
    Row_a = len(a)
    Col_a = len(a[0])
    c = [[n for n in range(0,Col_a)] for _ in range(0, Row_a) ]
    for i in range(0,Row_a):
        for j in range(0, Col_a):
            c[i][j] = a[i][j] - b[i][j]
    return c

def matrix_shape(a, row, col):
    return [[a[n] for n in range( _ * col , col + _ * col)] for _ in range(0, row)] 

def list_shape(a):
    b = []
    for row in range(0, len(a)):
        for col in range(0, len(a[row])):
            b.append(a[row][col])
    return b

def centralise(a):
    a[0] += WIDTH/2 
    a[1] = -(a[1] - HEIGH/2)
    return a

def rotation(x_angle, y_angle, z_angle, point):
    ro_matrix_x = [[1, 0, 0],
                    [0, cos(x_angle), -sin(x_angle)],
                    [0, sin(x_angle), cos(x_angle)]]
    
    ro_matrix_y = [[cos(y_angle), 0, sin(y_angle)],
                    [0, 1, 0],
                    [sin(y_angle), 0, cos(y_angle)]]
    
    ro_matrix_z = [[cos(z_angle), -sin(z_angle), 0],
                    [sin(z_angle), cos(z_angle), 0],
                    [0, 0, 1]]
    rotate_x = matrix_multi(ro_matrix_x, point)
    rotate_y = matrix_multi(ro_matrix_y,rotate_x )
    rotate_z = matrix_multi(ro_matrix_z,rotate_y )
    return rotate_z

def projection(point, size):
    pro_matrix = [[size, 0, 0],
                  [0, size, 0]]
    return matrix_multi(pro_matrix, point)



def cube():
    points = [] 
    points.append(matrix_shape([1,1,1], 3, 1))
    points.append(matrix_shape([-1,1,1], 3, 1))
    points.append(matrix_shape([-1,-1,1], 3, 1))
    points.append(matrix_shape([1,-1,1], 3, 1))
    points.append(matrix_shape([1,1,-1], 3, 1))
    points.append(matrix_shape([-1,1,-1], 3, 1))
    points.append(matrix_shape([-1,-1,-1], 3, 1))
    points.append(matrix_shape([1,-1,-1], 3, 1))
    return points

def draw_cube(pro_points):
    pygame.draw.line(WIN,Lightblue, pro_points[0], pro_points[3], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[0], pro_points[1], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[0], pro_points[4], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[2], pro_points[3], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[2], pro_points[1], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[2], pro_points[6], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[7], pro_points[3], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[7], pro_points[6], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[7], pro_points[4], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[5], pro_points[6], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[5], pro_points[4], 2)
    pygame.draw.line(WIN,Lightblue, pro_points[5], pro_points[1], 2)



def doughnut():
    points = []
    res = pi/24
    for i in range(0, int(2*pi / res)):
        for j in range(0, 24): 
            x = (1 + 0.5 * cos(j * pi/12)) * cos(i * res)
            y = (1 + 0.5 * cos(j * pi/12)) * sin(i * res)
            z = 0.5*sin(j * pi/12  )
            point = matrix_shape([x,y,z], 3, 1)
            points.append(point)
    return points   

def draw_doughnut(pro_points,a):
    for i in range(0, int(len(pro_points)/24)):
        for j in range(24 * i, 24 * i + 24):
            if j != (24 * i + 24 - 1):
                pygame.draw.line(WIN, 240, pro_points[j], pro_points[j + 1], a)
            else:
                pygame.draw.line(WIN, 240, pro_points[j - 23], pro_points[j], a)
            
            if i != len(pro_points)/24 - 1:
                pygame.draw.line(WIN, 240, pro_points[j], pro_points[j + 24], a)
            else: 
                pygame.draw.line(WIN, 240, pro_points[j], pro_points[j - (len(pro_points) - 24)], a)



def spring():
    points = []
    for i in range(0,500,1):
        x = i/100
        y = sin((4)*pi*x)
        z = cos((4)*pi*x)
        a = [x,y,z]
        points.append(matrix_shape(a,3,1))
    return points

def draw_spring(pro_points):
    for i in range(0, len(pro_points) - 1,):
        pygame.draw.line(WIN, Lightblue, pro_points[i], pro_points[i+1])



def cone(a,b):
    points = []
    for i in range(0,500):
        t = i/100
        y = exp(a*t) * (exp(complex(0, b)*t)).imag
        z = exp(a*t) * (exp(complex(0, b)*t)).real
        c = [t,y,z]
        points.append(matrix_shape(c,3,1))
    return points

def draw_cone(pro_points):
    for i in range(0, len(pro_points) - 1):
        pygame.draw.line(WIN, Lightblue, pro_points[i], pro_points[i+1])
        
        
    


def main():
    run = True
    clock = pygame.time.Clock()
    x_angle = 0
    y_angle = 0
    z_angle = 0

    cone_points = cone(0.3,5)
    spring_points = spring()
    doughnut_points = doughnut()
    cube_points = cube()
    

    while run:
        clock.tick(100)
        WIN.fill("black")

        x_angle += 0.009
        y_angle += 0.009    
        z_angle += 0.009
    
        pro_points1 = []
        pro_points2 = []
        pro_points3 = []
        pro_points4 = []

#draw a cube
        '''for point in cube_points:
            pro_point = centralise(list_shape(projection(rotation(x_angle, y_angle, z_angle, point), 100)))
            pro_points1.append(pro_point)

        draw_cube(pro_points1)'''

#draw a cone shape
        '''for point in cone_points:
            pro_point = centralise(list_shape(projection(rotation(x_angle, y_angle, z_angle, point), 50)))
            pro_points3.append(pro_point)

        draw_cone(pro_points3)'''
        

#draw a spring shape
        '''for point in spring_points:
            pro_point = centralise(list_shape(projection(rotation(x_angle, y_angle, z_angle, point), 50)))
            pro_points4.append(pro_point)

        draw_spring(pro_points4)'''

#draw a doughnut
        for point in doughnut_points:
            pro_point = centralise(list_shape(projection(rotation(x_angle, y_angle, z_angle, point), 200)))
            pro_points2.append(pro_point)

        draw_doughnut(pro_points2, 1)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()