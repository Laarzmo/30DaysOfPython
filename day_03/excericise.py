import math
age = int()
height = float()
comp = complex()


print('The area of the triangle is:',float(input('Base:')) * float(input('Height:')) * 0.5)

print('The perimater of the triangle is:',float(input('Sida a: ')) + float(input('Side b: ')) + float(input('Side c: ')))

length = float(input('length: '))
width = float(input('width: '))
print('area: ',length * width)
print('perimeter: ',(length + width) * 2 )

radius = float(input('Radius: '))
print('Area: ', radius ** 2 * 3.14)
print('Circum: ', radius * 2 * 3.14)

 
m8 = 2
p1 = [2,2]
p2 = [6,10]
m9 = (p2[1]-p1[1])/(p2[0]-p1[0])

print(p1,p2,m8,m9)
print(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))  

x = float(input('X: ')) # -3 -> y=0
y = x ** 2 + 6 * x + 9
print('y: ',y)

print(len('python') != len('dragon'))
print('on' in ('python' and 'dragon'))
print('jargon' in 'I hope this course is not full of jargon.')
print(str(float(len('python'))))
print((float(input('Gimmi numer')) % 2) == 0)
print(( 7 // 3 ) == int(2.7))
print(type('10') == type(10))
print(int(9.8) == 10)

print(float(input('Hours: ')) * float(input('rate: ')))
print(int(input('Years lived: '))*3600*24*365)


x = 1
print(x,1,x,x**2,x**3)
x += 1
print(x,1,x,x**2,x**3)
x += 1
print(x,1,x,x**2,x**3)
x += 1
print(x,1,x,x**2,x**3)
x += 1
print(x,1,x,x**2,x**3)
