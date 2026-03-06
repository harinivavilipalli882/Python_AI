print("Hello world")

a = 50
if a > 10:
 # print("{0} is greater than 10".format(str(a)))
 # print(str(a) + " is greater than 10")
   print(a, " is greater than 10")

print("Hello World!", end=" ")
print("I will print on the same line.")

print("Age is", 23)
print(2*3)
print(8+3)

##
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x,y,z)

############# Variables ##################

name = "Harini"      # string
age = 23             # integer
height = 5.3         # float
is_student = True    # boolean

print(name, age, height, is_student)


########## Converting between types #########
num_str = "100"
num_int = int(num_str)   # string → int
num_float = float(num_int)  # int → float
num_back_to_str = str(num_float)  # float → string

print(num_int, num_float, num_back_to_str)


################## LIST ################
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")   # add item
print(fruits[0])          # access first item
print(fruits[-1])         # access last item


################## TUPLE ################
coordinates = (10, 20)
print(coordinates[0])   # immutable, cannot change values


################## SET ################
unique_numbers = {1, 2, 3, 3, 2}
unique_numbers.add(4)
print(unique_numbers)   # duplicates removed automatically


################## DICTIONARIES ################

student = {"name": "Harini", "age": 22, "course": "Python"}
print(student["name"])   # access value
student["age"] = 23      # update value




################## IF..ELIF..ELSE conditions ################
age = 23

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")


################## FOR LOOP ################
for fruit in ["apple", "banana", "cherry"]:
    print("I like", fruit)

################## WHILE LOOP ################
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1


import random
print(random.randrange(1, 10))