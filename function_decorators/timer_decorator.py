import time
import functools


class timer(object): # support for python 2
    """ this decorator is used to time how long
        it takes for a function to run """

    def __init__(self, func, keep_record=False):
        self.alltime = 0
        self.count = 0
        self.func = func  # function to be timed
        self.keep_record = keep_record

    def __call__(self, *args, **kwargs) -> int:
        """ this is called when used to
            decorate an ordinary function """
        start_time = time.clock()
        result = self.func(*args, **kwargs)
        elapsed_time = time.clock() - start_time
        if self.keep_record:
            self.alltime += elapsed_time
            self.count += 1
            recorded_data = f'{self.func.__name__}: ran in {elapsed_time:.5f} seconds, \
                it has been called {self.count} times,/n with a total of \
                    {self.alltime:.5f} seconds'
        else:
            recorded_data = f"{self.func.__name__}: ran in {elapsed_time:.5f} seconds"
        print(recorded_data)
        
        return result  # self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        """ this is called when used to decorate a
            methods attached to a class """
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper


def timer_decorater_ver2(_func=None, *, keep_record=False):
    def timer(func):

        @functools.wraps(func)
        def timecounter(*args, **kwargs):
            start_time = time.clock()
            result = func(*args, **kwargs)
            elapsed_time = time.clock() - start_time
            if keep_record:
                timecounter.alltime += elapsed_time
                timecounter.count += 1
                recorded_data = f'{func.__name__}: ran in {elapsed_time:.5f} seconds, \
                    it has been called {timecounter.count} times,/n with a total of \
                        {timecounter.alltime:.5f} seconds'
            else:
                recorded_data = f"{func.__name__}: ran in {elapsed_time:.5f} seconds"
            print(recorded_data)
            return result  
        timecounter.alltime = 0
        timecounter.count = 0
        return timecounter
    
    if _func is None:
        return timer
    else:
        return timer(_func)
