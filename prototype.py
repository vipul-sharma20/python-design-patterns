"""
Prototype Pattern

Source: me

Interesting Discussion:
http://stackoverflow.com/questions/17610275/prototype-pattern-in-python
"""

import copy


class Car:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels


class Prototype:
    def clone(self, *args, **kwargs):
        return copy.deepcopy(self)


if __name__ == '__main__':
    car1 = Car('red', 4)
    prototype = Prototype()

    car2 = prototype.clone(car1)
    car2.color = 'blue'
    car2.wheels = 4

