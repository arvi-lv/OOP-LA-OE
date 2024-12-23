class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"Name: {self.name} \nAge: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

tobey = Tobey("Tobey", 23, "Spiderman")
andrew = Andrew("Andrew", 19, "The Amazing-Spiderman")
tom = Tom("Tom", 25, "Spiderman: No Way Home")

print(f"{tobey.name} is the lead in {tobey.movieTitle}.")
print(f"{andrew.name} is the lead in {andrew.movieTitle}.")
print(f"{tom.name} is the lead in {tom.movieTitle}.")