from swampy.Gui import *

def make_gui():

    global g

    g = Gui()

    g.title('Chapter 19 Section 2 Excercise 1')


def make_first_button():

    button_a = g.bu(text = 'Button A', command = make_second_button)


def make_second_button():

    button_b = g.bu(text = 'Button B', command = make_label)


def make_label():

    g.la(text = 'Nice job!')

def main():

    make_gui()

    make_first_button()

    g.mainloop()


if __name__ == '__main__':

    main()










    
