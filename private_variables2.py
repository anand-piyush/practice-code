__author__ = 'piyush'
# python internally masks the variables of a class that start with __
# https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes

# PART 2
# to hide a class variable, property can be used
# https://docs.python.org/3/library/functions.html#property

class C():
    def __init__(self):
        self._x = 0

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

class D():
    def __init__(self):
        self._x = 0

    def getx(self):
        pass

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


if __name__=='__main__':
    c = C()
    print c.x
    d = D()
    print d.x
