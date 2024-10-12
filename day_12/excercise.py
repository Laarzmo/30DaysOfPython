# exec 1
from random import randint
from string import ascii_letters, digits
def random_user(l):
    chars = ascii_letters + digits
    r = ''
    for i in range(l+1):
        r = r + chars[randint(0,len(chars)-1)]
    return(r)

def user_id_gen_by_user():
    a, b = map(int, input('user input: ').split())
    for x in range(a+1):
        print(random_user(b))


print(random_user(5))
# user_id_gen_by_user()

def rgb_color_gen():
    return('rgb('+str(randint(0,255))+','+str(randint(0,255))+','+str(randint(0,255))+')')
print(rgb_color_gen())