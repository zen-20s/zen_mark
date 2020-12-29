# lists(from python crash course)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].upper())
print(bicycles[2].lower())
print(bicycles[-1])  # here - refers to the last item of the list
message = f"my first bicycle was {bicycles[0].title()}. "
print(message)

# chaning,adding and removing elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles[0] = 'ducati'
print(motorcycles)
# appending
# motorcycles.append('ducati')
print(motorcycles)
# insert
motorcycles.insert(0, 'ducati')
print(motorcycles)

# del statement

# del motorcycles[0]
print(motorcycles)

# pop() methode

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# last_owned = (popped_motorcycle)
# print(f"the last motorcycle i owned was a {last_owned.title()}.")
# first_owned = (motorcycles.pop(0))
# print(f"the first motorcycle i owned was a {first_owned.title()}.")
# remove statement
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)

# print(f"\nA {too_expensive.title()}is too expensive for me.")

# organising a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # this is used for bring list in alfabetic order permanently
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
# this is used for bring list in reverse alfabetic order permanently
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))  # this is used to bring list in alfabetic order temprary

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()  # this is used to reverse the list
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # to know the length of the list


# for loop the list

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()},that was a grate trick!")
    print(f"i can't wait to see your next trick,{magician.title()}.\n")
print("thank you, everyone. it was a great show")

# making numerical list

for value in range(1, 5):
    print(value)
for value in range(6):
    print(value)
numbers = list(range(1, 6))
print(numbers)
numbers = list(range(6))
print(numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

square = []
for value in range(11):
    square.append(value**2)
print(square)

# list compeihensions
# to smaller the code of the list
squares = [value**2 for value in range(1, 11)]
print(squares)

# minimum/maximum/sum list

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))  # to know the maximum number of the list

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # to know the minimum number of the list

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sum(digits))  # to know the total sum of the list

# slicing a list

players = ['chales', 'martina', 'michail', 'folarance', 'eli']
print(players[0:4])
print(players[:4])
print(players[2:])
print(players[-2:])

# looping though a list

print("here are the first five players on my team")
for player in players[:5]:
    print(player.title())

# coping a list

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]  # to copy a list by slicing we use [:``]

print("my favorite foods are:")
print(my_foods)

print("my friends favorite foods are")
print(friends_food)

my_foods.append('canoli')  # adding a new item in a list
friends_food.append('ice cream')

print("my favorite foods are:")
print(my_foods)

print("my friends favorite foods are")
print(friends_food)

# combination of loops  + slice in list
my_foods = ['pizza', 'falafel', 'carrot cake']
for my_food in my_foods[:2]:
    print(my_food)
    print(f"{my_food.title()},my favorite foods are")


# tuples
# the list that can not change or the immutable list is called a tuple
# we use parentheses() istead of square brackets[] in list for tuples

dimentions = (200, 50)
print(dimentions[0])
print(dimentions[1])
# seince the tuple does not change so the belowe statements show a eror
# dimentions = (200, 50)
# dimentions[0] = 250
# print(dimentions[0])


# looping though all values in a tuple

dimentions = (200, 50)
for dimention in dimentions:
    print("original dimention:")
    print(dimention)
