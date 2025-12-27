# logical errors
num_1 = 10
num_2 = 2
result = num_1 + num_2
print(result)

# syntax errors
for i in "python":
    print(i)
    sample = [1,2,3,4]
    print(sample)

# runtime error
num_3 = int(input("enter number num_3 value"))
num_4 = int(input("enter number num_4 value"))
print(num_3 + num_4)
print(num_3 - num_4)
try:
    print(num_3/num_4)
except:
    print("error occured")
    print(num_3*num_4)
    print(num_3 + num_4)
    print(num_3 - num_4)

# zero division error
num_5 = int(input("enter number num_5 value"))
num_6 = int(input("enter number num_6 value"))
print(num_5 + num_6)
print(num_5 - num_6)
try:
    print(num_5/num_6)
except ZeroDivisionError as e:
    print(e)
    print(num_5*num_6)
    try:
        print(num_5/num_6)
    except Exception as f:
        print(f)
    else:
        print("no error")
    finally:
        print("always execute statement")
        print(num_5 + num_6)
        print(num_5 - num_6)

# file not found error
try:
    file = open("hsbc.txt","r")
    read_data = file.read
    print(read_data)
    file.close()
except FileNotFoundError as c:
    print(c)
else:
    print(f"file is valid")

# index error
try:
    sample1 = [1,2,3,4,5]
    print(sample(6))
except IndexError as d:
    print(d)
else:
    print(f"index is valid")

# key error
try:
    data = {"name":"surya"}
    print(data["age"])
except KeyError as e:
    print(e)
else:
    print(f"key is valid")

# attribute error
try:
    x = 10
    x.append(5)
except AttributeError as f:
    print(f)
else:
    print(f"attribute is valid")

# name error
try:
    print(f)
except NameError as g:
    print(g)
else:
    print("name is valid")

# value error
try:
    x = int(input("enter numeric value"))
except ValueError as a:
    print(a)
else:
    print(f"value is numeric {x}")

# type error
try:
    y = int(input("enter numeric value"))
except TypeError as b:
    print(b)
else:
    print(f"no type error {y}")
    