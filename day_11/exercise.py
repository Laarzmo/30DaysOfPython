# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a,b):
    return(a+b)

print(add_two_numbers(2,3))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(r):
    return(3.14 * r **2)

print(area_of_circle(10))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*n):
    tot = 0
    for i in n:
        if type(i) == type(int()) or type(i) == type(float()):
            tot += i
        else:
            print(f'{i} is not a number')
    return(tot)
print(add_all_nums(4,6,7.8,'qwer',8))        
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def conv_c_to_f(deg):
    return((deg * 9 / 5)+32)
print(conv_c_to_f(100))
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']
    if month in autumn: return('Autumn')
    elif month in winter: return('Winter')
    elif month in spring: return('Spring')
    elif month in summer: return('summer')
    else: return(f'{month} is not a momnth')
print(check_season('Marchf'))
# Write a function called calculate_slope which return the slope of a linear equation
 
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# 
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# 
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# 
# print(reverse_list([1, 2, 3, 4, 5]))
# 
# # [5, 4, 3, 2, 1]
# 
# print(reverse_list1(["A", "B", "C"]))
# 
# # ["C", "B", "A"]
# 
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# 
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# 
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# 
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# 
# numbers = [2, 3, 7, 9];
# 
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# 
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# 
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# 
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# 
# numbers = [2, 3, 7, 9];
# 
# print(remove_item(numbers, 3))  # [2, 7, 9]
# 
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# 
# print(sum_of_numbers(5))  # 15
# 
# print(sum_all_numbers(10)) # 55
# 
# print(sum_all_numbers(100)) # 5050
# 
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# 
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# 
# Exercises: Level 2
# 
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    # 
    # print(evens_and_odds(100))
    # 
    # # The number of odds are 50.
    # 
    # # The number of evens are 51.
# 
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# 
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# 
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# 
# Exercises: Level 3
# 
# Write a function called is_prime, which checks if a number is prime.
# 
# Write a functions which checks if all items are unique in the list.
# 
# Write a function which checks if all the items of the list are of the same data type.
# 
# Write a function which check if provided variable is a valid python variable
# 
# Go to the data folder and access the countries-data.py file.
# 
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# 
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.