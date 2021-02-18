# #7-1
# prompt = "What kind of rental car would you like?"
# name = input(prompt)
# print(f"\nLet me see if I can find you a {name}!")

# #7-2
# prompt = "How many people are in your dinner group?"
# number = int(input(prompt))
# if number > 8 :
# 	print("Please wait for a table.")
# else :
# 	print("Your table is ready.")

# #7-3
# prompt = "Please choose a number."
# number = int(input(prompt))
# if number % 10 == 0:
# 	print("Your number is a multiple of 10!")
# else:
# 	print("You chose a number.")

#7-4 Was not able to complete task
# available_toppings = ['cheese', 'bacon', 'vegetables', 'chicken', 'pork']
# toppings_list = []

# while available_toppings:
# 	topping_add = available_toppings.pop()
# 	print(f"Adding topping: {topping_add.title()}")
# 	toppings_list.append(topping_add)
# print("\nThe pizza has the following toppings")
# for checkout in toppings_list:
# 	print(checkout.title())

# #7-5
# prompt = "\nEnter your age:"
# age = int(input(prompt))

# if age < 3:
# 	print(f"\nThe ticket is free.")
# elif  age >= 3 and age <= 12:
# 	print(f"\nThe ticket is R10.")
# elif  age > 12:
# 	print(f"\nThe ticket is R25.")

# #7-6
# prompt = "\nEnter your age:"
# age = input(prompt)
# active=True
# while active:
# 	if age == 'quit':
# 		break
# 	elif int(age) < 3:
# 		print(f"\nThe ticket is free.")
# 		break
# 	elif  int(age) >= 3 and int(age) <= 12:
# 		print(f"\nThe ticket is R10.")
# 		break
# 	elif  int(age) > 12:
# 		print(f"\nThe ticket is R25.")
# 		break
# 	else:
# 		active:False

# #7-7
# prompt = "\nEnter your age:"
# age = input(prompt)
# active=True
# while active:
# 	if  int(age) >= 0 or int(age)< 0 :
# 		print("Infinite")
# 	
# #7-8
# sandwich_orders = ['tuna', 'bacon and egg', 'chicken and mayo', 'gatsby']
# sandwich = []

# while sandwich_orders:
# 	selected_sandwich = sandwich_orders.pop()
# 	print(f"Adding  {selected_sandwich.lower()} sandwich")
# 	sandwich.append(selected_sandwich)
# print("\nThe following sandwiches have been made:")
# for sandwich_finish in sandwich:
# 	print(f"{sandwich_finish.title()} sandwich")

# #7-9
# sandwich_orders = ['tuna', 'bacon and egg', 'chicken and mayo', 'gatsby', 'pastarami']
# sandwich= []
# print(sandwich_orders)
# print("Deli has run out of pastrami.")
# while 'pastarami' in sandwich_orders:
# 	sandwich_orders.remove('pastarami')
# print(sandwich_orders)

# while sandwich_orders:
# 	selected_sandwich = sandwich_orders.pop()
# 	print(f"Adding  {selected_sandwich.lower()} sandwich")
# 	sandwich.append(selected_sandwich)
# print("\nThe following sandwiches have been made:")
# for sandwich_finish in sandwich:
# 	print(f"{sandwich_finish.title()} sandwich")

#7-10
responses = {}

polling_active = True

while polling_active:

	name = input("\nWhat is your name? ")
	response = input("What is your dream place to go? ")
	
	responses[name] = response
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	
	if repeat == 'no':
		polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to go to {response}.")

print("\nNames: ")
for name in responses.keys():
	print(f"\t{name}")

print("\nDream destination: ")
for response in responses.values():
	print(f"\t{response}")
