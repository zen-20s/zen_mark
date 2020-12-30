# if statement (chapter 5)

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# (==) equality operator
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')


car = 'subaru'
print("is car == 'subaru' ? i pridict true.")
print(car == 'subaru')

print("\nis car == 'audi' ? i pridict false.")
print(car == 'audi')

# we can do comparition useing function with out effecting the original value

car = 'Audi'
print(car.lower() == 'audi')
print(car)
# (!=) inequality operator
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("anchovies!")

answer = 17

if answer != 45:
    print("that is not the correct answer.please try again!")

# using (and) to check multiple condition
# if any one condition failes the whole condition get false

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# using (or) to check multiple condition
# if any one condition fail and one get passes than the condition gets true

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# checking whether a value is (in) a list

requested_topping = ['mushroom', 'onion', 'pineapple']
print('mushroom' in requested_topping)
print('peperroni' in requested_topping)

# checking whether a value is (not in) a list

banned_users = ['andrew', 'carlolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")

# simple if statement

age = 19
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet?")

# if elif-else chain

age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet?")
else:
    print("sorry,you are too young to vote.")
    print("please register to vote as soon as you turn 18!")

# if/else/elif chain

age = 12

if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $25.")
else:
    print("your admission cost is $40.")

age = 18

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"your cost is ${price}.")

# using multiple elif blocks

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"your addmition cost is ${price}")


requested_topping = ['mushroom', 'extra cheese']

if 'mushroom' in requested_topping:
    print("adding mushroom")
if 'pepperoni' in requested_topping:
    print("adding pepperoni")
if 'extra cheese' in requested_topping:
    print("adding extra cheese")
print("\nfinised making your pizza")


alien_colour = 'green'

if alien_colour == 'green':
    print("your alien colour is green you got 5 points")
elif alien_colour == 'yellow':
    print("your alien colour is yellow you got 10 points")
elif alien_colour == 'red':
    print("your alien colour is red you got 15 points")


requested_toppings = ['mushroom', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"adding {requested_topping}")
print("\nfinised making your pizza")


requested_toppings = ['mushroom', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("sorry we are out of green pepper")
    else:
        print(f"adding {requested_topping}.")
print("\nfinised making your pizza")


requested_toppings = ['mushroom']

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}.")
    print("\nfinised making your pizza!")
else:
    print("are you sure you want a plane pizza")

# adding a list+for loop+if else statement for ordering a pizza
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green pepper':
            print("sorry we are out of green pepper")
        else:
            print(f"adding {requested_topping}.")
    print("\nfinised making your pizza")
else:
    print("are you sure you want a plane pizza")

# using multiple list


avaliable_topping = ['mushroom', 'green pepper', 'peperroni',
                     'extra cheese', 'pineapple', 'oliver']

requested_toppings = ['mushroom', 'french fries', 'extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in avaliable_topping:
            print(f"adding {requested_topping}")
        else:
            print(f"sorry, we don't have {requested_topping}.")
    print("\nfinised making your pizza")
else:
    print("are you sure you want a plane pizza")
