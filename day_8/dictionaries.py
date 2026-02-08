# Day 8: 30 Days of python programming

dog = {} # 1.
dog = {'name': 'Buddy', 'age': 5, 'color': 'brown', 'breed': 'Golden Retriever', 'legs': 4} # 2.
student = {'first_name': 'John', 'last_name': 'Doe', 'gender': 'Male', 'age': 20, 'marital_status': 'Single', 'skills': ['Python', 'Java', 'C++'], 'country': 'USA', 'city': 'New York', 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY', 'zip': '10001'}}
print(len(student)) # 4.

print(student['skills']) # 5.
print(type(student['skills']))

student['skills'].append('HTML') # 6.
student['skills'] = 'SQL'
print(student['skills'])

keys = student.keys()
print(keys) # 7.

values = student.values()
print(values) # 8.

tuples = tuple(student.items())
print(tuples) # 9.

student.popitem()
print(student) # 10.

del dog




