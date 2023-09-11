# age = 36
# txt = "My name is John, I am {}"
# print(txt .format(age))
# print("{} is an even number" .format(16))

# print(bool("Hello"))
# print(bool(15))

# Sorting list
# - Alphabetically

"""thislist = ["orange", "mango", "Kiwi", "pinapple"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)"""

"""car = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
print(car)
x = car.values()
print(x)
car["color"] = "red"
print(car)
print(x)"""


"""
a = 2
b = 330
print("A") if a > b else print("B")"""

# i = 1
# while i < 6:
#     print(i)
#     # i += 2
#     if i == 3:
#         # break
#         continue
#     i += 1

"""i = 0
while i < 6:
    # i += 1
    if i == 3:
        continue
    print(i)
    i += 2"""
    
'''i = 1
while i < 6:
    print(i)
    i += 1'''
# else:
#     print("i is no longer less than 6")
    

# fruits = ['apple', 'banana', 'cherry']
# for x in fruits: 
#     print(x)
#     if x == "banana":
#         continue
    # print(x)
    
# for x in 'banana':
#     print(x)


'''for x in range(6):
    print(x)
    if x == 3: break
    # print(x)
else:
    print("Finally finished")'''
    
'''adj = ["red", 'big', 'taste']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)'''        
        
'''
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)'''
    
# def my_function(*kids):
#     print('The youngest child is ' + kids[1])

# my_function("Emil", "Tobias", "Linus")

# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "linus")

'''def my_function(**kid):
    print("His last name is " + kid["1name"])

my_function(fname = "Tobias", lname = "Refsnes")
'''

'''def my_function(food):
    for x in food:
        print(x)
y = ("Red", "White", "Blue")
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)
my_function(y)
print(y)'''

'''#Return value
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(7))'''


#Python Lamda
# x = lambda a, b : a + 10 + b
# print(x(5,7))

# def myfunc(n):
#     return lambda a: a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

'''import my_module
my_module.greeting("Jonathan")

a = my_module.person1["age"]
print(a)'''


# counter = 0
# name = "Samuel Okoduwa"
# size = len(name)
# while counter < size:
#     print(name[counter], end= "\n")
#     counter = counter + 1

# print("Sammy has {0:4} red {1:16}!".format(5, "balloons"))
# print("{:-<20s}".format("Sammy"))
# print("Sammy has {0:4} red {1:16}!".format(5, "balloons"))

# for number in range(99):
#     print("{:02}".format(number), end=",")

# for i in range(10):
#     for j in range(10):
#         print("{} * {} = {}".format(i,j,(i*j)))


"""#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 0:
    last_digit = number % 10
else:
    last_digit = (-(abs(-number) % 10))
print("Last digit of {} is {} ".format(number, last_digit), end=" ")
if last_digit > 5:
    print("and is greater than 5")
if last_digit == 0:
    print("and is 0")
if last_digit < 6 and last_digit != 0:
    print("and less than 6 and not 0")

"""

def fibonacci_sequence(i, j):
    pass
    