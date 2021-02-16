#Checking whether value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

#Checking whether a value is in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user in banned_users:
	print(f"{user.title()}, you can if you wish.")
else:
	print(f"{user.title()}, you can post a response if you wish.")