# -*- coding: cp1252 -*-

# TYPEWRITER Program

# t is an instance of the Turtle() object
# 'for i in range' creates a for statement or loop that repeats 'n' number of times
# 'for i in range' is a common factor within the program and can be factored out and encapsulated in a separate function and then refactored into the program
# delay changes drawing time

from swampy.TurtleWorld import *
from math import *

world=TurtleWorld()
bob=Turtle()
bob.delay=0.0000001

# LEVEL 1 PRIMITIVES_________________________________________________________________________________________________________________________

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
        
def arc(radius, angle, t=bob):
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

# LEVEL 2 PRIMITIVES__________________________________________________________________________________________________________

def a(h=50, t=bob):
    "Creates an 'A' using an equilaterial 60* triangle"
    i=(3**(0.5))
    f=((2*h)/i)
    g=(f/2.0)
    pd(t)
    lt(t, 60)
    fd(t, f)
    rt(t, 120)
    fd(t, f)
    rt(t, 120)
    pu(t)
    fd(t, f)
    rt(t, 120)
    fd(t, g)
    rt(t, 60)
    pd(t)
    fd(t, g)
    rt(t, 60)
    fd(t, g)
    lt(t, 60)
    pu(t)
    fd(t, 10)

def b(h=50, t=bob):
    "Creates a 'B' using two semi-circles" 
    pd(t)
    fd(t, (h*(0.4)))
    arc((h/4.0), 180)   
    fd(t, (h*(0.4)))
    rt(t, 180)
    fd(t, (h*(0.3)))    
    arc((h/4.0), 180)
    fd(t, (h*(0.3)))
    fd(t, 5)    
    lt(t)
    fd(t, h)
    lt(t)
    pu(t)
    fd(t, ((h*(0.65))+10))

def c(h=50, t=bob):
    pu(t)
    fd(t, (h/2.0))
    fd(t, 10)
    arc((h/2.0), 180)
    fd(t, 4)
    pd(t)
    fd(t, 6) 
    arc((h/2.0), 180)
    fd(t, 10)
    pu(t)
    fd(t, 10)

def d(h=50, t=bob):
    pd(t)
    fd(t, (h*(0.2)))
    arc((h/2.0), 180)
    fd(t, (h*(0.2)))
    lt(t)
    fd(t, h)
    lt(t)
    pu(t)
    fd(t, ((h*(0.7))+10))

def e(h=50, t=bob):
    if (h%2)==0:
        h=h+1
    pd(t)
    lt(t)
    fd(t, h)
    rt(t)
    fd(t, (h*(0.625)))
    rt(t, 180)
    fd(t, (h*(0.625)))
    lt(t)
    fd(t, ((h+1)/2))
    lt(t)
    fd(t, (h*(0.625)))
    rt(t, 180)
    fd(t, (h*(0.625)))
    lt(t)
    fd(t, ((h-1)/2))
    lt(t)
    fd(t, (h*(0.625)))
    pu(t)
    fd(t, 10)

def f(h=50, t=bob):
    if (h%2)==0:
        h=h+1
    pd(t)
    lt(t)
    fd(t, h)
    rt(t)
    fd(t, (h*(0.625)))
    rt(t, 180)
    fd(t, (h*(0.625)))
    lt(t)
    fd(t, ((h+1)/2))
    lt(t)
    fd(t, (h*(0.625)))
    rt(t, 180)
    fd(t, (h*(0.625)))
    lt(t)
    fd(t, ((h-1)/2))
    lt(t)
    pu(t)
    fd(t, (h*(0.625)))
    fd(t, 10)

def g(h=50, t=bob):
    pu(t)
    fd(t, (h/2.0))
    fd(t, 10)
    arc((h/2.0), 180)
    fd(t, 3)
    pd(t)
    fd(t, 7) 
    arc((h/2.0), 180)
    arc((h/2.0), 90)
    lt(t)
    fd(t, (h/2.0))
    pu(t)
    lt(t)
    fd(t, (h/2.0))
    lt(t)
    fd(t, (h/2.0))
    fd(t, 10)

