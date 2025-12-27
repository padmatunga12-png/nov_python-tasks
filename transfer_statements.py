# TASK-1
# write a python program that takes a list of numbers as input
# numbers = [25,30,20,40,15,25] and prints the sum of the numbers,however if the sum exceeds
# 100,stop adding numbers and print sum exceeded 100
numbers = [25,30,20,40,15,25]
total = 0
for i in numbers:
    total += i
    if total >100:
        print("sum exceeded 100")
        break
    print("total=", total)

# TASK-2
# write a python script that uses a for loop to iterate through numbers from 1 to 600
# print only the odd numbers skipping the even ones using the statement
count = 1
for i in range(1,601):
    count += i
    if i%2!=0:
        print(f"{i}")

# TASK-3
# write a python script that checks if a number is even or odd if the number is even,
# print even if odd do nothing use the pass statement
num = int(input("enter your number:"))
if num%2 == 0:
    print("this is even number")
else:
    pass

# TASK-4
# write a python script that iterates through a list of words if the word is break
# exit the loop using the break statement if the word is skip skip the rest of the code
# for the current iteration using the continue statement for any other word print the word
value = input("enter your work:").split()
for value in value:
    if value == "break":
        print("i am breaking")
        break
    if value == "skip":
        continue
    else:
        print(value)
                     