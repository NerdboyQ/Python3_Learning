'''
The following code was created to illustrate the use of classes, how to 
create them, and understanding predefined & and custom class types. We use
the pre-defined "type" function to get the class type of different objects. 
'''

#Below we create a new class called "car_class"
class car_class:
	#Here we define the car_class parameters as empty strings to be updated later
	make = ""
	model = ""
	year = ""
	color = ""

	#When 'functions' are included in a class, we refer to them as methods
	#The methods below just return the car class' parameters defined above
	#NOTE: methods need the "self" parameter to be passed in as an argument
	#to reference the class global variables. self refers to the class we are
	#currently in
	def get_the_make(self):
		return self.make
	def get_the_model(self):
		return self.model
	def get_the_year(self):
		return self.year
	def get_the_color(self):
		return self.color

#To use a class, we call it as we would normally call a function with the name
#followed by '()'. Python will recognize it as a class due to its definition.
#When we call a class we call that "instantiating", and instantiating creates
#a new instance of that class that we call an "object" 
car_object_a = car_class()
#below we update this instance of the car_class we created, our new object's, 
#respective parameters we defined previously.   
car_object_a.make = "Chevy"
car_object_a.model = "Impala"
car_object_a.year = "2019"
car_object_a.color = "Green"

#We instantiate a new object below, so we now have two objects (car_object_a & car_object_b)
car_object_b = car_class()
car_object_b.make = "Tesla"
car_object_b.model = "Model X"
car_object_b.year = "2019"
car_object_b.color = "Space Gray"

#NOTE: lists are designated with '[]' and dictionaries are designated with '{}'. 

#Now we create a list of the objects, or the different instances of our car_class
car_list = [car_object_a, car_object_b]

#We then create a dictionary of the different objects. For the values for each key, we use
#the class defined methods to get the specific values we desire.
#NOTE: Dictionaries require keys.
car_dict = {
car_object_a : {"Make" : car_object_a.get_the_make(), "Model" : car_object_a.get_the_model(),"Year" : car_object_a.get_the_year(),"Color" : car_object_a.get_the_color()},
car_object_b : {"Make" : car_object_b.get_the_make(), "Model" : car_object_b.get_the_model(),"Year" : car_object_b.get_the_year(),"Color" : car_object_b.get_the_color()}, 
}

#Now, just for clarity we print the different class types we are using by using the 
#pre-defined python function 'type'
print(type(car_list))
print(type(len(car_list)))
print(type(car_object_b.make))
print(type(car_dict))
print("-"*50)
#Finally we iterate through the list of car_class objects and provide there Model & Color values
for car_instance in car_list:
	print(f"The color of the {car_dict[car_instance]['Model']} is: {car_dict[car_instance]['Color']}\n")

print("-"*50)