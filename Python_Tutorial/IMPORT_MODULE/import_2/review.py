#!/usr/bin/env/python3

# def no_c(my_string):
#     new_str = ""
#     for char in my_string:
#         if char != "c"

"""my_string = "Character"
no_c = ""
for char in my_string:
    if char != "c" and char != "C":
        no_c = no_c + char
# print (no_c)

def no_c(my_string):
    remove_c_C = ""
    for char in my_string:
        if char != "c" and char != "C":
            remove_c_C += char
    return remove_c_C"""

# print(no_c("Character"))
# print(no_c("There are Charitable carts in Cameron"))

# matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# for integer in matrix:
#     print(integer)
    
'''
u = (1, 3 , 5, 7, "Print")

print(len(u), u[0])

sentence = "At Holberton school, I learnt C!"
length = len(sentence)
first = sentence[0]
if sentence == ():
    first == None
else:
    print("Length: {:d} - First character: {}" .format(length, first))'''

'''def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if sentence == ():
        first == None
    else:
        return ("Length: {:d} - First character: {}" .format(length, first))
print(multiple_returns("I am in the lords army"))
# print(multiple_returns())
    
# print ("Length: {:d} - First character: {}" .format(length, first))
'''    


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for x in matrix:
#     print(x)

'''set_1 = { "Python", "C", "JavaScript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
# c_set = common_elements(set_1, set_2)
c_set = set_1.intersection(set_2)
print(c_set)
print(sorted(list(c_set)))

# def common_elements(set_1, set_2):
#     c_set = set_1.intersection(set_2)
#     return c_set
# print (common_elements(set_1=set_1, set_2=set_2))'''

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# # thisdict["year"] = 2018
# thisdict["color"] = "red"
# print(thisdict)

# def update_dictionary(a_dictionary, key, value):
#     a_dictionary = {
#         key: value
#     }
#     a_dictionary[key] = value
#     return a_dictionary

# print(update_dictionary("thisdict", "brand", "toyota"))

# def best_score(a_dictionary):
#     highest_score = max(a_dictionary)
#     if highest_score == max(a_dictionary):
#         return highest_score
#     elif not a_dictionary:
#         return None

# def best_score(a_dictionary):
#     if not a_dictionary:
#         return None
#     bestScore = 0
#     bestScore_key = ""
#     for key, value in a_dictionary.items():
#         if value > bestScore:
#             bestScore = value
#             bestScore_key = key
#     return bestScore_key
    
# print(best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}))
# print(best_score(None))
    
# scores = {
#     "Abel": 16,
#     "Jude": 21,
#     "Samuel": 27,
#     "Johnson": 25
# }
# keys = scores.keys()
# values = scores.values()
# best_score = max(scores)
# # print(keys)
# # print(values)
# # print(scores)
# print(best_score)

# scores = [20, 67, 76, 29, 56]
# for index in range(len(scores)):
#     # print(index)
#     print(f"{index} => {scores[index]}")
# # for score in scores:
# #     print(score)

# nums = [1, 2, 3, 4]
# square_nums = []
# for num in nums:
#     square_nums.append(num * num)

# print(f" before comprehension: {nums} => {square_nums}")

# compr_nums = [num ** 2 for num in nums
# print(f"After Comprehension: {nums} => {compr_nums}")

# num = [3, 5, 1, 7, 9]
# add_num = []

# for addition in num:
#     add_num
    
# a = 10
# b = 20
# # temp = a
# # a = b
# # b = temp
# # print(a, b)
# a, b = b, a
# print(a, b)
'''
class Cristal:
    # Attribute
    color = "blue"
    # print(f"The color is {color}")
    
    def __init__(self, id):
        self.id = id
        print("You just created an object")
    # Method
    def write(self):
        print("Hey! I am writing")
# ****************The end of the class************

# Creating an instance of the object Class ==> Object(Instanciation)
first_pen = Cristal(id="dl-01")  

# Using a mthod
# first_pen.write()

# Access to the attribute
# print(first_pen.color)
print(f"The first color is {first_pen.color}")
print(f"The first pen id is {first_pen.id}")

second_pen = Cristal(id="dl-02")
print(f"The secnd clolor is {first_pen.color}")
print(f"The second id is {second_pen.id}")'''


"""
def fahrenheit(T):
    return((float(9)/5)* T + 32)
def celsius(T):
    return((float(5)/9)*T - 32)
temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celsius, F)

print(list(F))"""

# temperatures_in_Fahrenheit = list(F)
# temperatures_in_celsius = list(map(celsius, temperatures_in_Fahrenheit)

# print(temperatures_in_Fahrenheit)

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = number % 10 and -(-abs(-number)) % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than five")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
    

                                  
                                                        