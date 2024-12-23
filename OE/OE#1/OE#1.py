class lol_hero():
    def __init__(self, name, role, dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type

    def __str__(self):
        return f"{self.name} is a {self.role} with {self.dmg_type} damage."

    def describe(self):
        return f"{self.name} is a {self.role} who deals {self.dmg_type} damage."

mm = lol_hero("Jhin", "Marksman", "Physical")
mage = lol_hero("Ahri", "Mage", "Magic")
jungler = lol_hero("Nidalee", "Jungler", "Magic")
tank = lol_hero("Leona", "Tank", "Physical")
supp = lol_hero("Seraphine", "Support", "Magic")

print(f'''
MY TEAM:
{mm.name}
{mm.role}
{mm.dmg_type}
{mm.describe()}

{mage.name}
{mage.role}
{mage.dmg_type}
{mage.describe()}

{jungler.name}
{jungler.role}
{jungler.dmg_type}
{jungler.describe()}

{tank.name}
{tank.role}
{tank.dmg_type}
{tank.describe()}

{supp.name}
{supp.role}
{supp.dmg_type}
{supp.describe()}
''')