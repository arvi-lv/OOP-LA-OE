class Champion:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name}! {self.name} and deals {self.attack_power} damage. {target.name} has {target.health} health left.")
    
    def defend(self, attacker):
        dmg_taken = attacker.attack_power * 0.9
        self.health -= dmg_taken
        print(f"{self.name} defends against {attacker.name}. Health is now {self.health}.")

class Garen(Champion):
    def special_move(self, target):
        target.health -= 80
        print(f"{self.name} uses Demacian Justice! {target.name} loses 80 health.")

class Lux(Champion):
    def special_move(self, target):
        target.health -= 100
        print(f"{self.name} casts Final Spark! {target.name} loses 100 health.")

class Ashe(Champion):
    def special_move(self, target):
        target.health -= self.attack_power * 1.5
        print(f"{self.name} fires an Enchanted Crystal Arrow! {target.name} loses {self.attack_power * 1.5} health.")

class Dragon(Champion):
    def special_move(self, target):
        self.health += 50
        print(f"{self.name} roars and regains 50 health!")

garen = Garen("Garen", 120, 25)
lux = Lux("Lux", 80, 20)
ashe = Ashe("Ashe", 75, 15)
dragon = Dragon("Dragon", 300, 35)

champions = [garen, lux, ashe]

while True:
    for attacker in champions:
        attacker.attack(dragon)
        attacker.special_move(dragon)
        dragon.defend(attacker)
        if dragon.health <= 0:
            print("The Dragon has been slain! Victory is ours!")
            break
    
    if dragon.health <= 0:
        break

    for defender in champions:
        dragon.attack(defender)
        dragon.special_move(defender)
        defender.defend(dragon)
        if defender.health <= 0:
            print(f"Oh no! {defender.name} has fallen!")
            champions.remove(defender)
    
    if not champions:
        print("The Dragon wins!")
        break