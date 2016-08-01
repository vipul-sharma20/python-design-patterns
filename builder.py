"""
Builder Pattern

Reference: https://en.wikipedia.org/wiki/Builder_pattern#Java

Interesting Discussion:
http://stackoverflow.com/questions/11977279/builder-pattern-equivalent-in-python
"""

class Car:
    def __init__(self):
        self._wheels = None
        self._color = None
        self._engine = None

    def set_color(self, color):
        self._color = color

    def set_wheels(self, wheels):
        self._wheels = wheels

    def set_engine(self, engine):
        self._engine = engine


class CarBuilder:
    def buildView(self):
        pass
    def getResult(self):
        pass


class RedCar(CarBuilder):

    def __init__(self):
        self.car = Car()

    def buildView(self):
        self.car.set_color('red')
        self.car.set_wheels(4)
        self.car.set_engine('1000 CC')

    def getResult(self):
        return self.car


class BlueCar(CarBuilder):

    def __init__(self):
        self.car = Car()

    def buildView(self):
        self.car.set_color('blue')
        self.car.set_wheels(4)
        self.car.set_engine('1500 CC')

    def getResult(self):
        return self.car


class CarBuilderDirector:
    def __init__(self, builder):
        self._builder = builder

    def get_car(self):
        self._builder.buildView()
        return self._builder.getResult()


if __name__ == '__main__':
    red_car_builder = RedCar()
    red_car_builder_director = CarBuilderDirector(red_car_builder)
    red_car = red_car_builder_director.get_car()

    blue_car_builder = BlueCar()
    blue_car_builder_director = CarBuilderDirector(blue_car_builder)
    blue_car = blue_car_builder_director.get_car()

    print red_car
    print blue_car

