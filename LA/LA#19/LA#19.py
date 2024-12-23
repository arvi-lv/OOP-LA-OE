class PritongManacc:
    def __init__(self, manacc, crispyfry):
        self.manacc = manacc
        self.crispyfry = crispyfry

    def __str__(self):
        return f"Pritong Manacc Ingredients: \n{self.manacc}, {self.crispyfry}"

pritong_manacc = PritongManacc("Manacc", "Crispy Fry")
print(pritong_manacc)