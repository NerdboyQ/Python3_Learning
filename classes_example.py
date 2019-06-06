class car:
	make = ""
	model = ""
	year = ""
	color = ""
	def get_the_make(self):
		return self.make
	def get_the_model(self):
		return self.make

car_a = car()
car_a.make = "Chevy"
print(car_a.get_the_make())
print(type(car_a))
print(type(car_a.make))