import random
def gamestart():
    userscore=0
    computerscore=0
    while True:
        user=userchoice()
        computer=computerchoice()
        print("You Choose-->",user)
        print("Computer Choose-->",computer)
        result=winner(user,computer)
        print(result)
        if result=="YOU WIN THE GAME !....":
            userscore+=1
        elif result=="COMPUTER WIN THE GAME !....":
            computerscore+=1
        print("Score => You->",userscore,"Computer->",computerscore)
        playagain=input("Do You Want To Play Again (yes/no) :").lower()
        if playagain!='yes':
            print("Final Score => You->",userscore,"Computer->",computerscore)
            print("Thank You For Playing !....")
            print("GAME ENDED")
            break
def userchoice():
    choice=input("Enter Your Choice (rock,paper,scissors) :").lower()
    while choice not in ['rock','paper','scissors']:
        print("Invalid Choice..Please Enter a Valid Choice")
        choice=input("Enter You Choice (rock,paper,scissors) :").lower()
    return choice
def computerchoice():
    return random.choice(['rock','paper','scissors'])
def winner(user,computer):
    if (user=='rock' and computer=='scissors') or\
       (user=='paper' and computer=='rock') or\
       (user=='scissors' and computer=='paper'):
        return "YOU WIN THE GAME !...."
    elif user==computer:
        return "ITS A TIE !...."
    else:
        return "COMPUTER WIN THE GAME !...."
gamestart()
