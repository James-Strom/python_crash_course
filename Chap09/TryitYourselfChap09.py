# 9-1, 9-2
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
    
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open!")

# nona_lina = Restaurant("Nona Lina", "Pizza and Pasta")
# hudsons = Restaurant("Hudsons", "Hamburger")
# steak_house = Restaurant("Steak House", "steak")
# hudsons.open_restaurant()
# nona_lina.describe_restaurant()
# hudsons.describe_restaurant()
# steak_house.describe_restaurant()

# 9-3
# class Users:
    # def __init__(self,first_name,last_name,email):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email

    # def describe_user(self):
    #     print(f"First name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\n")

    # def greet_user(self):
    #     print(f"Hello {self.first_name}.\nWelcome back!!")

# james = Users("James", "Stromnes", "js@CC.com")
# mark = Users("Mark", "Stromnes", "ms@CC.com")
# sven = Users("Sven", "Stromnes", "ss@CC.com")
# nils = Users("Nils", "Stromnes", "ns@CC.com")

# james.greet_user()
# mark.describe_user()
# sven.describe_user()
# nils.describe_user()


# 9-4
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
    
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open!")

#     def set_number_served(self, num):
#         self.number_served = num

#     def increment_number_served(self, increment):
#         self.number_served += increment

# nona_lina = Restaurant("Nona Lina", "Pizza and Pasta")
# print(nona_lina.number_served)
# nona_lina.number_served = 21
# print(nona_lina.number_served)
# nona_lina.set_number_served(42)
# print(nona_lina.number_served)
# nona_lina.increment_number_served(8)
# print(nona_lina.number_served)

# 9-5
class Users:
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\n")

    def greet_user(self):
        print(f"Hello {self.first_name}.\nWelcome back!!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# james = Users("James", "Stromnes", "js@CC.com", "1234")
# james.increment_login_attempts()	
# print(james.login_attempts)
# james.increment_login_attempts()	
# print(james.login_attempts)
# james.increment_login_attempts()	
# print(james.login_attempts)
# james.increment_login_attempts()	
# print(james.login_attempts)
# james.increment_login_attempts()	
# print(james.login_attempts)
# james.increment_login_attempts()	
# print(james.login_attempts)
# james.reset_login_attempts()
# print(james.login_attempts)

# 9-6(9.1 must be uncommented for this to work)
# class Ice_cream_stand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.icecream_flavours = ["Strawberry","Vanilla","Bar one"]



#     def display_icecream_flavours(self):
#         print(self.icecream_flavours)

# creamery = Ice_cream_stand("Creamery","Ice Cream")
# creamery.display_icecream_flavours()


# 9-7 (9-5 must be uncommented)
# class Admin(Users):		
#     def __init__(self, first_name, last_name, email, password):
#         super().__init__(first_name, last_name, email, password)
#         self.privileges = ["can add post", "can delete post", "can ban user"]


#     def show_privileges(self):
#         print(self.privileges)

# james = Admin('James', 'Stromnes', 'js@CC.com', '1234')
# james.show_privileges()

# 9-8 (9-5 must be uncommented)

class Admin(Users):		
	def __init__(self, first_name, last_name, email, password):
		super().__init__(first_name, last_name, email, password)
		self.privileges = Privileges()

	

class Privileges:
	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		print(self.privileges)	


# james = Admin('James', 'Stromnes', 'js@CC.com', '1234')
# james.privileges.show_privileges()

# 9-9
# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
        
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
        
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class Battery:
#     """A simple attempt to model a battery for an electric car."""
    
#     def __init__(self, battery_size=75):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 75:
#                 range = 260
#         elif self.battery_size == 100:
#                 range = 315
            
#         print(f"This car can go about {range} miles on a full charge.")

#     def upgrade_battery(self):
#         if self.battery_size != 100:
#             self.battery_size = 100

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
    
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()

# 9-13
# from random import randint

# class Die:
#     def __init__(self,sides):
#         self.sides = sides

#     def roll_die(self):
#         return randint(1, self.sides)

# six = Die(6)
# ten = Die(10)
# twen = Die(20)

# print(six.roll_die())
# print(six.roll_die())
# print(six.roll_die())
# print(six.roll_die())
# print(six.roll_die())
# print(six.roll_die())
# print(six.roll_die())
# print(six.roll_die())
# print(six.roll_die())
# print(f"{six.roll_die()} last 6 die\n")

# print(ten.roll_die())
# print(ten.roll_die())
# print(ten.roll_die())
# print(ten.roll_die())
# print(ten.roll_die())
# print(ten.roll_die())
# print(ten.roll_die())
# print(ten.roll_die())
# print(ten.roll_die())
# print(f"{ten.roll_die()} last 10 die\n")

# print(twen.roll_die())
# print(twen.roll_die())
# print(twen.roll_die())
# print(twen.roll_die())
# print(twen.roll_die())
# print(twen.roll_die())
# print(twen.roll_die())
# print(twen.roll_die())
# print(twen.roll_die())
# print(f"{twen.roll_die()} last 20 die\n")

# 9-14(incomplete)
from random import choices

lotto_list =['a','b','c','d','e','1','2','3','4','5','6','7','8','9','10']
lotto_nums = []
my_nums = ['b','1','2','6']
lotto_num = 0

while lotto_num < 4:
    lotto_nums.append(choice(lotto_list)):
        lotto_num +=1
    return

if lotto_nums == my_nums:
    print("I have won!!")
else:
    print(f"Lotto numbers were: {lotto_nums}\n")
    print(f"My numbers were: {my_nums}")


# 9-15
# 9-16
