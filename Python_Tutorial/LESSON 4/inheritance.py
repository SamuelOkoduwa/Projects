
# A Parent Class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(self.fname, self.lname)
        
# x = Person("John", "Jerry")
# x.printname()

# A child Class
class Student(Person):
    #when you use the __init__() function it will no longer inherit from the parent
    def __init__(self, fname, lname):
    # to keep the nheritance of the parent __init__() function, add a call to the parents __init__ function
        Person.__init__(self, fname, lname)
    
x = Student("Mike", "Johnson")
x.printname()
