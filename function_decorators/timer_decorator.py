'''Timer_decorator is a module file that contains:
        timer: a class object that serves as a decorator
            for both methods and functions.
        timer_ver2: a function object with memory retention
            which serves as a decorator for both methods and
            functions
    
    This scipt requires emoji be installed within python
'''
import time
import functools
import emoji


class timer(object): # support for python 2
    """decorates a function, by wrapping the amount time it takes to 
        to run, to the function.

    Parameters
    ----------
    func : function object
        function to be decorated with timing
    keep_record : bool, optional
        A flag used to keep overall time this function ran (default is
        False)

    Methods
    -------
    __call__ :
        gets activated when this class is used to decorate a fuction, it
        responds to a call action to the decorated function
    
    __get__ :
        gets activated when this class is used to decorate a method, it
        responds to a call action to the decorated methos by creating
        a descriptor as a proxy before calling the method. this solves
        self(object attribute reference) collisions.
    """

    def __init__(self, func, keep_record=False):
        """
        Parameters
        ----------
        alltime : int
            total duration of all function calls
        count : int
            total no of all function calls
        func : function object, optional
            function to be decorated
        """
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
            recorded_data = f'{self.func.__name__}: ran in {elapsed_time:.5f} seconds \
                 , it has been called {self.count} times,/n with a total of \
                    {self.alltime:.5f} seconds'
        else:
            recorded_data = f"{self.func.__name__}: ran in {elapsed_time:.5f} seconds"
        print(emoji.emojize(' :yum: :yum: :yum:', use_aliases=True))
        print(recorded_data)
        print(emoji.emojize(' :tada: :tada: :tada:', use_aliases=True))
        
        return result  # self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        """ this is called when used to decorate a
            methods attached to a class """
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper


def timer_ver2(_func=None, *, keep_record=False):
    def timer_proxy(func):

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
            print(emoji.emojize(' :yum: :yum: :yum:', use_aliases=True))
            print(recorded_data)
            print(emoji.emojize(' :tada: :tada: :tada:', use_aliases=True))
            return result  
        timecounter.alltime = 0
        timecounter.count = 0
        return timecounter
    
    if _func is None:
        return timer_proxy
    else:
        return timer_proxy(_func)
