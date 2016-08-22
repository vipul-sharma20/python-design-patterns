"""
Singleton Pattern

Source: PEP 318 page
https://www.python.org/dev/peps/pep-0318/#examples
(from Shane Hathaway on python-dev)

Interesting Discussion:
http://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons-in-python
"""


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class MyClass:
    pass

"""
Code demo:

In [1]: from singleton import MyClass

In [2]: a = MyClass()

In [3]: b = MyClass()

In [4]: id(a)
Out[4]: 4379132776

In [5]: id(b)
Out[5]: 4379132776

In [6]: id(a) == id(b)
Out[6]: True
"""
