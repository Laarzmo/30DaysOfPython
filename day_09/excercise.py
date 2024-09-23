#Exercises: Day 9
#Exercises: Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18-age} more years to learn to drive. ')
     
my_age = int(input('Enter my age: '))
your_age = int(input('Enter your age: '))
if abs(my_age - your_age) > 1:
    plur = 's'
else:
    plur = ''
if my_age > your_age:
    print(f'I am {my_age-your_age} year{plur} older than you')
elif my_age < your_age:
    print(f'You aer {your_age-my_age} year{plur} older than me')
else:
    print('We are same age')

#### Exercises: Level 2
score = int(input('Score: '))
if score < 0 or score > 100:
    print('Give score between 0-100)')
elif score >= 80: print('A')
elif score >= 70: print('B')
elif score >= 60: print('C')
elif score >= 50: print('D')
else: print('F')
 

autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
month = input('Monht: ')
if month in autumn: print('Autumn')
elif month in winter: print('Winter')
elif month in spring: print('Spring')
elif month in summer: print('summer')
else: print(f'{month} is not a momnth')

#
#The following list contains some fruits:
#
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('fruit: ')
if fruit in fruits:
    print(f'{fruit} is in the list')
else:
    fruits.append(fruit)
    print(fruits)
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
#
#Exercises: Level 3
#Here we have a person dictionary. Feel free to modify it!
#
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
 #* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][(len(person['skills'])//2)])
 #* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    print('Is python ','Python' in person['skills'])

    if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
    if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a backend developer')
    if 'Node' in person['skills'] and 'Ract' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')

  #* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 #* If the person is married and if he lives in Finland, print the information in the following format:
    #Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] and person['country'] == 'Finland':
    print('sabeneh Yetayeh lives in Finland. He is married.')