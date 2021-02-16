#Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#includes first excludes last
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

#Start list from beginning
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

#Start list from 3rd name on index till end
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

#List states the last 3 on teh index in same order
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())