def h(h=50, t=bob):
    pd(t)
    lt(t)
    fd(t, h)
    rt(t, 180)
    fd(t, (h/2.0))
    lt(t)
    fd(t, (h*(0.75)))
    lt(t)
    fd(t, (h/2.0))
    rt(t, 180)
    fd(t, h)
    lt(t)
    pu(t)
    fd(t, 10)

def i(h=50, t=bob):
    pd(t)
    fd(t, (h*(0.3125)))
    fd(t, 1)
    lt(t)
    fd(t, h)
    lt(t)
    fd(t, (h*(0.3125)))
    rt(t, 180)
    fd(t, 1)
    fd(t, (h*(0.625)))
    rt(t, 180)
    fd(t, (h*(0.3125)))
    fd(t, 1)
    lt(t)
    fd(t, h)
    lt(t)
    fd(t, (h*(0.3125)))
    fd(t, 1)
    pu(t)
    fd(t, 10)

def j(h=50, t=bob):
    pu(t)
    lt(t)
    fd(t, h)
    rt(t, 180)
    fd(t, (h*(0.8)))
    pd(t)
    arc((h*(0.2)), 180)
    fd(t, (h*(0.8)))
    bk(t, (h*(0.8)))
    pu(t)
    bk(t, (h*(0.2)))
    rt(t)
    fd(t, 10)

def k(h=50, t=bob):
    a=(h*(2**0.5))/2.0
    pd(t)
    lt(t)
    fd(t, h)
    lt(t, 180)
    fd(t, h*0.5)
    lt(t, 135)
    fd(t, a)
    lt(t, 135)
    pu(t)
    fd(t, h*0.5)
    lt(t)
    fd(t, h*0.5)
    pd(t)
    lt(t, 45)
    fd(t, a)
    lt(t, 45)
    pu(t)
    fd(t, 10)

def l(h=50, t=bob):
    a=(h*(3**0.5))/3
    pd(t)
    lt(t)
    fd(t, h)
    lt(t, 180)
    fd(t, h)
    lt(t)
    fd(t, a)
    pu(t)
    fd(t, 10)

def m(h=50, t=bob):
    a=(2*h*(3**0.5))/3
    pd(t)
    lt(t)
    fd(t, h)
    rt(t, 150)
    fd(t, a)
    lt(t, 120)
    fd(t, a)
    rt(t, 150)
    fd(t, h)
    lt(t)
    pu(t)
    fd(t, 10)

def n(h=50, t=bob):
    a=(2*h*(3**0.5))/3
    pd(t)
    lt(t)
    fd(t, h)
    rt(t, 150)
    fd(t, a)
    lt(t, 150)
    fd(t, h)
    lt(t, 180)
    pu(t)
    fd(t, h)
    lt(t)
    fd(t, 10)
    
def o(h=50, t=bob):
    pu(t)
    fd(t, h*0.5)
    pd(t)
    circle(h*0.5, t)
    pu(t)
    fd(t, (h*0.5)+10)

def p(h=50, t=bob):
    "Creates a 'P' using a semi-circle" 
    pu(t)
    fd(t, (h*(0.4)))
    arc((h/4.0), 180)   
    fd(t, (h*(0.4)))
    rt(t, 180)
    pd(t)
    fd(t, (h*(0.3)))    
    arc((h/4.0), 180)
    fd(t, (h*(0.3)))
    fd(t, 5)    
    lt(t)
    fd(t, h)
    lt(t)
    pu(t)
    fd(t, ((h*(0.65))+10))

def q(h=50, t=bob):
    pu(t)
    fd(t, h*0.5)
    pd(t)
    circle(h*0.5, t)
    arc(h*0.5, 22.5, t)
    lt(t)
    fd(t, h*0.25)
    bk(t, h*0.5)
    fd(t, h*0.25)
    rt(t)
    arc(h*0.5, 337.5, t)
    pu(t)
    fd(t, (h*0.5)+10)

