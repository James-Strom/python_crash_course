#3-1
names = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#3-2
print(f"Hello {names[0]}")
print(f"Hello {names[1]}")
print(f"Hello {names[2]}")
print(f"Hello {names[3]}")
print(f"Hello {names[4]}")

#3-3
cars = ['BMW', 'Mercedes', 'Ford', 'Audi', 'Lambo']
print(f'I would like to own a {cars[0]}')
print(f'I would like to own a {cars[1]}')
print(f'I would like to own a {cars[2]}')
print(f'I would like to own a {cars[3]}')
print(f'I would like to own a {cars[4]}')

#3-4
guest_list = ['MLK', 'Nelson Mandela', 'Cristano Ronaldo', 'Roger Federer']
print(f"I would like to in invite you, {guest_list[0]} for dinner")
print(f"I would like to in invite you, {guest_list[1]} for dinner")
print(f"I would like to in invite you, {guest_list[2]} for dinner")
print(f"I would like to in invite you, {guest_list[3]} for dinner")

#3-5
new_list = guest_list.pop(2)
guest_list.append('alexander the great')
print(f"I am sorry {new_list} that you cannot make the dinner")
print(f"You {guest_list[0].title()} are invited to dinner at my place.")
print(f"You {guest_list[1].title()} are invited to dinner at my place.")
print(f"You {guest_list[2].title()} are invited to dinner at my place.")
print(f"You {guest_list[3].title()} are invited to dinner at my place.")

#3-6
guest_list.insert(0, 'Adugustus Caesar')
guest_list.append('Julius Caesar')
guest_list.insert(3, 'Genghis Khan')
print(f"{guest_list[0].title()} you are invited tonight for late lunch")
print(f"{guest_list[1].title()} you are invited tonight for late lunch")
print(f"{guest_list[2].title()} you are invited tonight for late lunch")
print(f"{guest_list[3].title()} you are invited tonight for late lunch")
print(f"{guest_list[4].title()} you are invited tonight for late lunch")
print(f"{guest_list[5].title()} you are invited tonight for late lunch")
print(f"{guest_list[6].title()} you are invited tonight for late lunch")

#3-7

print(f"I'm sorry {guest_list.pop(2)} there is only room for 2 guests")
print(f"I'm sorry {guest_list.pop(2)} there is only room for 2 guests")
print(f"I'm sorry {guest_list.pop(2)} there is only room for 2 guests")
print(f"I'm sorry {guest_list.pop(2)} there is only room for 2 guests")
print(f"I'm sorry {guest_list.pop(2)} there is only room for 2 guests")
print(f"{guest_list[0].title()} you are invited tonight for late lunch")
print(f"{guest_list[1].title()} you are invited tonight for late lunch")

#3-8
places = ['rome', 'paris', 'oslo', 'new york', 'sydney']
print(places)
print(sorted(places))
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3-9
print(f"There are {len(guest_list)} coming to dinner.")

#3-11
#print(f"There are {len(uest_list)} coming to dinner.")
print(f"There are {len(guest_list)} coming to dinner.")