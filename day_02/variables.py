# level 1
first_name = 'First'
last_name = 'Name'
full_name = 'Full Name'
country = 'Finland'
city = 'Helsinki'
age = 27
year = 1999
is_married = False
is_true = True
is_light_on = True
make, model, year, displacement = 'Skoda', 'Octavia', 2018, 1.8

# level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(make),type(model),type(year),type(displacement))

print(len(first_name))
print(len(first_name)<len(last_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_two // num_one

import math

area_of_circle = 30 ** 2 * math.pi
circum_of_circle = 30 * 2 * math.pi

radius = float(input('Radius: '))
print(radius ** 2 * math.pi)

first_name = input('First name: ')
last_name = input('Last name:' )
country = input('Country: ')
age = int(input('Age: '))
