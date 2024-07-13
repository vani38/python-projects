print("WELCOME TO COMPUTER QUIZ")
playing=input("Do you want to play?")
if playing!="yes":
    quit()
print("Okay!Let's play:)")
score=0
answer=input("What does MU stands for?")
if answer== "memory unit":
    print("Right answer")
    score+=1
else:
    print("Wrong answer")
answer=input("What does CPU stands for?")
if answer== "central processing unit":
    print("Right answer")
    score+=1
else:
    print("Wrong answer")
answer=input("What does GPU stands for?")
if answer== "graphics processing unit":
    print("Right answer")
    score+=1
else:
    print("Wrong answer")
answer=input("What does RAM stands for?")
if answer== "random access memory":
    print("Right answer")
    score+=1
else:
    print("Wrong answer")
print("you got" + " " + str(score)+ "  " + "questions right answer")  
    