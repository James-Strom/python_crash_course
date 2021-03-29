# 10-1
#Example opening the file directly
# with open('Chap10/text_folder/learning_python.txt') as file_object:
# 	contents = file_object.read()
# print(contents.rstrip())

# #Using file Path
# file_path = 'Chap10/text_folder/learning_python.txt'
# with open(file_path) as file_object:
# 	contents = file_object.read()
# print(contents.rstrip())

# #Reading specific line
# filename = 'Chap10/text_folder/learning_python.txt'
# with open(file_path) as file_object:
# 	for line in file_object:
# 		print(line)
# 10-2
# with open('text_folder/learning_python.txt') as file_object:
# 	for line in file_object:
# 		string = line.replace('python', 'java')
# 		print(string.rstrip())
# 10-3
# filename = 'Chap10/text_folder/guest.txt'

# name = input("What is your name?")

# with open(filename, 'w') as file_object:
# 	file_object.write(name)
# 10-4
# filename = 'Chap10/text_folder/guest_book.txt'
# name = ''
# while name != 'q':
# 	name = input("Please enter your name or 'q' to quit: ")
# 	if name != 'q':
# 		with open(filename, 'a') as file_object:
# 			file_object.write(f"{name}\n")
# 			print(f"Welcome {name}")
# 10-5
# filename = 'Chap10/text_folder/reasons.txt'
# reason = ''
# while reason != 'q':
# 	reason = input("Please enter why you love programming or 'q' to quit: ")
# 	if reason != 'q':
# 		with open(filename, 'a') as file_object:
# 			file_object.write(f"{reason}\n")
# 10-6
# num1 = ""
# num2 = ""
# try:
# 	num1 = int(input("Enter a number: "))
# 	num2 = int(input("Enter another number: "))
# 	result = num1 + num2
# 	print(f"Your answer is {result}")
# except ValueError:
# 	print("Please enter a valid number.")

# 10-7
# num1 = ""
# num2 = ""
# while num1 != 0:
# 	try:
# 		num1 = int(input("Enter a number or enter 0 to quit: "))
# 		num2 = int(input("Enter another number: "))
# 		result = num1 + num2
# 		print(f"Your answer is {result}")
# 	except ValueError:
# 		print("Please enter a valid number.")
# 10-8
# filenames = ['Chap10/text_folder/dogs.txt', 'Chap10/text_folder/cats.txt']	

# def read_files(filename):
# 	try:
# 		with open(filename) as fn:
# 			contents = fn.read()
# 	except FileNotFoundError:
# 		print(f"Sorry file not found\n")
# 	else:
# 			print(contents)

# for filename in filenames:
# 	read_files(filename)
# 10-9
filenames = ['Chap10/text_folder/dogs.txt', 'Chap10/text_folder/cats.txt']	

def read_files(filename):
	try:
		with open(filename) as fn:
			contents = fn.read()
	except FileNotFoundError:
		pass
	else:
			print(contents)

for filename in filenames:
	read_files(filename)
