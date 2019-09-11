import inspect


def reset(arg, default=-999):
    #if arg not in locals():
    #    return 
    print(inspect.getargspec(reset).args)
    
x=3
reset(x)
