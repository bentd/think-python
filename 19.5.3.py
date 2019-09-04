# Chapter 19 Section 5 Excercise 3

from swampy.Gui import *

def make_gui():

    global g
    g = Gui()
    g.title('Chapter 19 Section 5 Excercise 3')

    global canvas
    canvas = g.ca(width=500, height=500)
    canvas.config(bg='black')

#-------------------------------------------------------------

def make_circle_button():

    circle_button = g.bu(text= 'Make New Circle', command= make_circle)

def make_circle():

    global item
    item = canvas.circle([0,0],100,fill='white')

#--------------------------------------------------------------

def make_entry():

    global entry
    entry = g.en(text= 'Type Color of Circle')

#---------------------------------------------------------------

def edit_circle_button():

    edit_button = g.bu(text= 'Change Circle Color', command= edit_circle)
    
def edit_circle():

    global item
    
    try:  
        item.config(fill= entry.get().lower())
    except:
        error()

#-----------------------------------------------------------------

def error():

    current_entry = entry.get().lower()
    error_message = "'%s' color not recognized..." %(current_entry)
    print error_message
    
    entry.delete(0,END)
    entry.insert(END, error_message)

#--------------------------------------------------------------------
    
def main():

    make_gui()
    make_circle_button()
    make_entry()
    edit_circle_button()
    g.mainloop()

if __name__ == '__main__':

    main()
