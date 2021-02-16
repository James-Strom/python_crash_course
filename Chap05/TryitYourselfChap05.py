#5-1
num = 20
value = (3*4)
print(f"\n{value} which is not equal to {num}")
print(num==value)
value = (3*5)
print(f"\n{value} which is not equal to {num}")
print(num==value)
value = (4*5)
print(f"\n{value} which is equal to {num}")
print(num==value)
value = (5*6)
print(f"\n{value} which is not equal to {num}")
print(num==value)
value = (12+8)
print(f"\n{value} which is equal to {num}")
print(num==value)
value = (40/2)
print(f"\n{value} which is equal to {num}")
print(num==value)
value = (3*4+6)
print(f"\n{value} which is not equal to {num}")
print(num==value)
value = (3*4+8)
print(f"\n{value} which is equal to {num}")
print(num==value)
value = (3*4)
print(f"\n{value} which is not equal to {num}")
print(num==value)
value = (2**3+2*6)
print(f"\n{value} which is equal to {num}")
print(num==value)

#5-2
#inequality
favourite_team = 'man utd'
if favourite_team != 'Liverpool':
	print("\nGlory glory Man Utd!")
	print(favourite_team!='Liverpool')
#equality
num=10
print(num==10)

value = (2*5)
print(f"\n{value} which is equal to {num}")
print(num==value)

value = (5*6)
print(f"\n{value} which is not equal to {num}")
print(num==value)

#greater than
age = 25
print(age)
print(age<30)

#less than
print(age>10)

#lower()
car = 'BMW'
print(car.lower())

#5-3
#pass
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
	print("\nYou have earned 5 points")

#fail
if 'orange' in alien_color:
	print("\nYou have earned 5 points")

#5-4
#if
alien_color = 'green'
if 'green' in alien_color:
	print("\nYou have earned 5 points")
else :
	print("\nYou have earned 10 points")
#else
alien_color = 'orange'
if 'green' in alien_color:
	print("\nYou have earned 5 points")
else :
	print("\nYou have earned 10 points")

#5-5
#green
alien_color = 'green'
if 'green' in alien_color:
	print('\nYou have earned 5 points.')
elif 'yellow' in alien_color:
	print('\nYou have earned 10 points')
elif 'red' in alien_color:
	print('\nYou have earned 15 points')
else:
	print('\nYou have earned 0 points.')
#yellow
alien_color = 'yellow'
if 'green' in alien_color:
	print('\nYou have earned 5 points.')
elif 'yellow' in alien_color:
	print('\nYou have earned 10 points')
elif 'red' in alien_color:
	print('\nYou have earned 15 points')
else:
	print('\nYou have earned 0 points.')
#red
alien_color = 'red'
if 'green' in alien_color:
	print('\nYou have earned 5 points.')
elif 'yellow' in alien_color:
	print('\nYou have earned 10 points')
elif 'red' in alien_color:
	print('\nYou have earned 15 points')
else:
	print('\nYou have earned 0 points.')

#5-6
age = 64
if age < 2:
	print('\nYou are a baby')
elif age >=2 and age<4:
	print('\nYou are a toddler')
elif age >=4 and age<13:
	print('\nYou are a kid')
elif age >=13 and age<20:
	print('\nYou are a teenager')
elif age >=20 and age<65:
	print('\nYou are a adult')
elif age >=65:
	print('\nYou are a elder')

#5-7
favourite_fruits = ['banana', 'orange', 'grapes']
if 'banana' in favourite_fruits:
	print("You like bananas.")
if 'orange' in favourite_fruits:
	print("You like oranges.")
if 'grapes' in favourite_fruits:
	print("You like grapes.")
if 'berry' in favourite_fruits:
	print("You like berries.")
if 'apple' in favourite_fruits:
	print("you like apples.")

#5-8
usernames = ['admin', 'abba', 'cddc', 'effe', 'ghhg']
user ='abba'
if user is 'admin':
	print("Hello admin, would you like a status report?")
if user in usernames :
	print(f"Hello {user} welcome back!")
#5-9
if usernames == []:
	print("we need to find users!!")

#5-10
current_users = ['john', 'james', 'alex', 'jem', 'chris']
new_users = ['sven', 'mark', 'tania', 'nils', 'james']
for new_user in new_users:
	if new_user in current_users:
		print(f"{new_user} is not available.")
	if new_user not in current_users:
		print(f"{new_user} is available")

#5-11(have not added range)
num = 2
if num == 1:
	print(f"{num}st")
if num == 2:
	print(f"{num}nd")
if num == 3:
	print(f"{num}rd")
if num > 3:
	print(f"{num}th") 

#5-12
#Review styling

#5-13