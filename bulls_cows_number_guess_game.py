#import required module
import random
#returns list of digits of a number
def getDigits(num):
    return [int(i)for i in str(num)]
#returns True if number has no duplicate digits otherwise False
def noDuplicates(num):
    num_list=getDigits(num)
    if len(num_list)== len(set(num_list)):
        return True
    else:
        return False
#generates a 4 digit number with no repeated digits
def generateNum():
    while True:
        num=random.randint(1000,9999)
        if noDuplicates(num):
            return num
#returns common digits with exact matches(bulls) and the common digits in wrong position(cows)
def numOfBullsCows(num,guess):
    bull_cow=[0,0]
    num_list=getDigits(num)
    guess_list=getDigits(guess)
    for i,j in zip(num_list,guess_list):
        #common digit present
        if j in num_list:
            #common digit exact match
            if j==i:
                bull_cow[0]+=1
            #common digit match but in wrong position
            else:
                bull_cow[1]+=1
    return bull_cow
#secret code
num=generateNum()
tries=int(input("Enter number of tries:"))
#play game until correct case or till no tries left
while tries>0:
    guess=int(input("Enter your guess:"))
    if not noDuplicates(guess):
        print("Number should not have repeated digits.Try again.")
        continue
    if guess<1000 or guess>9999:
        print("Enter 4 digit number only.Try again.")
        continue
    bull_cow=numOfBullsCows(num,guess)
    print(f"{bull_cow[0]}bulls,{bull_cow[1]}cows")
    tries-=1
    if bull_cow[0]==4:
        print("You guessed right!")
        break
    else:
        print(f"You ran out of tries.")
print({num})
            
            
