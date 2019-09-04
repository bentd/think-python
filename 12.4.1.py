def sumall(*args):
    return sum(args)

def sumall_(*args):
    len_=len(args)
    if len_ == 1: return args[0]
    if len_ == 2: return args[0]+args[1]
    else: return args[0]+sumall_(*args[1:len_])

print sumall_(1,2,3,4)
