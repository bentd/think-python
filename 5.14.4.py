def test_triangle(a, b, c):
    if ((a+b)>c) and ((b+c)>a) and ((a+c)>b):
        print('Yes. These are the sides of a real triangle.')
    else:
        print('No. These are not the sides of a real triangle.')

print

def user_triangle(f=test_triangle):
    while True:
        print('Ready to test a triangle?')
        print
        a=raw_input('Side 1: ')
        a=int(a)
        b=raw_input('Side 2: ')
        b=int(b)
        c=raw_input('Side 3: ')
        c=int(c)
        print
        f(a, b, c)
        print

user_triangle()
