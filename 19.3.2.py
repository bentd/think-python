# Chapter 19 Section 3 Excercise 2

from swampy.Gui import *

def make_gui():

    global g
    g = Gui()
    g.title('Chapter 19 Excercise 2')

def make_button():

    button=g.bu(text= 'Create Circle', command= make_canvas_circle)

def make_canvas():

    global canvas
    canvas = g.ca(width=500, height=500)
    canvas.config(bg='black')
    

def make_circle():

    global item
    item = canvas.circle([0,0],100,fill='white')
    item.config(outline='red',width=1)


def make_canvas_circle():

    make_canvas()
    make_circle()

def main():

    make_gui()
    make_button()
    g.mainloop()

if __name__ == '__main__':

    main()
