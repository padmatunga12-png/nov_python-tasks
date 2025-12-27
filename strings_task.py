# TASK-1
# you are given a string sentence print the characters at even indices
# sentence = "python is amazing"
# sentence = "python is amazing"
even_index_chars = ""
for index in range(len(sentence)):
    if index % 2 == 0:
        even_index_chars += sentence[index]
        print(even_index_chars)

# TASK-2
# you are given a string s replace all spaces in the string with underscores and print the modified string
# s = "python is fun and powerfull"
modified_string = s.replace("","_")
print(modified_string)

# TASK-3
# you are given a string s check if the string contains only digits
# s = "12345"
s = "12345"
if s.isdigit():
    print("the string contains only digits")
else:
    print("the string contains non-digit characters")

# TASK-4
# you are given string s print the string in reverse order
# s = "python is amazing"
reversed_string = s[::-1]
print(reversed_string)

# TASK-5
# you are given a string s capitalize the first letter of each word in the string and print the modified string
# s = "python programming is fun"
s = "python programming is fun"
capitalized_string = s.title()
print(capitalized_string)
    
        