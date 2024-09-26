# Exercises: Level 1
# Declare an empty list
lst = list()
# Declare a list with more than 5 items
lst = [1,2,3,4,5,6]
# Find the length of your list
print(len(lst)) 
# Get the first item, the middle item and the last item of the list
print(lst[0],lst[len(lst)//2],lst[len(lst)-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['name', 79, 1.78, True, 'Home address']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies) 
# Print the number of companies in the list
print(len(it_companies)) 

# Print the first, middle and last company
print(it_companies[0],it_companies[len(lst)//2],it_companies[-1])
 
# Print the list after modifying one of the companies
it_companies[0]='SAP'
print(it_companies) 

# Add an IT company to it_companies
it_companies.append('IT company') 
print(it_companies) 
# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,'It Company')
print(it_companies) 
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]=it_companies[1].upper()
print(it_companies) 
# Join the it_companies with a string '#;  '
it_companies = it_companies + ['#:  '] 
# Check if a certain company exists in the it_companies list.
print(it_companies.index('IBM'))
# Sort the list using sort() method
it_companies.sort()
print(it_companies) 
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies) 
 
# Slice out the first 3 companies from the list
for x in range(3):
    it_companies.pop(0) 
print(it_companies) 
# Slice out the last 3 companies from the list
for x in range(3):
    it_companies.pop() 
print(it_companies) 
 
# Slice out the middle IT company or companies from the list
it_len = len(it_companies)
if it_len % 2 == 0:
    it_companies.pop((it_len  // 2) -1)
it_companies.pop((it_len // 2) -1)
print(it_companies) 

# Remove the first IT company from the list
it_companies.pop(it_companies.index('It Company'))
print(it_companies) 
 
# Remove the middle IT company or companies from the list
# 
# Remove the last IT company from the list
# 
# Remove all IT companies from the list
# 
# Destroy the IT companies list
# 
# Join the following lists:
# 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux')+1,'Python')
full_stack.insert(full_stack.index('Redux')+1,'SQL')

print(full_stack)
# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[-1]
print(f'First {min} and last {max}')
# Add the min age and the max age again to the list
ages.append(min)
ages.append(max)
print(ages)
# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages)
ages_len = len(ages)
if ages_len % 2 == 0:
    print(ages[ages_len // 2 -1],ages[ages_len // 2])
    print((ages[ages_len // 2 -1] + ages[ages_len // 2]) / 2)
else:
    print(ages[ages_len // 2 -1])

# Find the average age (sum of all items divided by their number )
sum=0
for n in ages:
   sum+=n
average=sum/ages_len
print(average)
# Find the range of the ages (max minus min)
print(max-min)
# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min-average))
print(abs(max-average))

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries)
countries_len = len(countries)
if countries_len % 2 == 0:
    print(countries[countries_len // 2 - 1])
print(countries[countries_len // 2 ])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(countries)
print(countries[:countries_len // 2 ])
print(countries[countries_len // 2: ])
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
ch, ru, us, *scandic = countries
print(ch, ru, us, scandic)
# 🎉 CONGRATULATIONS ! 🎉