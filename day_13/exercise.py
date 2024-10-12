# syntax
# [i for i in iterable if expression]

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i >= 0])

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

print([k for i in list_of_lists for j in i for k in j])

#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

print([(k,0,k,k**2,k**3,k**4,k**5,k**6) for k in range(11)])
print()

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

print([ [y[0].upper(),y[0].upper()[:3],y[1].upper()] for x in countries for y in x ])


#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]
print([{'country':m[0], 'city':m[1]} for k in countries for m in k])

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

print([y[0] + ' ' + y[1] for x in names for y in x])