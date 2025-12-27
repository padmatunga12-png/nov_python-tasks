# TASK-1
# write a python program to calculate the area of a rectangle using th given formula:area=length*width
# take the values of length annd width as inputs from the user
length = int(input("please enter length value:"))
width = int(input("given width value please:"))
result = length*width
print(result)

# TASK-2
# write a python program to demonstrate incrementing and decrementing a variable
stu_marks = 55
stu_marks -= 20
product_cost = 2000
product_cost += 500
print(f"result of incrementing value: {product_cost} and the decrementing value: {stu_marks}")

# TASK-3
# write a python program to convert temperature from celsius to fahrenheit
# the formula for conversion is: F = (c*9/5)+32 take the temperature in celsius as input from the user
c = int(input("enter your temperature in celsius:"))
F = (c*9/5)+32
print(f"this is your conversion value from celsius to fahrenheit:{int(F)} degree fahrenheit")

# TASK-4
# write a python program to calculate the simple interest given the principle
# amount,rate,and time(in years). simple interest calculator,take inputs from the user
principle_amount = 10000
rate = 5
time = 2
SI = (principle_amount*rate*time)/100
print(f"The Simple Interest is:{round(SI)}")

# TASK-5
# write a pyhton program to concatenate two strings and display the result.
# the strings should be taken from the user
item_1 = input("enter your first item:")
item_2 = input("enter your second item:")
total = item_1 + "" + item_2
print(total)

# TASK-6
# write a pyhton program to convert a distance from kilometers to miles
kilometer = 100
result = kilometer*0.621371
print(f"conversion of kms to mile is: {result}")

# TASK-7
# create a program that takes user input for their name and age
# use formatted string to print a message welcomin the user name and age
name = input("please enter your name:")
age = int(input("enter your age:")) 
print(f"welcome mam your name is {name} and ypur age is {age}")

# TASK-8
# create a list called numbers that contains integers from 1 to 10
# check if the number 5 is in the list
# check if the number 15 is not in the list
list = [1,2,3,4,5,6,7,8,9,10] 
print(5 in list)
print(15 not in list)
