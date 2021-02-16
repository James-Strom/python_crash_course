#4-1
pizzas = {'pepperoni', 'something meaty', 'meat supreme'}
for pizza in pizzas:
	print(f"I like {pizza} pizza")
print("I love pizza!!!")

#4-2
animals = {'dogs', 'cats', 'tortoises'}
for animal in animals:
	print(f"I am alergic to {animals}")
	print(f"{animal} are slow pets")
	print(f"{animal} are awesome.")
print(f"{animal} make great pets!")

#4-3
numbers = list(range(1, 21))
print(numbers)

#4-4
nums = list(range(1, 11))
for num in nums:
	print(num)

#4-5
print(min(nums))
print(max(nums))

#4-6
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

#4-7
multiples = []
for value in range(1, 11):
	multiples.append(value*3)
print(multiples)

#4-8
cubes = []
for cube in range(1, 11):
	cubes.append(cube**3)
print(cubes)

#4-9
cubes = [value**3 for value in range(1, 11)]
print(cubes)

#4-10
pizzas = ['pepperoni', 'something meaty', 'meat supreme','chicken','hawaian','margherita']
print(f"The first 3 items are: ")
for pizza in pizzas [:3]:
	print(f"\t{pizza}")
print(f"The middle 3 items are:")
for pizza in pizzas[2:5]:
	print(f"\t{pizza}")
print(f"The last 3 items are:")
for pizza in pizzas[3:]:
	print(f"\t{pizza}")
print("I love pizza!!!")

#4-11
my_pizzas =  ['pepperoni', 'something meaty', 'meat supreme']
friend_pizzas = my_pizzas[:]
my_pizzas.append('chicken')
friend_pizzas.append('hawaian')
print(friend_pizzas)
print(my_pizzas)
print(f"My favorite pizzas are:")
for pizza in my_pizzas:
	print(f"\t{pizza.title()}")
print(f"My friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(f"\t{pizza.title()}")

#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for food in my_foods:
	print(f"\t{food}")

#copying our list
print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(f"\t{food}")

#4-13
buffets = ('chicken', 'salad', 'veg', 'pasta', 'steak')
for buffet in buffets:
	print(buffet)
#buffets.append('juice')
buffets = ('pizza', 'ice cream', 'veg', 'pasta', 'steak')
print("\nNew Buffet")
for buffet in buffets:
	print(buffet)
	
#4-14
#read through PEP 8

#4-15
