class heroName():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        print(f"Hero: {self.name} \nRole: {self.role}")

top = heroName("Garen", "Tank")
mid = heroName("Ahri", "Mage")

top.describe()
mid.describe()