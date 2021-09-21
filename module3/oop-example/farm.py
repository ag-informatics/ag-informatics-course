from datetime import date

class Animal:

	#constructor method allows you to create a class
	def __init__(self, name, birth_year, birth_month, birth_day, weight):
		self.name = name
		self.birthdate = date(birth_year, birth_month, birth_day)
		self.weight = weight

	#change details within the class
	def change_name(self, new_name):
		name = new_name

	#provide a calculated output without revealing the details of this object
	def calculate_age(self):
		today = date.today()
		age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
		return age

	def details(self):
		print(f"{self.name} is {self.calculate_age()} years old today!")

class Goat(Animal):
	def __init__(self, name, birth_year, birth_month, birth_day, weight):
		super().__init__(name, birth_year, birth_month, birth_day, weight)
		#goat_secret_name = "secret goaty goat"
		#self.goat_secret_name = "secret goaty goat"

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

	def details(self):
		print(f"{self.name} is {self.calculate_age()} years old today. Breed: {self.breed}")


sunny = Goat("Sunny", 2009, 4, 1, 20)
sunny.details()
#print(sunny.goat_secret_name)

bessy = Cow("Bessy", 2010, 4, 1, 200, "Holstein")
bessy.details()

clucky = Chicken("Clucky", 2019, 6, 1, 5, "Australorp")
clucky.details()


