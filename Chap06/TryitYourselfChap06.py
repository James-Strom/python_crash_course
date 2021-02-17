#6-1
person1 = {"firstName":"james", "lastName":"bond", "age":32, "city":"london"}

for key, value in person1.items():
	print(f"Key:{key}")
	print(f"Value: {value}\n")

#6-2
favorite_number = {
	'mark': 6,
	'james': 9,
	'alex': 21,
	'ben': 10,
	'dan': 17,
	}
	
for name, number in favorite_number.items():
	print(f"\n{name.title()}'s favorite number is:")
	print(f"\t{number}")

#6-3
python_glossary = {
	'list:': "collection of items in a particular order.",
	'comprehension:':"combines for loop and new elements into one line.",
	'indentation:': "refers to the spaces at the beginning of a code line.",
	'comments:': "code lines that will not be executed.",
	'tuple:': "is an ordered, and unchangeable, collection.",
	}

for name, glossary in python_glossary.items():
	print(f"\n{name.title()}\n\t{glossary.capitalize()}")

#6-4  
#completed during 6-3
python_glossary = {
	'list:': "collection of items in a particular order.",
	'comprehension:':"combines for loop and new elements into one line.",
	'indentation:': "refers to the spaces at the beginning of a code line.",
	'comments:': "code lines that will not be executed.",
	'tuple:': "is an ordered, and unchangeable, collection.",
	}

for name, glossary in python_glossary.items():
	print(f"\n{name.title()}\n\t{glossary.capitalize()}")

#6-5
country_river = {
	'nile': 'egypt',
	'vaal':'south africa',
	'thames': 'england',
	}
for river, country in country_river.items():
	print(f"\n{river.title()} is in {country.title()}")

#6-6
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
	
for name, languages in favorite_languages.items():
	print(f"\nThenk you {name.title()} for taking the poll.")
	if name not in favorite_languages:
		print(f"\nWould you like to take the poll?")
#6-7
people = {
	'person1' : {
	'firstName':'james', 
	'lastName':'bond', 
	'age':32, 
	'city':'london'
	},

	'person2' : {
	'firstName':'thor', 
	'lastName':'odinson', 
	'age':2500, 
	'city':'asgard'
	},

	'person3' : {
	'firstName':'bruce', 
	'lastName':'wayne', 
	'age':28, 
	'city':'gotham'
	},
}

for person, person_info in people.items():
	full_name = f"{person_info['firstName']} {person_info['lastName']}"
	age = person_info['age']
	city = person_info['city']
	print(f"\nfull_name: {full_name.title()}")
	print(f"age: {age}")
	print(f"city: {city.title()}")

#6-8
pets = {
	'pet_01' : {
	'kind' : 'dog',
	'owner' : 'fred',
	},
	'pet_02' : {
	'kind' : 'cat',
	'owner' : 'kate',
	},
	'pet_03' : {
	'kind' : 'fish',
	'owner' : 'bob',
	},
}

for pet, pet_info in pets.items():
	kind = pet_info['kind']
	owner = pet_info['owner']
	print(f"\nPet kind: {kind.title()}")
	print(f"Owner: {owner.title()}")

#6-9
favourite_places = {
	
	'mark': ['eiffel tower', 'mt everest'],
	'james': ['coliseum', 'machu picchu', 'table mountain'],
	'ben' : ['petra', 'clifton beach'],
}

for name, places in favourite_places.items():
	print(f"\n{name.title()}:")
	for place in places:
		print(f"\t{place.title()}")

#6-10
favorite_number = {
	'mark': [6, 7],
	'james': [9, 10],
	'alex': [21, 13],
	'ben': [10, 14],
	'dan': [17, 10],
	}
	
for name, numbers in favorite_number.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t\t\t\t\t\t\t{number}")

#6-11
cities = {
	'city_01' : {
	'name' : 'london',
	'city_country' : 'england',
	'city_pop' : 8900000,
	'city_fact' : 'capital city',
	},
	'city_02' : {
	'name' : 'paris',
	'city_country' : 'france',
	'city_pop' : 2200000,
	'city_fact' : 'capital city'
	},
	'city_03' : {
	'name' : 'harare',
	'city_country' : 'zimbabwe',
	'city_pop' : 1500000,
	'city_fact' : 'capital city'
	},
}

for city, city_info in cities.items():
	name = city_info['name']
	city_country = city_info['city_country']
	city_pop = city_info['city_pop']
	city_fact = city_info['city_fact']
	
	print(f"\nCity name: {name.title()}")
	print(f"Country: {city_country.title()}")
	print(f"City population: {city_pop}")
	print(f"Fact: {city_fact.capitalize()}")