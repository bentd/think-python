
class Power(int):

    def __init__(self, val=0):

        self._val = int(val)
    
    def ispowerof(self, other):

        if self == other: return True

        if self % other == 0: return Power(self/other).ispowerof(other)

        else: return False

def run():

    num1 = Power(75)

    num2 = Power(125)

    num3 = Power(5)

    print num1.ispowerof(num3)

    print num2.ispowerof(num3)


if __name__ == '__main__':

    run()

                
