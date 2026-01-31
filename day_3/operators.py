# Day 3: 30 Days of python programming

# Exercises
age = 23 # 1.
height = 167.5 # 2.
complex_number = 1 + 2j # 3.

base = input('Enter base: ') # 4.
height = input('Enter height: ')
print('The area of the triangle is ' + str(int((int(base) * int(height)) / 2)))

side_a = input('Enter side a: ') # 5.
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
print('The perimeter of the triangle is ' + str(int(side_a) + int(side_b) + int(side_c)))

length = input('Enter length: ') # 6.
width = input('Enter width: ')
print('The area of the rectangle is ' + str(int(length) * int(width)) + ' and the perimeter is ' + str(2 * (int(length) + int(width))))

radius = input('Enter radius: ') # 7.
print('The area of the circle is ' + str(3.14 * int(radius) * int(radius)) + ' and the circumference is ' + str(2 * 3.14 * int(radius)))

fungsi_garis = input('Enter "y=mx+c": ') # 8.
print('The slope is ' + str(int(fungsi_garis[2])) + ' and the x-intercept is ' + str(int(int(fungsi_garis[5])/int(fungsi_garis[2]))) + ' and the y-intercept is ' + str(int(fungsi_garis[5])))

# 9. (2,2) and (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
print('The slope is ' + str(int((y2 - y1) / (x2 - x1))) + ' and the distance is ' + str(int((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)))

print('find y in y = x^2 + 6x + 9 when y = 0 is: ' + str(int((9/7)**0.5))) # 11.

print(len('python') > len('jargon')) # 12.

print('on' in 'python' and 'on' in 'jargon') # 13.

print('jargon' in 'I hope this course is not full of jargon') # 14.

print('on' not in 'python' and 'on' not in 'jargon') # 15.

print(str(float(len('python')))) # 16.

even = input('Enter a number to check if it is even or not: ') # 17.
print(int(even) % 2 == 0)

print(7//3 == int(2.7)) # 18.

print(type('10') == type(10)) # 19.

print(int(9.8) == 10) # 20.

print('Your weekly earning is ' + str(int(input('Enter hours: ')) * int(input('Enter rate per hour: ')))) # 21.

print('You have lived for ' + str(int(input('Enter number of years you have lived: ')) * 365 * 24 * 60 * 60) + ' seconds') # 22.

print('1' + ' ' + str(1**0) + ' ' + str(1**1) + ' ' + str(1**2) + ' ' + str(1**3)) # 23.
print('2' + ' ' + str(2**0) + ' ' + str(2**1) + ' ' + str(2**2) + ' ' + str(2**3))
print('3' + ' ' + str(3**0) + ' ' + str(3**1) + ' ' + str(3**2) + ' ' + str(3**3))
print('4' + ' ' + str(4**0) + ' ' + str(4**1) + ' ' + str(4**2) + ' ' + str(4**3))
print('5' + ' ' + str(5**0) + ' ' + str(5**1) + ' ' + str(5**2) + ' ' + str(5**3))
