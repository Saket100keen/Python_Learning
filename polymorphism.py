#Polymorphisim using duck typing
#Duck typing is a concept in programming where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit inheritance from a particular class. 
#In other words, if an object behaves like a certain type (i.e., it has the necessary methods and properties), it can be treated as that type, regardless of its actual class.

class laptop: #crow
    def build(self): #quacking
        print("laptop is build")

class desktop: #duck
    def build(self): #quacking
        print("desktop is build")

class tablet:#duck
    def open_pdf(self): #it's not quacking
        print("Opening pdf in tablet")

class Alien:
    def code(self, machine : laptop):
        print("Alien is buiding ")
        machine.build()


apple = laptop()
beast = desktop()
lenovo = tablet()
navin = Alien()
navin.code(apple)
navin.code(beast)
navin.code(lenovo)