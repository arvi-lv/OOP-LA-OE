class AdobongManacc:
    def __init__(self, toyo, manacc, sibuyas):
        self.toyo = toyo
        self.manacc = manacc
        self.sibuyas = sibuyas

    def __str__(self):
        return (f"Ang mga ingredients ng adobong manacc: \n{self.toyo} \n{self.manacc} \n{self.sibuyas}")

adobo = AdobongManacc("Sariwang Hipon", "Maacm na knorr", "Lantang Kangkong")

print(adobo)