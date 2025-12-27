# TASK-1
# reverse list
my_list = [10,20,30,40,50,60]
my_list.reverse()
print(my_list)

# TASK-2
# common elements
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,1]
for i in list1:
    if i in list2:
        print(i)

# TASK-3
# unique elements
original_list = [1,2,2,3,4,4,5]
unique_list = []
for i in original_list:
    unique_list.append(i)
    print(unique_list)

# TASK-4
# remove duplicates
duplicated_list = [1,2,2,3,4,4,5]
new_list = []
for i in duplicated_list:
    if i not in new_list:
        new_list.append(i)
        print(new_list)

# TASK-5
# write a python script that concatenates two lists and prints the result
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,4]
print(f"{list1 + list2}")

# TASK-6
# write a python script that repeats a list three times and prints the result
lists = [1,3,4,2,5]
result = lists*3
print(result)

# TASK-7
# write a python script that removes the elements at even indices from a list
lists = [1,2,3,4,5,6,7,8,9]
result_list = []
for index in range(len(lists)):
    if index % 2 != 0:
        result_list.append(lists[index])
        print(result_list) 
# TASK-8
# write a python script that inserts the numbers 10,11,and 12 at the beginning of a list
lists = [1,2,3,4,5]
lists.insert(0,10),
lists.insert(1,11),
lists.insert(2,12),
print(lists)

# TASK-9
# square numbers create a list of squares of numbers from 1 to 10
lists = []
square = [i**2 for i in range(1,11)]
square.append(lists)
print(square)

# TASK-10
# even numbers generate a list of even numbers from 1 to 20
even_numbers = []
for i in range(0,21):
    if i % 2 == 0:
        even_numbers.append(i)
        print(even_numbers)

# TASK-11
# words lengths given a list of words create a list containing the lengths of each word
words = ["apple","banana","pomegranate","grapes"]
result = []
for w in words:
    result.append(len(w))
    print(result)   
