class heroName():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"Hero: {self.name} \nRole: {self.role}"

mid = heroName("Veigar", "Mage")
adc = heroName("Vayne", "AD Carry")

print(mid.name)
print(mid.role)
print(adc.name)
print(adc.role)
print(adc.describe())
print(mid.describe())