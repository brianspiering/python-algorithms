class Bunch(dict):
    """'Bunch' pattern that allows specificy arbitary attributes in the constructor
    """
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self