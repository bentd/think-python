
from swampy.TurtleWorld import *
from math import *

def world():

    global turtle
    global world

    world = TurtleWorld()
    turtle = Turtle()

    world.wm_minsize(width=800, height=800)

    turtle.delay = 0.00000001

    start(turtle, (0, 0))

def reset():

    global turtle
    global world

    world.clear()
    turtle = Turtle()

    start(turtle, (0, 0))

def start(turtle, coord):
    
    turtle.x = coord[0]
    turtle.y = coord[1]
    turtle.redraw()

def extangle(sides):

    return 360.0 / sides

def circumference(radius):

    return 2 * pi * radius

def chord(half, radius):

    return sin(radians(half)) * 2 * radius



def polyline(turtle, sides, length, angle):

    for i in range(sides):

        fd(turtle, length)
        lt(turtle, angle)

def polygon(turtle, sides, length):
    
    polyline(turtle, sides, length, extangle(sides))

def arc(turtle, radius, angle):
    
    arc = circumference(radius) * (angle / 360.0)
    sides = int(arc / 3) + 1
    length = arc / sides
    angle = float(angle) / sides
    polyline(turtle, sides, length, angle)

def square(turtle, length):

    polygon(turtle, 4, length)
        
def circle(turtle, radius):

    arc(turtle, radius, 360)

def petal(turtle, radius, angle):

    turn = abs(180 - angle)

    for i in range(2):
        
         arc(turtle, radius, angle)
         lt(turtle, turn)

def flower(turtle, sides, radius, angle):

    turn = 360.0 / sides

    for i in range(sides):
        
        petal(turtle, radius, angle)
        lt(turtle, turn)

def circledflower(turtle, sides, radius, angle):

    flower(turtle, sides, radius, angle)

    half = angle / 2.0
        
    lt(turtle, half)
    pu(turtle)
    fd(turtle, chord(half, radius))
    lt(turtle)
    pd(turtle)
    
    circle(turtle, chord(half, radius))

def pie(turtle, slices, radius):

    angle = 360.0 / slices
    
    for i in range(slices):
        
        fd(turtle, radius)
        bk(turtle, radius)
        lt(turtle, angle)

    fd(turtle, radius)
    lt(turtle)
    circle(turtle, radius)

def spiral(turtle, loops, length=3, a=0.1, b=0.0002):
    
    theta = 0.0
    dtheta = lambda: 1 / (a + b * theta)
    
    for i in range(loops):
        
        fd(turtle, length)
        lt(turtle, dtheta())
        theta += dtheta()

def branch(turtle, sides, length, angle=50):

    if n == 0: return

    foo = sides * length
    turn = 2 * angle
    
    fd(turtle, foo)
    lt(turtle, angle)

    for turn, ang in [(rt, 2*angle), (lt, angle)]:
        
        branch(turtle, sides-1, length)
        turn(turtle, ang)
    
    bk(turtle, foo)

def snowflakebranch(turtle, branches, sides, length):

    for i in range(branches):

        angle = 360.0 / branches
        branch(turtle, sides, length)
        lt(turtle, angle)
    
def koch(turtle, sides):

    foo = sides / 3.0

    if foo < 1:
        
        fd(turtle, sides)
        return

    else:

        for turn, dist in [(lt, 60), (rt, 120), (lt, 60), (lt, 360)]:

            koch(turtle, foo)
            turn(turtle, dist)
            

def snowflake(turtle, sides):
    
    for i in range(3):
        
        koch(turtle, sides)
        rt(turtle, 120)

def main():

    world()
    
    while True:
        pie(turtle, 8, 100)
        reset()
    

if __name__ == "__main__":

    main()
