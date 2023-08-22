# Polymorphism is often used in class methods where we can have multiple classes with the same method name.
# for example three classes: Car, Boat, and Plane having a mthod that can move()

# Example
class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print('Drive')

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
    def move(self):
        print("Fly")
        
car1 = Car("Ford", "Mustang")	#creates a car class
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")


        