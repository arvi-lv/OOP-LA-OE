class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.atck_power = attack_power

    def attack(self, target):
        target.health -= self.atck_power
        print(f"{self.name} attacked {target.name} for {self.atck_power} damage!")
        print(f"{target.name} deals {self.name} damage.")
        print(f"{target.name} now has only {target.health} health.")
       
    def heal(self, amount):
        self.health += amount
       
mage = Player("Veigar", 100, 10)
adc = Player("Varus", 100, 20)

while mage.health > 0 and adc.health > 0:
   
    mage.attack(adc)
    if adc.health <= 0:
        print(f"{mage.name} wins!")
        break
   
    adc.attack(mage)
    if mage.health <= 0:
        print(f"{adc.name} wins!\n")
        break
       

mage.heal(100)
print("------------------------------------------------")
print(f"{mage.name} restores health and now has {mage.health} again.")