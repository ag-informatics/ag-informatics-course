### WRITE THIS CODE FIRST in a NEW FILE
from datetime import date

#look for help using
# help(date)

#indentation matters
#note the use of the colon
#note the use of "self"
#order within the function doesn't matter
#order when passing into the function matters, 
#hence documentation matters


#LETS TRY TO CREATE A MORE REUSABLE ANIMAL
class Animal:

	#constructor method allows you to create a class
	def __init__(self, name, birth_year, birth_month, birth_day, weight):
		self.name = name
		self.birthdate = date(birth_year, birth_month, birth_day) #uses the date library to create a formatted date
		self.weight = weight

	##LATER: come write a method
	#provide a calculated output without revealing the details of this object
	def calculate_age(self):
		today = date.today()
		age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
		return age

	#print the details
	def details(self):
		print(f"{self.name} is {self.calculate_age()} years old today!")


# DEMO USING THE ANIMAL
bessy = Animal("Bessy", 2010, 4, 1, 200)
print(f"hello {bessy.name}")


#EXAMPLE STUB CLASS
class Dodo(Animal):
	pass


# GOAT AS AN EXAMPLE OF INHERITANCE
# CREATE A CHILD CLASS
class Goat(Animal):
	def __init__(self, name, birth_year, birth_month, birth_day, weight, breed):
		super().__init__(name, birth_year, birth_month, birth_day, weight)

		self.breed = breed
		goat_secret_name = "secret goaty goat"
		self.goat_secret_name = "secret goaty goat"


#DEMO GOAT OBJECT
# access goat secret name and explain why that's bad.
sunny = Goat("Sunny", 2009, 4, 1, 20, "highland")
sunny.details()
print(sunny.goat_secret_name)


# COW is an example of POLYMORPHISM - overriding the prev defined function
class Cow(Animal):
	def __init__(self, name, birth_year, birth_month, birth_day, weight, breed):
		super().__init__(name, birth_year, birth_month, birth_day, weight)
		self.breed = breed

	def details(self):
		print(f"{self.name} is {self.calculate_age()} years old today. She is a {self.breed} weighing {self.weight} pounds.")


### DEMO COW PRINT
bessy = Cow("Bessy", 2010, 4, 1, 200, "Holstein")
bessy.details()



# MAKE EDITS?
# import importlib
# importlib.reload(animals)

#tell them this is dangerous because of variable scopes


# CHICKEN is an example of a more complex class
# class Chicken(Animal):

# 	PURPOSE = ['egg', 'meat']
# 	BREEDS = [
# 		('australorp', 'Australorp'), 
# 		('buckeye', 'Buckeye'), 
# 		('java', 'Java'), 
# 		('sussex', 'Sussex'), 
# 		('brahma', 'Brahma'), 
# 		('other', 'Other'),
# 	]


# 	def __init__(self, name, birth_year, birth_month, birth_day, weight, breed):
# 		super().__init__(self,name, birth_year, birth_month, birth_day, weight)
# 		self.breed = breed
# 		self.PURPOSE 

# 	def details(self):
# 		print(f"{self.name} is {self.calculate_age()} years old today. Breed: {self.breed}")
