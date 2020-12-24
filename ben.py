#lists(from python crash course)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].upper())
print(bicycles[2].lower())
print(bicycles[-1])  #here - refers to the last item of the list
message = f"my first bicycle was {bicycles[0].title()}. "
print(message)

#chaning,adding and removing elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#motorcycles[0] = 'ducati'
print(motorcycles)
#appending
#motorcycles.append('ducati')
print(motorcycles)
#insert
motorcycles.insert(0, 'ducati')
print(motorcycles)

#del statement

#del motorcycles[0]
print(motorcycles)

#pop() methode

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# last_owned = (popped_motorcycle)
# print(f"the last motorcycle i owned was a {last_owned.title()}.")
# first_owned = (motorcycles.pop(0))
# print(f"the first motorcycle i owned was a {first_owned.title()}.")
#remove statement
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)

# print(f"\nA {too_expensive.title()}is too expensive for me.")

#organising a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()  #this is used for bring list in alfabetic order permanently
# print(cars)
