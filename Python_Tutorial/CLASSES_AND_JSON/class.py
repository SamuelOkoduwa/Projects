# Sample of classes
class MyClass:
    x = 5
# print(MyClass().x)

"""# Create a class neamed Person, use the __init__() function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # using the string representation of an object with __str__() function
    def __str__(self):
        return f"{self.name}({self.age})"
        
p1 = Person("John", 36)
# print(f"His name is {p1.name} and is {p1.age} years")
print(p1)"""

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def print_name(self):
        return f"My first name is {self.first_name} and my last name is {self.last_name}"
p2 = Person("Julius", "Rufus0")
print(p2)