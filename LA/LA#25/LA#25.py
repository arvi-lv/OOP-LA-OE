from abc import ABC, abstractmethod

class lolHero(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Garen(lolHero):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

class Lux(lolHero):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

hero1 = Garen("Mordekaiser", "Garen")
hero2 = Lux("Luxanna", "Lux")

print(hero1.alias)
print(hero2.alias)