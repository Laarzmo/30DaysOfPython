# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update('SAP','SUSE')
# Remove one of the companies from the set it_companies
it_companies.pop()
# What is the difference between remove and discard
# This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

# Exercises: Level 2
# Join A and B
print(A | B)
# Find A intersection B
print(A & B)
# Is A subset of B
print( A <= B)
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
print(B | A, A | B)
# What is the symmetric difference between A and B
print(A ^B)
# Delete the sets completely
del A, B
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_st = set(age)
print(len(ages_st),len(age))
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
print(len(set('I am a teacher and I love to inspire and teach people'.split())))