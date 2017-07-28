__author__ = 'piyush'
# python internally masks the variables of a class that start with __
# https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes

# PART 2
# to hide a class variable, property can be used
# https://docs.python.org/3/library/functions.html#property

class A():
    def __init__(self):
        self.__var = 0
        self._var = 3
        self.var1 = 1
    def __func1(self):
        print "func1 called"
    def func2(self):
        print "func2 called"

if __name__=='__main__':
    a = A()
    try:
        print a.__var # error
    except Exception as e:
        print str(e)
    print a.var1 #ok
    try:
        a.__func1()  # error
    except Exception as e:
        print str(e)
    print a.func2() # runs fine
    print a._var   # this is ALSO fine
    print a.__dict__ # illustrates the masked names of the variables
