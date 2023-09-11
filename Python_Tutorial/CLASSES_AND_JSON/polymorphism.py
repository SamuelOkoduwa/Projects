# Polymorphism is often used in class methods where we can have multiple classes with the same method name. For example three classes: Car, Boat, and Plane having a mthod that can move()

# Example
class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        return('Drive')

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        return("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
    def move(self):
        return("Fly")
        
car1 = Car("Ford", "Mustang")	#creates a car class
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# for x in (car1, boat1, plane1):
#     print(x.move())
    
    
# Inheritance Class Polymorphism
# We can use a parent class caled Vehicle and make Car< Boat, and Plane child of classes of Vehicle, the child classes inherits the vehicle methods but overides them

# Example create a class called Vehicle and make Car, Boat, Plane child classes
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        return("Move")
    
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        return ("Sail!")
class Plane(Vehicle):
    def move(self):
        return ("Fly")
car2 = Car("Ford", "Mustang")	#Create a Car Object
boat2 = Boat("Ibizza", 'Touring 20')	#create a Boat object
plane2 = Plane("Boeing", "747")		#create an a Plane Object

for y in (car2, boat2, plane2):
    print(y.brand, y.model)
    print(y.move())
    