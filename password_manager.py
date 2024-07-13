master_password=input("What is the master password?")

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,password=data.split("|")
            print("User:",user,"Password:",password)
                        
def add():
    name=input("Account name:")
    password=input("password:")
    with open("password.txt","a") as f:
        f.write(name+"|"+master_password+"\n")
        
while True:
    mode=input("Would you like to add new password or view existing ones(view,add)? ")
    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode.")
        