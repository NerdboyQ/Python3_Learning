def my_function(val):
	max_value = val+11
	while val < max_value:
		if val%2 == 0:
			print(f'even value: {val}')
		else:
			print(f'odd value: {val}')
		val+=1
	val-=1
	return val

global_val = 5
global_val = my_function(global_val)
print(f'print my global {global_val}')