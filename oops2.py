# inheritance
class feature_phone():
    def __init__ (self, brand, model, battery, color):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.color = color
    def make_call (self,number):
        print(f"calling {number} from {self.brand} {self.model}")
    def send_message (self,message,num):
        print(f"sendind {message} from {num}")
class smartphone (feature_phone):
        def camera (self):
            print(f" photo captured")
        def gaming (self):
            print(f"playing gta {self.brand}")
        def browsing (self):
            print(f" internet browsing")
nokia = smartphone("nokia",2025,5000,"black")
nokia.make_call(1234567890)
nokia.send_message("pythonlife",1234567890)
nokia.camera()
nokia.gaming()
nokia.browsing("chrome")

# hirarchical inheritance
class a():
    def parent (self):
        print("this is parent class")
class b(a):
    def child1 (self):
        print("this is  child 1 class")
class c(a):
    def child2 (self):
        print("this is child 2 class")
obj1 = b()
obj1.child()
obj1.parent()
obj2 = c()
obj2.child2()
obj2.parent()

# multilevel inheritance
class gfather():
    def output (self):
        print(f"earned 100cr properties")
class father (gfather):
    def output1 (self):
        print(f" this is father class")
class child (father):
    def output2 (self): 
        print(f"this is child class")
    def sample(self):
        print(f"started ABC company")
obj = child()
obj.output()
obj.output1()
obj.output2()
obj.sample()

# multiple inheritance
class parent1():
    def father (self):
        print(f"this is father class")
class parent2():
    def mother (self):
        print(f"this is mother class")
class child(parent1, parent2):
    def child (self):
        print(f"this is child class")
obj = child()
obj.father()
obj.mother()
obj.child()

# method overloading
class calculator():
    def sample (self,a,b):
        print(a,b)
    def sample (self,a,b,c):
        print(a,b,c)
obj = calculator()
obj.sample(10,20)
obj.sample(10,20,30)

# operator overloading
class calculator():
    def add (self, a = none, b = none, c = none):
        print(a,b,c)
obj = calculator()
obj.add(10,20,30)
obj.add(10,20)
obj.add(10)
obj.add()
obj.add("vasu", "kumar", "palani")
obj.add("raju", "kumar")
obj.add("sample", 123456)
obj.add("ravi")
obj.add()

# method overriding
class gfather():
    def details (self,a):
        print(f"this is gfather class", a)
class father(gfather):
    def details (self,a):
        print(f"this is father class", a)
obj = father()
obj.details("100cr")

# using superkey
class gfather():
    def details (self,a):
        print(f"this is gfather class", a)
class father(gfather):
    def details (self,a):
        print(f"this is father class", a)
        super().details("100cr")
obj = father()
obj.details("100cr")                        
        
        
                          

                                                    
           
                        
               
                                    
    