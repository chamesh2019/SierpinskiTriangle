import math
import random
import pygame
from dataclasses import dataclass

@dataclass
class Point:
    x: int | float
    y: int | float

Iterations = 100000

def update(screen: pygame.Surface, start_point: Point, base_triangle: tuple[Point, Point, Point]) -> None:
    
    current_point = start_point
    
    for _ in range(Iterations):
        new_point = find_middle_point(current_point, random.choice(base_triangle))
        draw_point(screen, new_point)
        current_point = new_point
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
    
def draw_basics(screen: pygame.Surface) -> tuple[Point, tuple[Point, Point, Point]]:
    screen.fill((0, 0, 0))
    # set center pos to 2/3 of the screen
    center_pos = (screen.get_width() // 2, (screen.get_height() // 3)* 2)

    center_point = Point(center_pos[0], center_pos[1])
    contraint = 400
        
    point1 = calculate_cordinates(center_point, contraint, -90)
    draw_point(screen, point1)
    
    point2 = calculate_cordinates(center_point, contraint, 30)
    draw_point(screen, point2)

    point3 = calculate_cordinates(center_point, contraint, 150)
    draw_point(screen, point3)

    # random point inside point1, point2, point3 triangle
    

    return point3, (point1, point2, point3)


def find_middle_point(point1: Point, point2: Point) -> Point:
    x = (point1.x + point2.x) // 2
    y = (point1.y + point2.y) // 2
    return Point(x, y)


def draw_point(screen: pygame.Surface, point: Point) -> None:
    pygame.draw.circle(screen, (255, 255, 255), (point.x, point.y), 1)
    

def calculate_cordinates(center: Point, radius: int, angle: int) -> Point:
    x = center.x + radius * math.cos(math.radians(angle))
    y = center.y + radius * math.sin(math.radians(angle))
    return Point(x, y)