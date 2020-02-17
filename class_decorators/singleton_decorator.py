

class singleton:
    def __init__(self, undecoratedClass):
        self.undecoratedClass = undecoratedClass
        self.instance = None

    def __call__(self, *args, **kwargs):
        print(self.undecoratedClass.closed)
        if self.undecoratedClass.closed is True:
            self.instance = None
        if self.instance is None:
            self.instance = self.undecoratedClass(*args, **kwargs)
            self.undecoratedClass.closed = True
        else:
            print('instance already exists')
        return self.instance
