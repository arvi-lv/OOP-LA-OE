class Wedding:
    def __init__(self, theme, food):
        self.theme = theme
        self.food = food

    def menu(self):
        print("Cake, Chicken, Beef Stew")
        self.__special_dish()

    def __special_dish(self):
        print(f"The theme is {self.theme}.")
        print(f"The special dish is {self.food}.\n")


wedding1 = Wedding("Ang tamis", "Roast Chicken")
wedding2 = Wedding("Ang sarap", "Grilled Salmon")
wedding3 = Wedding("Classico", "Beef Wellington")

wedding1.menu()
wedding2.menu()
wedding3.menu()