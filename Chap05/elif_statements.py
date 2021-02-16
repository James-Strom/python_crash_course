#Elif else if statements
# == comparison operator
# 
num = 26

if num<5:
	value = "is to small."
elif num > 5 and num<25:
	value = "should be greater"
elif num == 25:
	value = "is correct!!"
else:
	value = "should be smaller."
print(f"your number is {num} and {value}")