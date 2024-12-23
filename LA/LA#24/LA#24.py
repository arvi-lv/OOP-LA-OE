from abc import ABC, abstractmethod

class lolHero(ABC):
    @abstractmethod
    def attack(self):
        pass

class Fighter(lolHero):
    def attack(self):
        print("Unleashes a powerful melee strike!")

class Sorcerer(lolHero):
    def attack(self):
        print("Casts a devastating spell!")

class Marksman(lolHero):
    def attack(self):
        print("Fires a precise shot!")

class Support(lolHero):
    def attack(self):
        print("Heals an ally with a supportive spell!")

garen = Fighter()
annie = Sorcerer()
jax = Marksman()
lulu = Support()

garen.attack()
annie.attack()
jax.attack()
lulu.attack()
