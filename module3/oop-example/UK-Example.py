from datetime import date

class Animal:
    #constructor
    def __init__(self, name, birth_year, birth_month, birth_day, weight):
        self.name = name
        self.birthdate = date(birth_year, birth_month, birth_day)
        self.weight = weight

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def details(self):
        print(f"{self.name} is {self.calculate_age()} years old today!")

class Goat(Animal):
    def __init__(self, name, birth_year, birth_month, birth_day, weight, breed):
        super().__init__(name, birth_year, birth_month, birth_day, weight)
        self.breed = breed

    def details(self):
        print(f"{self.name} is {self.calculate_age()} years old today! He is a {self.breed}.")


bessy = Animal("Bessy", 2010, 4, 1, 900)


cat_luis = Animal("Luis", 2015, 2, 15, 10)

print(f"hello {bessy.name}")
print(f"Cat Luis's name is {cat_luis.name}. His birthdate is {cat_luis.birthdate}")

print(f"Cat Luis's name is {cat_luis.name}. His birthdate is {cat_luis.birthdate}. He is {cat_luis.calculate_age()} years old.")

billy = Goat("Billy", 2000, 12, 25, 100, "Boahr")
print(f"Billy's name is {billy.name}. His birthdate is {billy.birthdate}. He is {billy.calculate_age()} years old. He is a {billy.breed}")
billy.details()
bessy.details()