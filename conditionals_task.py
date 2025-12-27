# TASK-1
# vowel checker
input_value = input("enter your word:")
vowels = "aeiouAEIOU"
if input_value in vowels:
    print("yes you entered a vowel")
else:
    print("invalid entry this is not a vowel")
    
# TASK-2
user_age = int(input("enter your age:"))
if user_age >=0 and user_age < 13:
    print("he is a child")
elif user_age >=13 and user_age <=17:
    print("he is a teenager")
elif user_age >=18 and user_age <=64:
    print("he is adult")
elif user_age >=65:
    print("he is a senior")
else:
    print("invalid entry")
    
# TASK-3
value = int(input("enter ypur number:"))
if value >0:
    print("this is a positive value")
elif value <0:
    print("this is negative value")
else:
    print("this is zero")
    
# TASK-4
# leap year checker progarm
year = int(input("enter a year:"))
if ("year % 4 == 0 and year % 100 ! = 0") or ("year % 400 == 0"):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT Leap Year")

# TASK-5
num_1 = int(input("enter your first integer:"))
num_2 = int(input("enter your second integer:"))
operator = input("enter your operator in (+,-,*,/):")
if operator == "+":
    result = num_1 + num_2
    print(result)
elif operator == "-":
    result1 = num_1 - num_2 
    print(result1)
elif operator == "*":
    result2 = num_1*num_2
    print(result2)
elif operator == "/":
    result3 = num_1/num_2
    print(result3)
else:
    print("invalid operator")

# TASK-6
x = int(input("enter your number:"))
result = "result_is_even" if x % 2 == 0 else "result_is_odd" 
print("result")

# TASK-7
# discount calculator program
original_price = float(input("enter the original price:"))
discount_percentage = float(input("enter the discount_percentage:"))
discount_amount = (discount_percentage/100)*original_price
final_price = original_price - discount_amount
print(f"original price: {original_price}")
print(f"discount percentage: {discount_percentage}%")
print(f"discount amount:{discount_amount}")
print(f"final price after discount:{final_price}")

# TASK-8
# BMI calculator program
weight = float(input("enter your weight in kilograms:"))
height = float(input("enter your height in meters:"))
bmi = weight/(height**2)
print("your BMI is:", bmi)
if bmi < 18.5:
    print("you are underweight")
elif 18.5 <= bmi < 24.9:
    print("you are normal weight")
elif 25 <= bmi <29.9:
    print("you are overweight")
else:
    print("you are obese")
                                 
                

        