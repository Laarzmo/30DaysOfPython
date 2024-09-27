# Create an empty dictionary called dog
dog = dict()
# Add name, color, breed, legs, age to the dog dictionary
dog.update({'name': '', 'color':'', 'breed':'', 'legs':'', 'age':''})
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'',
    'last_name':'',
    'gender':'',
    'age':'',
    'martial_status': True,
    'skills':['',''],
    'country':'',
    'city':'',
    'address':''
}
print(student)
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student['skills'])
# Modify the skills values by adding one or two skills
student['skills'].extend(['eka','toka'])
print(student['skills'])

# Get the dictionary keys as a list
print(list(student.keys()))
    
# Get the dictionary values as a list
print(list(student.values()))

# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
student.popitem()
del student
# Delete one of the dictionaries