def r(h=50, t=bob):
    "Creates a 'R' using a semi-circle" 
    pu(t)
    fd(t, (h*(0.4)))
    arc((h/4.0), 180)   
    fd(t, (h*(0.4)))
    rt(t, 180)
    pd(t)
    fd(t, (h*(0.3)))    
    arc((h/4.0), 180)
    fd(t, (h*(0.3)))
    fd(t, 5)    
    lt(t)
    fd(t, h)
    lt(t, 180)
    fd(t, h*0.5)
    rt(t, 120)
    fd(t, (h*0.5*(3**0.5)))
    lt(t, 30)
    pu(t)
    fd(t, 10)

def s(h=50, t=bob):
    pd(t)
    fd(t, h*0.25)
    arc(h*0.25, 180, t)
    rt(t, 180)
    pu(t)
    arc(h*0.25, 180, t)
    rt(t, 180)
    pd(t)
    fd(t, h*0.25)
    bk(t, h*0.25)
    rt(t, 180)
    arc(h*0.25, 180, t)
    pu(t)
    rt(t, 180)
    arc(h*0.25, 180, t)
    fd(t, (h*0.25)+10)

def t(h=50, t=bob):
    pu(t)
    fd(t, (h*(0.625)))
    pd(t)
    lt(t)
    fd(t, h)
    lt(t)
    fd(t, (h*(0.625)))
    rt(t, 180)
    fd(t, (h*(1.25)))
    bk(t, (h*(0.625)))
    rt(t)
    fd(t, h)
    lt(t)
    pu(t)
    fd(t, (h*(0.625)))
    fd(t, 10)

def u(h=50, t=bob):
    pu(t)
    lt(t)
    fd(t, h)
    rt(t, 180)
    pd(t)
    fd(t, 0.75*h)
    arc(h*0.25, 180)
    fd(t, 3)
    fd(t, (0.75*h))
    rt(t, 180)
    pu(t)
    fd(t, h)
    lt(t)
    fd(t, 10)

def v(h=50, t=bob):
    a=h/(cos(pi/12))
    pu(t)
    lt(t)
    fd(t, h)
    rt(t, 165)
    pd(t)
    fd(t, a)
    lt(t, 150)
    fd(t, a)
    pu(t)
    rt(t, 165)
    fd(t, h)
    lt(t)
    pu(t)
    fd(t, 10)    

def w(h=50, t=bob):
    a=h/(cos(pi/12))
    pu(t)
    lt(t)
    fd(t, h)
    rt(t, 165)
    pd(t)
    fd(t, a)
    lt(t, 150)
    fd(t, a)
    pu(t)
    rt(t, 165)
    fd(t, h)
    lt(t)
    pu(t)
    lt(t)
    fd(t, h)
    rt(t, 165)
    pd(t)
    fd(t, a)
    lt(t, 150)
    fd(t, a)
    pu(t)
    rt(t, 165)
    fd(t, h)
    lt(t)
    fd(t, 10)

def x(h=50, t=bob):
    pd(t)
    lt(t, 45)
    fd(t, (h*(2**0.5)))
    lt(t, 135)
    pu(t)
    fd(t, h)
    lt(t, 135)
    pd(t)
    fd(t, (h*(2**0.5)))
    lt(t, 45)
    pu(t)
    fd(t, 10)

def y(h=50, t=bob):
    v=h/3.5
    a=v/(sin(pi/4.5))
    d=a*(sin((5*pi)/18))
    pu(t)
    fd(t, d)
    lt(t)
    pd(t)
    fd(t, 2.5*v)
    lt(t, 50)
    fd(t, a)
    bk(t, a)
    rt(t, 100)
    fd(t, a)
    bk(t, a)
    lt(t, 50)
    bk(t, 2.5*v)
    rt(t)
    pu(t)
    fd(t, (d+10))

def z(h=50, t=bob):
    a=(h*(3**0.5))/3
    pu(t)
    fd(t, a)
    pd(t)
    bk(t, a)
    lt(t, 60)
    fd(t, 2*a)
    lt(t, 120)
    fd(t, a)
    bk(t, a)
    lt(t, 60)
    fd(t, 2*a)
    lt(t, 120)
    fd(t, a)
    pu(t)
    fd(t, 10)
        
