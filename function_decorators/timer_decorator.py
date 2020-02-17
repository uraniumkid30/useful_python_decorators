import time
import functools


class timer(object):
    """ this decorator is used to time how long
        it takes for a function to run """

    def __init__(self, func):
        self.alltime = 0
        self.func = func  # function to be timed

    def __call__(self, *args, **kwargs) -> int:
        """ this is called when used to
            decorate an ordinary function """
        start_time = time.clock()
        result = self.func(*args, **kwargs)
        elapsed_time = time.clock() - start_time
        self.alltime += elapsed_time
        elasped_data = f"{self.func.__name__}: ran in {elapsed_time:.5f} seconds"
        # '%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime)
        print(elasped_data)
        return result  # self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        """ this is called when used to decorate a
            methods attached to a class """
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper


def timerV2(func):

    @functools.wraps(func)
    def timecounter(*args, **kwargs):
        start_time = time.clock()
        result = func(*args, **kwargs)
        elapsed_time = time.clock() - start_time
        timecounter.alltime += elapsed_time
        elasped_data = f"{func.__name__}: ran in {elapsed_time:.5f} seconds"
        # '%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime)
        print(elasped_data)
        return result  # self.func(*args, **kwargs)
    timecounter.alltime = 0
    return timecounter
