# practice using classes and objects by writing a program to create laptop object
class laptop():
    def __init__ (self, bn, color, size, model, storage, battery):
        self.bn = bn
        self.color = color
        self.size = size 
        self.model = model
        self.storage = storage
        self.battery = battery
    def gaming (self):
            print(f"you are gaming ludo {self.bn}")
    def movies (self,movie,app_name):
            print(f"you are watching movies on {app_name}movie{movie}")
    def listening (self,app,bn):
            print(f"you are listening through {app} in the {bn}")
    def editing (self,app):
            print(f"you are editing in {app}")
    def browsing (self, browser):
            print (f"you are browsing from {browser} on {self.bn}")
acer = laptop("acer_intel", "grey","17", "aspire3", "255gb", "15")
acer.gaming()
acer.movies("kantara", "amazonprime")
acer.listening("youtube","acer")
acer.editing("inshot")
acer.browsing("browser")                     
    
    