def do_quad(i, f):
    i()
    f()
    f()
    f()
    f()
    i()
    f()
    f()
    f()
    f()
    i()

def print_line():
    a='+'
    s=4*'-'
    print a,s,a,s,a

def print_space():
    l='|';
    p=4*' ';
    print l,p,l,p,l

def run():
    do_quad(print_line, print_space)

run()
