# print
print(10+10)
print()

print("welcome to pythonlife")

# addition operation
num_1 = 20
num_2 = 30
result = num_1+num_2
print(result)
'''
 above code is used to perform addition operation 
 num_1 is a variable it contains a value 20
 num_2 is a variable it contains a value 30
 later, in next line performed addition operation byb using + operator
 result has been displayed by using print statement
 
'''
# variable creation
age = 45
print(id(age))

product_cost = 2000
print(id(product_cost))

_employee_id = 456
print(_employee_id)

employee_1_salary = 250000
print(employee_1_salary)

name = "aruna"
Name = "saanvika"
NAME = "anand"
print(id(name))
print(id(Name))
print(id(NAME))

# camel case
studentName = "annareddy"
print(studentName)

# snake_case
student_name = "padmavathi"
print(student_name)

# pascal case
StudentName = "ahalya"
print(StudentName)

product_cost = -564738
print(product_cost)
print(type(product_cost))

height = -5.876
print(height)
print(type(height))

# string
sentence = 'welcome to pythonlife 7 O clock'
print((sentence))
print(type(sentence))
sentence_2 = "welcome to pythonlife 7 O' clock"
print(sentence_2)
print(type(sentence_2))
sentence_3 = ''' welcome to pythonlife '''
print(sentence_3)
print(type(sentence_3))

# type conversion
product_cost = 2000
print(product_cost)
print(type(product_cost))

product_cost = 2000
float_conversion = float(product_cost)
print(float_conversion)               #int---->float
print(type(float_conversion))

kilometers = 1.25
int_conversion = int(kilometers)
print(int_conversion)                 #float--->int
print(type(int_conversion))

# str--->int
employee_salary = "250000050"
print(employee_salary)
print(type(employee_salary))
int_conversion = int(employee_salary)
print(type(int_conversion))

# str---->float
height = "5.7"
print(type(height))
float_conversion = float(height)
print(float_conversion)
print(type(float_conversion))

num_1 = int(input("enter number1:"))
num_2 = int(input("enter number2:"))
result = num_1 + num_2
print(result)

first_name = "350"
last_name = "20"
print(first_name + last_name)

num_1 = 25
num_2 = 25.50
print(num_1 + num_2)

school_name = "gmr"
a = 45000
mail_id = "padmatunga12@gmail.com"
print("pythonlife")


# LIST
sample_list = [25,5.7,"welcome to pythonlife",(35,15.7,"sample"),[1,2,3],{2,4,5}]
print(sample_list)
print(id(sample_list))
print(type(sample_list))
sample_list.append("python course")
print(sample_list)
print(id(sample_list))

# TUPLES
voter_id = (35,15.75,"pythonlife",[1,2,3,5.7],(5.7,25,35,"python"),{1,2,3})
print(voter_id)
print(type(voter_id))
voter_id.append("sample")
print(voter_id)

# SET
sample_set = {35,425,156.78,"charan","kiran","venkat","reddy",25,(1,2,3,4),{1,2,3}}
print(sample_set)
print(type(sample_set))

# DICTIONARY
sample_dict = {"user1":"user@123","user2":"user@123","user3":"user@123"}
print(sample_dict)
print(type(sample_dict))
