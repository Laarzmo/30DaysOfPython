# Exercises: Level 1
# Create an empty tuple
tpl = tuple()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bro = ('bro first','bro second')
sis = ('sis first','sis second')

# Join brothers and sisters tuples and assign it to siblings
siblings =  bro + sis
print(siblings)

# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('father', 'mother')
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
*sibling, father, mother = family_members
print(sibling, father, mother)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('orange', 'apple')
# vegetables = ('carrot','potato')
vegetables = ('carrot','potato','cocumber')
animal_products = ('moose','pig')
food_stuff_tp = fruits + vegetables + animal_products
# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt)
print((len(food_stuff_lt)+1)//2)
print((len(food_stuff_lt)+1)//2-1,(len(food_stuff_lt))+1//2*-1+1)

print(food_stuff_lt[:(len(food_stuff_lt)+1)//2-1],food_stuff_lt[(len(food_stuff_lt)+1)//2*-1+1:])
# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3],food_stuff_lt[-3:])
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print(nordic_countries.count('Estonia'))
# Check if 'Iceland' is a nordic country
print(nordic_countries.count('Iceland'))
