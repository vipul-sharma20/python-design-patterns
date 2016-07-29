class SuperHero(object):
    def get_powers(self):
        return self.power

class SuperHeroFactory(object):
    def get_hero(self, target):
        return target()

class _Batman(SuperHero):
    power = "Something"

class _Superman(SuperHero):
    power = "The other thing"

if __name__ == '__main__':
    factory_obj = SuperHeroFactory()
    heroes = [_Batman, _Superman]
    for hero in heroes:
        print factory_obj.get_hero(hero).get_powers()

