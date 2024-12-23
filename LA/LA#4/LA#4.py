class heroName():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"Hero: {self.name} Role: {self.role}"

    def __str__(self):
        return f"Hero: {self.name} Role: {self.role}"

top = heroName("Garen", "Top Lane")
mid = heroName("Ahri", "Mage")

print(top.name)
print(top.role)
print(mid.name)
print(mid.role)
print(mid)
print(top)