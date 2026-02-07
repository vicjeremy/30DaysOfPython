# Day 7: 30 Days of python programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise level 1
print(len(it_companies)) # 1.
it_companies.add('Twitter') # 2.
it_companies.update(['Twitter', 'Netflix', 'Spotify']) # 3.
it_companies.remove('Twitter') # 4.
it_companies.discard('Twitter') # 5. doesn't raise an error if the element is not in the set

# Exercise level 2
print(A.union(B)) # 1.
print(A.intersection(B)) # 2.
print(A.issubset(B)) # 3.
print(A.isdisjoint(B)) # 4.
print(A | B) # 5.
print(B | A)
print(A.symmetric_difference(B)) # 6.
del A, B # 7.

# Exercise level 3
age_set = set(age) # 1.
print(len(age_set) < len(age)) # 2.

'''
string is an immutable sequence of characters
list is a mutable ordered collection of items
set is an unordered collection of unique items
tuple is an immutable ordered collection of items
'''

sentence = 'I am a teacher and I love to inspire and teach people.'
sentence = sentence.split(' ')
sentence_set = set(sentence)
print(sentence)
print(len(sentence_set))




