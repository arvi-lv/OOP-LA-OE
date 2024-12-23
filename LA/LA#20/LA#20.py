class SinigangNaBaboy:
    def __init__(self, pork, tamarind, water, vegetables):
        self.__pork = pork
        self._tamarind = tamarind
        self.__water = water
        self.__vegetables = vegetables
        
    def __str__(self):
        return f"Sinigang na Baboy Recipe: \n{self.__pork}, {self._tamarind}, {self.__water}, and {self.__vegetables}."
    
    def maasimBa(self):
        return self._tamarind

sinigang = SinigangNaBaboy("Pork belly", "Tamarind paste", "Marami", "Radish")
print(sinigang)
print(sinigang.maasimBa())