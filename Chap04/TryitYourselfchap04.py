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
#cubes = list(range(1, 11, **3))
#print(cubes)

#4-9
cubes = []
for cube in range(1, 11):
	cubes.append(cube**3)
print(cubes)