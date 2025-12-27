# TASK-1
# write a python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop
count = 0
for i in range(1,6):
    count += 1
    print(f"{i**2} is square of {i}")

# TASK-2
# write a python program that uses a while loop to print a countdown from 5 to 1
num = 5
while num>=1:
    print(num)
    num -= 1
    
# TASK-3
# write a pyhton program to print the multiplication table for a user specified number using a nested for loop
num = int(input("enter your value:"))
for i in range(1,11):
    print(f"{num} x {i} = {i*3}")

# TASK-4
# write a python program that uses a for loop to find the sum of all even numbers between 0 and 10
for i in range(0,10):
    if i%2 == 0:
        print(i)

# TASK-5
# calculate the sum of all numbers from 1 to a given number
num = int(input("enter your value:"))
total = 0
for i in range(1,num + 1):
    total += i
    print("total=",total)

# TASK-6
# display numbers from a list using loop
list = [10,25,20,14,5]
for i in list:
    print(i)

# TASK-7
# display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)

# TASK-8
# write a python program to print the cube of all numbers from 1 to a given number
num = int(input("enter your value:"))
count = 0
for i in range(1,num):
    count += 1
    print(f"{i**3} is cube of {count}")
                    