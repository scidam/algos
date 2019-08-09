import sys
from functools import partial, wraps

class Sentinel(Exception): pass

class SetTrace(object):
    """
    with SetTrace(monitor):
        ...
    """

    def __init__(self, func, arguments):
        self.arguments = arguments
        self.func = func

    def __enter__(self):
        sys.settrace(partial(self.func, arguments=self.arguments))
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        sys.settrace(None)
        # http://effbot.org/zone/python-with-statement.htm
        # When __exit__ returns True, the exception is swallowed.
        # When __exit__ returns False, the exception is reraised.

        # This catches Sentinel, and lets other errors through
        return isinstance(exc_value, Sentinel)


def monitor(frame, event, arg, **kwargs):
    if event == "line":
        l = frame.f_locals
        if 'arguments' in kwargs:
            for ar in kwargs['arguments']:
                x = l.get(ar, "Not defined")
                print('{} = {}'.format(ar, x))
    return partial(monitor, arguments=kwargs['arguments'])


def trace(arguments=[]):
    if arguments:
        def detrace(f):
            def new_f(*args, **kwargs):
                result  = None
                with SetTrace(monitor, arguments):
                    result = f(*args, **kwargs)
                return result
            return new_f
        return detrace
    else:
        return lambda x: x
    

def foo():
    x = 0
    while True:
        print('bar', x)
        x += 1


@trace(arguments=['x'])
def peek():
    x = 3
    return 1

    
if __name__ == '__main__':
    peek()
