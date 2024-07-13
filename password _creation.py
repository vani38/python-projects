import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*']
print("WELCOME TO PASSWORD GENERATOR")
a=int(input("Howmany letters you want in your password?\n "))
b=int(input("Howmany numbers you want in your password?\n"))
c=int(input("Howmany symbols you want in your password?\n"))
password=[]

for i in range(1,4):
    char=random.choice(letters)
    password+=char
    
for i in range(1,3):
    char=random.choice(numbers)
    password+=char
    
for i in range(1,2):
    char=random.choice(symbols)
    password+=char

print(password)
random.shuffle(password)
my_password="".join(password)
print(my_password)
