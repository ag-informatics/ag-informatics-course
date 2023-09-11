### WRITE THIS CODE FIRST in a NEW FILE
from datetime import date

class Animal:

	#LETS TRY TO CREATE A MORE REUSABLE ANIMAL
	#constructor method allows you to create a class
	def __init__(self, name, birth_year, birth_month, birth_day, weight):
		self.name = name
		self.birthdate = date(birth_year, birth_month, birth_day)
		self.weight = weight


	#provide a calculated output without revealing the details of this object
	def calculate_age(self):
		today = date.today()
		age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
		return age

	#print the details
	def details(self):
		print(f"{self.name} is {self.calculate_age()} years old today!")


## DO THIS
## OPEN python shell
## import animals
## then create a single object using the Animal class written below.


## GOAT AS AN EXAMPLE OF INHERITANCE
## CREATE A CHILD CLASS
class Goat(Animal):
	def __init__(self, name, birth_year, birth_month, birth_day, weight):
		super().__init__(name, birth_year, birth_month, birth_day, weight)
		goat_secret_name = "secret goaty goat"
		self.goat_secret_name = "secret goaty goat"


## MAKE EDITS?
## import importlib
# importlib.reload(animals)
# tell them this is dangerous because of variable scopes

# create a goat object
# access goat secret name and explain why that's bad.

## COW is an example of POLYMORPHISM

class Cow(Animal):
	def __init__(self, name, birth_year, birth_month, birth_day, weight, breed):
		super().__init__(name, birth_year, birth_month, birth_day, weight)
		self.breed = breed

	def details(self):
		print(f"{self.name} is {self.calculate_age()} years old today. She is a {self.breed} weighing {self.weight} pounds.")



class Chicken(Animal):

# BREEDS = [
# 	('australorp', 'Australorp'), 
# 	('buckeye', 'Buckeye'), 
# 	('java', 'Java'), 
# 	('sussex', 'Sussex'), 
# 	('brahma', 'Brahma'), 
# 	('other', 'Other'),
# ]

PURPOSE = ['egg', 'meat']

def __init__(self, name, birth_year, birth_month, birth_day, weight, breed):
	super().__init__(name, birth_year, birth_month, birth_day, weight)
	self.breed = breed
	self.PURPOSE 

def details(self):
	print(f"{self.name} is {self.calculate_age()} years old today. Breed: {self.breed}")

sunny = Goat("Sunny", 2009, 4, 1, 20)
sunny.details()
#print(sunny.goat_secret_name)

bessy = Cow("Bessy", 2010, 4, 1, 200, "Holstein")
bessy.details()

clucky = Chicken("Clucky", 2019, 6, 1, 5, "Australorp")
clucky.details()


