#8-1
def display_messages():
	print("I am learning about functions in the Python language.")
display_messages()

#8-2
def favourite_book(title):
	print(f"One of my favourite books is {title}")

favourite_book('Harry Potter')

#8-3
def make_shirt(size, text):
	print(f"Your shirt size is {size.title()} and you wish to display the message: {text}")

make_shirt('small', 'I love Python')
make_shirt(text='I love JavaScript', size='large')

#8-4
def make_shirt(text, size = 'large'):
	print(f"Your shirt size is {size.title()} and you wish to display the message: {text}")

make_shirt('I love python')

def make_shirt(size, text= 'I love python'):
	print(f"Your shirt size is {size.title()} and you wish to display the message: {text}")

make_shirt('medium')
make_shirt('large')
make_shirt('x-large', 'Java for the win!')

#8-5
def describe_city(city, country='South Africa'):
	print(f"{city.title()} is in {country.title()}")
describe_city('durban')
describe_city('cape town')
describe_city('cairo', 'egypt')

#8-6dgfgdf
def city_country(city, country):

	describe_city = f"'{city.title()}, {country.title()}'"
	print(describe_city)
city_country('durban', 'south africa')

#8-7