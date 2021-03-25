# #8-1
# def display_messages():
# 	print("I am learning about functions in the Python language.")
# display_messages()

# #8-2
# def favourite_book(title):
# 	print(f"One of my favourite books is {title}")

# favourite_book('Harry Potter')

# #8-3
# def make_shirt(size, text):
# 	print(f"Your shirt size is {size.title()} and you wish to display the message: {text}")

# make_shirt('small', 'I love Python')
# make_shirt(text='I love JavaScript', size='large')

# #8-4
# def make_shirt(text, size = 'large'):
# 	print(f"Your shirt size is {size.title()} and you wish to display the message: {text}")

# make_shirt('I love python')

# def make_shirt(size, text= 'I love python'):
# 	print(f"Your shirt size is {size.title()} and you wish to display the message: {text}")

# make_shirt('medium')
# make_shirt('large')
# make_shirt('x-large', 'Java for the win!')

# #8-5
# def describe_city(city, country='South Africa'):
# 	print(f"{city.title()} is in {country.title()}")
# describe_city('durban')
# describe_city('cape town')
# describe_city('cairo', 'egypt')

# #8-6
# def city_country(city, country):

# 	describe_city = f"'{city.title()}, {country.title()}'"
# 	print(describe_city)
# city_country('durban', 'south africa')

#8-7
# def make_album(artist, album, song_num=None):

# 	musician = {'Artist': artist, 'Album': album}
# 	if song_num:
# 		musician['Number of Songs'] = song_num
# 	return musician

# musician = make_album('Bruno Mars', '24k Magic', 9)
# print(musician)
# musician = make_album('Adele', '25', 11)
# print(musician)
# musician = make_album('Beyonce', 'Lemonade')
# print(musician)

# #8-8
# while True:
# 	print("\nEnter  artist name and album title")
# 	print("(enter 'q' to quit)")
# 	artist = input("Artist: ")
# 	if artist == 'q':
# 		break
# 	album = input("Album title: ")
# 	if album == 'q':
# 		break
# 	musician = make_album(artist, album)
# 	print(musician)

# 8-9
# messages = ['hey', 'howzit', 'sup', 'whatup']

# def show_messages(messages):
# 	for message in messages:
# 		print(message)

# show_messages(messages)

# 8-10
# messages = ['hey', 'howzit', 'sup', 'whatup']
# sent_messages = []

# def send_messages(messages, sent_messages):
# 	while messages:
# 		message = messages.pop()
# 		sent_messages.append(message)

# send_messages(messages, sent_messages)

# print(f"Messages: {messages}")
# print(f"Sent messages:{sent_messages}")

# # 8-11(slice)
# messages = ['hey', 'howzit', 'sup', 'whatup']
# sent_messages = []

# def send_messages(messages, sent_messages):
# 	while messages:
# 		message = messages.pop(0)
# 		sent_messages.append(message)

# send_messages(messages [:], sent_messages)
# print(messages)
# print(sent_messages)

# 8-12
# def make_sandwich(*toppings):
# 	print("Making your sandwich with the following toppings: ")
# 	for topping in toppings:
# 		print(f"- {topping}")
# make_sandwich('chicken', 'mayo')
# print(make_sandwich)
# make_sandwich('bacon', 'egg')
# print(make_sandwich)
# make_sandwich('cheese', 'ham')
# print(make_sandwich)
# 8-13
# def build_profile(first, last, **user_info):
# 	"""Build a dictionary containing everything we know about a user."""
# 	user_info['first_name'] = first
# 	user_info['last_name'] = last
# 	return user_info

	
# user_profile = build_profile('James', 'Stromnes',
# 								field='Programming',
# 								interests='Golf',
# 								favourite_movie =  'Inception')
# print(user_profile)
# 8-14
# def make_car(manufacturer, model,**car_features):
# 	car_features['manufacturer'] = manufacturer
# 	car_features['model'] = model
# 	return car_features
# car = make_car('Ford', 'Fiesta', color ='white', service_package=True)
# print(car)

# 8-16(imported from try_8_16)
import try_8_16
from try_8_16 import make_car
from try_8_16 import make_car as mc
import try_8_16 as t8
from try_8_16 import *