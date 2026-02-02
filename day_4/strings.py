# Day 4: 30 Days of python programming

a, b, c, d = 'Thirty', 'Days', 'Of', 'Python' # 1.
full = a + b + c + d
print(full)

e, f, g = 'Coding', 'For', 'All' # 2.
full2 = e + f + g
print(full2)

company = "Coding For All" # 3.

print(company) # 4.

print(len(company)) # 5.

print(company.upper()) # 6.

print(company.lower()) # 7.

print(company.capitalize()) # 8.
print(company.title())
print(company.swapcase())

print(company[0:7]) # 9.

print(company.index('Coding')) # 10.
print(company.find('Coding'))
print(company.rfind('Coding'))
print(company.rindex('Coding'))

print(company.replace('Coding', 'Python')) # 11.

text12 = 'Python for Everyone' # 12.
print(text12.replace('Everyone', 'All')) 

print(company.split(' ')) # 13.

text14 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' # 14.
print(text14.split(', '))

print(company[0]) # 15.

print(company[-1]) # 16.

print(company[10]) # 17.

print('PFE') # 18.

print('CFA') # 19.

print(company.index('C')) # 20.

print(company.find('F')) # 21.

text22 = company + 'People' # 22.
print(text22.rindex('l')) 

text23= 'You cannot end a sentence with because because because is a conjunction' # 23.
print(text23.find('because'))
print(text23.index('because'))

text24 = 'You cannot end a sentence with because because because is a conjunction' # 24.
print(text24.rfind('because'))
print(text24.rindex('because'))

print(text24.replace(' because because because ', ' ')) # 25.

print(text24.find('because')) # 26.

print(text24.replace(' because because because ', ' ')) # 27.

print(company.startswith('Coding')) # 28.

print(company.endswith('coding')) # 29.

text30 = '   Coding For All      '
print(text30.strip()) # 30.


challenge = '30DaysOfPython' # 31.
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

python_library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
combine = ' '.join(python_library)
print(combine) # 32.

print('I am enjoying this challenge.\nI just wonder what is next.') # 33.

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki') # 34.

print(f'radius = {10}\narea = {3.14} * radius ** {2}\nThe area of a circle the radius {10} is {3.14 * 10 ** 2:.0f} meters square.') # 35.

print(f'8 + 6 = {8+6}\n8 - 6 = {8-6}\n8 * 6 = {8*6}\n8 / 6 = {8/6:.2f}\n8 % 6 = {8%6}\n8 // 6 = {8//6}\n8 ** 6 = {8**6}') # 36.