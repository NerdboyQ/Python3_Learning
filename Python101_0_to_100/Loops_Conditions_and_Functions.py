'''
The following code was created to illustrate the use of loops that 
have the same functionality, but how the syntax differs between the two.
These loops are contained within functions that we create to be called
as needed. Both functions expect a start value that will be provided by
the user.
'''
#Below is our for loop function based counter
def my_for_loop_function(val):
	#The next two lines are just being used to indicate which function is running
	print("-"*50)
	print("This is my for loop run")
	#Below we set the max value at which our loop will stop execution. This will
	#cause the increase the input value by 10, as the 11th value is our "stop" point
	max_value = val+11
	#This loop's syntax increases the for value from the user provided value to the max_value
	#defined above. The for loop increments by 1 as its default 
	for val in range(val,max_value):
		#The contitional statement below checks if the user's passed in value is currently 
		#even or not. We do this using the % operator, or modulus. This operator returns a
		#zero if dividing value returns a remainder greater than 1 or not; if not the the 
		#dividing the two values results in an even qutient with no remainder. 
		if val%2 == 0:
			print(f'even value: {val}')
		else:
			print(f'odd value: {val}')

	return val

#Below is our while loop function based counter
def my_while_loop_function(val):
	#The next two lines are just being used to indicate which function is running
	print("-"*50)
	print("This is my while loop run")
	#Below we set the max value at which our loop will stop execution. This will
	#cause the increase the input value by 10, as the 11th value is our "stop" point
	max_value = val+11
	#This loop's syntax will run as long as the user provided value is less than the max value
	#assigned above. Because the while loop does not increment that value considered automatically
	#it must be adjust within the while loop. If not the loop will be endless.  
	while val < max_value:
		#The contitional statement below checks if the user's passed in value is currently 
		#even or not. We do this using the % operator, or modulus. This operator returns a
		#zero if dividing value returns a remainder greater than 1 or not; if not the the 
		#dividing the two values results in an even qutient with no remainder. 
		if val%2 == 0:
			print(f'even value: {val}')
		else:
			print(f'odd value: {val}')
		#As stated above, the while loop does not automatically increase the user's provided value
		#it has to be updated "directly" as seen below.
		val+=1
	val-=1
	return val

#The line below uses the built in "input" function that provides a string for the user
#to see, and allows the user to enter a value. 
user_entered_val = input("Please enter the starting value for your counter\n")

#When using the input function, the function will return a string, so it have to be converted
#into an integer value (see below) as the defined functions are expecting integer values.
global_val = int(user_entered_val)
global_val = my_while_loop_function(global_val)
print(f'print my global {global_val}')

global_val = int(user_entered_val)
global_val = my_for_loop_function(global_val)
print(f'print my global {global_val}')