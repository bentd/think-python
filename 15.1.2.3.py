from copy import copy,deepcopy
from swampy.World import World



class Point(object):
    """ Represents a point in 2-D space.
        attributes: x-coordinate, y-coordinate """

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return '(%g,%g)' %(self.x,self.y)
        
    def __add__(self,other):
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        elif isinstance(other, tuple):
            return Point(self.x+other[0],self.y+other[1])


def distance(point1,point2):
    x2=(point1.x-point2.x)**2
    y2=(point1.y-point2.y)**2
    return (x2+y2)**0.5

def draw_point(canvas,point):
    bbox=[[point.x,point.y],[point.x,point.y]]
    canvas.rectangle(bbox, outline='black', width=2, fill='black')



class Rectangle(object):
    """ Represents a rectangle. 
        attributes: width, height, lower left-hand corner, color """

def dimensions(rect,width,height):
    rect.width=width
    rect.height=height

def corner(rect,x,y):
    rect.corner=Point()
    rect.corner.x=x
    rect.corner.y=y

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_corner(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def move_copy(rect,dx,dy):
    newrect=deepcopy(rect)
    newrect.corner.x += dx
    newrect.corner.y += dy
    return newrect

def draw_rectangle(canvas, rect):
    bbox = [[rect.corner.x,rect.corner.y],[rect.corner.x+rect.width,rect.corner.y+rect.height]]
    canvas.rectangle(bbox, outline='black', width=2, fill=rect.color)



class Circle(object):
    """ Represents a circle object.
        attributes: center, radius, color """

def center(circle,x,y):
    circle.center=Point()
    circle.center.x=x
    circle.center.y=y

def draw_circle(canvas,circle):
    canvas.circle([circle.center.x,circle.center.y], circle.radius, outline=None, fill=circle.color)




if __name__ == '__main__':
    
    point1=Point(0,4)
    point2=Point(3,0)
    print str(point1)
    print point2
    print distance(point1,point2)

    rect1=Rectangle()
    rect2=Rectangle()
    rect1.color='white'
    rect2.color='red'
    dimensions(rect1,300,100)
    dimensions(rect2,300,100)
    corner(rect1,-150,0)
    corner(rect2,-150,-100)
    print (find_center(rect1))

    circle=Circle()
    center(circle,-25,0)
    circle.radius=70
    circle.color='blue'


    world=World()
    canvas = world.ca(width=500, height=500, background='white')

    draw_point(canvas,point1)
    draw_rectangle(canvas, rect1)
    draw_rectangle(canvas, rect2)
    points=[[-150,-100],[-150,100],[-150+(100*(3**0.5)),0]]
    canvas.polygon(points,fill='blue')

    world.mainloop()



