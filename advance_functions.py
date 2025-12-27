# TASK-1
# write a python function square_all numbers that takes a list of numbers as input
# and returns a new list containing the square of each number in the input list
# use the map fun with a lambda fun to implement this
list_1 = [23,65,12,32,15]
def square_all(i):
    return list(map(lambda i:i **2,list_1))
squared_numbers = square_all([23,65,12,32,15])
print(squared_numbers)

# TASK-2
# write a python function filter_positive num that takes a list of num as
# input and retutns a new list containing only the positive numbers from the input list
# use the filter fun with a lambda fun to implement this
list_1 = [12,13,14,11,10,15,16,17,18,19]
def filter_positive(i):
    return list(filter(lambda i:i>0,list_1))
input_numbers = [-20,-15,0,15,20]
positive_numbers = filter_positive(input_numbers)
print(positive_numbers)


# TASK-3
# write a python fun calculate_factorial(n) that calculates the factorial of a
# given num n. use the reduce fun with an appropriate lambda fun to implement this
def factorial(n):
    factorial = 1
    for i in range (1,n+1):
        factorial *= i
        return factorial
    n = int(input("enter an integer:"))
    print("factorial of", n, "is",factorial(n))
    from functools import reduce
    def calculate_factorial(n):
        if n == 0 or n == 1:
            return 1
        return reduce(lambda i, n:n*1,range(1,n+1))
    factorial_of_5 = calculate_factorial(5)
    print(factorial_of_5)
    
    # TASK-4
    # write a python fun count_vowels(string) that takes a string as input and 
    # returns the count of vowels in the input string use the reduce fun with an 
    # appropriate lambda fun to implement this
    from functools import reduce
    def count_vowels(string):
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        return reduce(lambda count, char:count + (1 if char in vowels else 0), string,0)
    input_string = "Hello,how are you?"
    vowel_count = sum(1 for char in input_string if char.lower() in "aeiou")
    print(vowel_count)
    