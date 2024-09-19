# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + ' ' + 'Days'+ ' ' + 'Of'+ ' ' + 'Python')

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'
# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print('upper'.upper())
# Change all the characters to lowercase letters using lower() method.
print('lower'.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Coding For All'))

# Change Python for Everyone to Python for All using the replace method or other methods.
print('Python for Everyone'.replace('Everyone','All'))

# Split the string 'Coding For All' using space as the separator (split()) .
print('Coding For All'.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
      
# What is the character at index 0 in the string Coding For All.
print('Coding For All'[0])

# What is the last index of the string Coding For All.
indx=(len('Coding For All')-1)
print(indx,'Coding For Alg'[indx])

# What character is at index 10 in "Coding For All" string.
print('Coding For Alg'[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
print('Coding For All'.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print('Coding For All'.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All People'.rindex('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'[31:47+len('because')])

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does ''Coding For All' start with a substring Coding?
print('Coding For All'.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print('Coding For All'.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
print('30DaysOfPython'.isidentifier())

# thirty_days_of_python
print('thirty_days_of_python'.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
      
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge. \nI just wonder what is next.')

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\t\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
print(f'8 + 6 = 14, {8 + 6}')
print(f'8 - 6 = 2, {8 - 6}')
print(f'8 * 6 = 48, {8 * 6}')
print(f'8 / 6 = 1.33, {8 / 6:.2f}')
print(f'8 % 6 = 2, {8 % 6}')
print(f'8 // 6 = 1, {8 // 6}')
print(f'8 ** 6 = 262144, {8 ** 6}')
