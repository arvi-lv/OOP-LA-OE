class lolHero:
    def __init__(self, name, ability):
        self.__name = name
        self.ability = ability

    def introduce(self, function_name):
        def initial_function(*args, **kwargs):
            print("Introducing--")
            function_name(*args, **kwargs)
        return initial_function

hero = lolHero("Lux", "Light Binding")

@hero.introduce
def hero_intro(name, ability):
    print(f"Name: {name} Ability: {ability}")

hero_intro("Zed", "Nawawala")