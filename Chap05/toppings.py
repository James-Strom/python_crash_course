#Toppings if statement
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

#Using Elif statement
requested_toppings = ['cheese', 'bacon', 'pepperoni']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
else:
	print("No extra toppings")

print("\nFinished making your pizza!")

#using if statement with list
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#empty list
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

#Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
		
print("\nFinished making your pizza!")