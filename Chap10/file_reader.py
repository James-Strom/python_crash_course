#Example openign the file directly
# with open('text_folder/pi_digits.txt') as file_object:
# 	contents = file_object.read()
# print(contents.rstrip())

#Using file Path
file_path = 'text_folder/pi_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
print(contents.rstrip())

#Reading specific line
filename = 'text_folder/pi_digits.txt'
with open(file_path) as file_object:
	for line in file_object:
		print(line)