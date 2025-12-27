#### file methods ####

### read ###
file = open("demo.txt", mode = 'r')
read_data = file.read()
print(read_data)
file.close()

### readline ###
file = open("demo.txt", mode = 'r')
read_data = file.readline()
print(read_data)
file.close()

### readlines ###
file = open("demo.txt", mode = 'r')
read_data = file.readlines()
print(read_data)
file.close()

### write ###
mode = 'a'
file = open("demo.txt", mode = 'a')
write_data = file.write("\nappend operation performed by using mode = 'a'")
file.close()

### write data ###
mode = 'w'
file = open("demo.txt", mode = 'w')
write_data = file.write("welcome to pythonlife write operation")
file.close()

### craeting new file ###
file = open("sample.txt",  mode = 'w')
write_data = file.write("pythonlife write operation")
file.close()

### writelines ###
emp_data = ["annareddy\n","ahalya\n","aruna\n","saanvika"]
file = open("demo123.txt",mode = 'w')
write_data = file.writelines(emp_data)
file.close()

### delete files ###
import os 
os.remove("demo123.txt")
os.remove("pythonlife.txt")
os.remove("sample.txt")
os.remove("sample123.txt")
os.remove("sampledemo.txt")

### rename file ###
import os 
fn = "demo.txt"
nn = "sampledemo.txt"
os.rename(fn,nn)

### handlind the file on desktop ###
file = open("C:\\Users\\Ameen basha\\Desktop\\sample123.txt",mode = 'r')
read_data = file.read()
print(read_data)
file.close()

### creating file on desktop ###
file = open("C:\\Users\\Ameen basha\\Desktop\\sample123.txt",mode = 'a')
write_data = file.write("sample data")
file.close()

### mode(w+) ###
file =  open("pythonlife.txt",mode = 'w+')
write_data = file.write("hi everyone")
print(file.tell())
file.seek(0)
read_data = file.read()
print(read_data)
file.close()

### mode(a+) ###
file = open("demo.txt",mode = 'a+')
write_data = file.write("good morning")
print(file.tell())
file.seek()
read_data = file.read()
print(read_data)
file.close()

### mode(r+) ###
file = open("demo.txt",mode = 'r+')
write_data = file.write("good evening")
print(file.tell())
file.seek(0)
read_data = file.read()
print(read_data)
file.close()


