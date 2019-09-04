# -*- coding: cp1252 -*-
# MSHAPE Program

# t is an instance of the Turtle() object
# 'for i in range' creates a for statement or loop that repeats 'n' number of times
# 'for i in range' is a common factor within the program and can be factored out and encapsulated in a separate function and then refactored into the program
# delay changes drawing time
# As of 14-8-29;11:33, the cirlce around the flower "bug" was officially "debugged" [I used degrees instead of radians]

from swampy.TurtleWorld import *
from math import *

world=TurtleWorld()
bob=Turtle()
bob.delay=0.000001

# DEFINITIONS________________________________________________________________________________________________________________

def start(a, b, t=bob):
    "Places turtle() object away from point of origin via x and y forward movement without making any lines"
    t.x=a
    t.y=b
    t.redraw()

def polyline(n, length, angle, t=bob):
    "Piece of code to be refactored into the remaining shape functions"
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def square(length, t=bob):
    "Creates a square through repetitive lines and 90 degree turns"
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(n, length, t=bob):
    "Creates a sizable regular polygon using the number of sides to find the degree of external angles"
    angle = 360.0/n
    polyline(n, length, angle, t)

def inverted_polygon(n, length, t=bob):
    "This was an accidental function when I was trying to make regular polygons"
    p=(n-2)*180
    q=(p/(1.0*n))
    for i in range(n):
        fd(t, length)
        lt(t, q)
        
def arc(angle, radius, t=bob):
    """
    Draws an arc using radius to determine length of the arc, this is known as arc_length
    And uses angle obviously to determine angle
    N is the number of sides and is dependent on the size of the circle
    """
    arc_length=2*radius*pi*angle/360
    n=int(arc_length/3)+1
    length=arc_length/n
    step_angle=float(angle)/n
    polyline(n, length, step_angle, t)

def circle(radius, t=bob):
    "Refactors arc to create a 360 degree arc also known as a circle"
    arc(radius, 360, t)

def petal(angle, radius, t=bob):
    """
    Creates a flower petal by combining two arcs
    This is done through creating an arc
    Then turning around short of a full 180 degrees to creat the adjacent arc
    """
    for i in range(2):
         arc(radius, angle, t)
         lt(t, abs(180-angle))

def flower(n, angle, radius, t=bob):
    "Creates a flower through repetitive execution of the petal function divided equally into 360 degrees"
    for i in range(n):
        petal(angle, radius, t)
        lt(t, 360.0/n)

def flower_in_circle(n, angle, radius, t=bob):
    "Creates flower that is circumvented by a circle with a radius that is equal to the chord of the arcs of the petals"
    for i in range(n):
        petal(angle, radius, t)
        lt(t, 360.0/n)
    lt(t, (angle/2.0))
    chord=(sin(radians(angle/2.0)))*2*radius  
    pu(t)
    fd(t, chord)
    lt(t)
    pd(t)
    circle(chord, t)

def pie(n, length, t=bob):
    "Disects polygon into triangles similar to a pie"
    angle=360.0/n
    radius=(length/2.0)/(sin(radians(angle/2)))
    for i in range(n):
        fd(t, radius)
        lt(t, 180)
        fd(t, radius)
        lt(t, (180+angle))
    pu(t)
    fd(t, radius)
    lt(t, 90+180.0/n)
    pd(t)
    polygon(n, length, t)

def spiral(n, length=3, a=0.1, b=0.0002, t=bob):
    """
    Draws an Archimedian spiral starting at the origin.

    Args
    n: how many line segments to draw
    length: how long each segment is
    a: how loose the initial spiral starts out (larger is looser)
    b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    
    """
    theta = 0.0
    for i in range(n):
        fd(t, length)
        dtheta = 1 / (a + b * theta)
        print(dtheta)
        lt(t, dtheta)
        theta += dtheta

def branch(n, length, t=bob):
    "Draws a sort of fractal branch that continuously divides into two more branches."
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(length, n-1, t)
    rt(t, 2*angle)
    draw(length, n-1, t)
    lt(t, angle)
    bk(t, length*n)

def snowflakebranch(branches, length, n=3, t=bob):
    for i in range(branches):
        angle=360.0/branches
        branch(n, length, t)
        lt(t, angle)
    
def koch(n, t=bob):
    "Draws a kock curve with length n."
    if n<3:
        fd(t, n)
        return
    m=n/3.0
    koch(m, t)
    lt(t, 60)
    koch(m, t)
    rt(t, 120)
    koch(m, t)
    lt(t, 60)
    koch(m, t)

def snowflake(n, t=bob):
    "Draws a snowflake (a triangle with a koch curve for each side)."
    for i in range(3):
        koch(n, t)
        rt(t, 120)

# EXECUTION___________________________________________________________________________________________________________________

def run():
    while True:
        cont=raw_input('Continue? \n')
        if cont=='no':
            return
        none=None
        positiona=input('Where do you wish to start on the x-axis? \n')
        positionb=input('Where do you wish to start on the y-axis? \n')
        start(positiona, positionb)
        function=input('Which shape function would you like to call? \n')
        parameter1=input('How many sides? \n')
        parameter2=input('What is the length of this shape? \n')
        parameter3=input('What is the angle of this shape? \n')
        parameter4=input('What is the radius of this shape? \n')
        if function==polyline:
            polyline(parameter1, parameter2, parameter3)
        elif function==square:
            square(parameter2)
        elif function==polygon:
            polygon(parameter1, parameter2)
        elif function==inverted_polygon:
            inverted_polygon(parameter1, parameter2)
        elif function==arc:
            arc(parameter3, parameter4)
        elif function==circle:
            cirlce(parameter4)
        elif function==petal:
            petal(parameter3, parameter4)
        elif function==flower:
            flower(parameter1, parameter3, parameter4)
        elif function==flower_in_circle:
            flower_in_circle(parameter1, parameter3, parameter4)
        elif function==pie:
            pie(parameter1, parameter2)
        elif function==spiral:
            spiral(parameter1)
        elif function==branch:
            branch(parameter1, parameter2)
        elif function==snowflakebranch:
            snowflakebranch(parameter1, parameter2)
        elif function==koch:
            koch(parameter1)
        else:
            snowflake(parameter1)

run()
