# Day 6: 30 Days of python programming

# Exercise Level 1
empty_tuple = tuple() # 1.

brothers = ('david', 'steven', 'jeremy') # 2.
sisters = ('lucy', 'lucia', 'lucien')

siblings = brothers + sisters # 3.
print(siblings)

print(len(siblings)) # 4.

family_members = siblings + ('mother', 'father') # 5.
print(family_members)

# Exercise Level 2

print(family_members[:-2]) # 1.
parents = family_members[-2:]
print(parents)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('potato', 'tomato', 'cabbage', 'onion')
animal_products = ('milk', 'meat', 'eggs', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products # 2.
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp) # 3.
print(food_stuff_lt)

print(food_stuff_lt[len(food_stuff_lt)//2]) # 4.

print(food_stuff_lt[:3]) # 5.
print(food_stuff_lt[-3:]) 

del food_stuff_tp # 6.

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden') # 7.
print('Estonia' in nordic_countries) 
print('Iceland' in nordic_countries) 



