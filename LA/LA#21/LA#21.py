class SinigangNaBaboy:
    def __init__(self, pork, tamarind, water, vegetables):
        self.pork = pork
        self._tamarind = tamarind
        self.__water = water
        self.__vegetables = vegetables
        
    def __str__(self):
        return f"My Sinigang na Baboy has ingredients of {self.pork}, {self._tamarind}, {self.__water}, and {self.__vegetables}."
    
    def maasimBa(self):
        return self._tamarind
       
    def i_set_tamay(self, bagong_tamarind):
        self._tamarind = bagong_tamarind

sinigang = SinigangNaBaboy("Pork belly", "Tamarind paste", "Marami", "Radish")
sinigang.i_set_tamay("fresh tamarind")
print(sinigang.maasimBa())