def space(t=bob):
    pu(t)
    fd(t, 20)

def period(h, t=bob):
    pd(bob)
    a=int(h*(0.1))
    for i in range(a):
        if a==1:
            break
        square(a)
        a=a-1
    pu(t)
    fd(t, (a+10))

def question(h, t=bob):
    pd(t)
    period(h, t)
    bk(t, ((int(h*0.1))+4))
    lt(t)
    pu(t)
    fd(t, (h*(0.2)))
    pd(t)
    fd(t, (h*(0.3)))
    rt(t)
    arc((h*(0.2)), 185, t)
    pu(t)
    arc((h*(0.2)), 175, t)
    rt(t)
    fd(t, (h*(0.50)))
    lt(t)
    fd(t, ((h*(0.2))+10))

def exclamation(h, t=bob):
    pd(t)
    period(h, t)
    bk(t, ((int(h*0.1))+5))
    lt(t)
    pu(t)
    fd(t, (h*(0.2)))
    pd(t)
    fd(t, (h*0.8))
    pu(t)
    bk(t, h)
    rt(t)
    fd(t, ((h*(0.05))+10))

def comma(h, t=bob):
    pd(bob)
    a=int(h*(0.05))
    for i in range(a):
        if a==1:
            break
        square(a)
        rt(t)
        fd(t, a)
        lt(t)
        square(a)
        lt(t)
        fd(t, a)
        rt(t)
        a=a-1
    pu(t)
    fd(t, (a+10))   
    

# LEVEL 3 PRIMITIVES & EXECUTION__________________________________________________________________________________________________________
            
def iterate(user, size=50):
    for letter in user:
        if letter==' ':
            space()
        if letter=='.':
            period(size)
        if letter=='?':
            question(size)
        if letter=='!':
            exclamation(size)
        if letter==',':
            comma(size)
        if letter=='a' or letter=='A':
            a(size)
        if letter=='b' or letter=='B':
            b(size)
        if letter=='c' or letter=='C':
            c(size)
        if letter=='d' or letter=='D':
            d(size)
        if letter=='e' or letter=='E':
            e(size)
        if letter=='f' or letter=='F':
            f(size)
        if letter=='g' or letter=='G':
            g(size)
        if letter=='h' or letter=='H':
            h(size)
        if letter=='i' or letter=='I':
            i(size)
        if letter=='j' or letter=='J':
            j(size)
        if letter=='k' or letter=='K':
            k(size)
        if letter=='l' or letter=='L':
            l(size)
        if letter=='m' or letter=='M':
            m(size)
        if letter=='n' or letter=='N':
            n(size)
        if letter=='o' or letter=='O':
            o(size)
        if letter=='p' or letter=='P':
            p(size)
        if letter=='q' or letter=='Q':
            q(size)
        if letter=='r' or letter=='R':
            r(size)
        if letter=='s' or letter=='S':
            s(size)
        if letter=='t' or letter=='T':
            t(size)
        if letter=='u' or letter=='U':
            u(size)
        if letter=='v' or letter=='V':
            v(size)
        if letter=='w' or letter=='W':
            w(size)
        if letter=='x' or letter=='X':
            x(size)
        if letter=='y' or letter=='Y':
            y(size)
        if letter=='z' or letter=='Z':
            z(size)

def run(y=100, x=-175, size=input('Font Size: ')):
    if not type(size)==int:
        print 'Sorry, invalid literal'
        run()
    start(x, y)
    end=['END','End','end']
    font=['Change Size','Change size','change size']
    new='new line'
    while True:     
        user_input=raw_input('|>>> ')
        for i in end:
            if user_input==i:
                return  
        for i in font:
            if user_input==i:
                y=(bob.get_y())
                x=(bob.get_x())
                run(y, x, input('Font Size: '))
        if user_input==new:
            run((y-(2*(size))), -175, size=size)
        else:
            if user_input=='':
                space()
            else:
                iterate(user_input, (int(size)))
    return

run()
     















