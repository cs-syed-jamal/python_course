import random
'''
1 for snake
-1 for water
0 for gun
'''
# Generate a random number from -1, 0, or 1
computer=-random.choice([-1, 0, 1])
youstr=input("Enter you choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",0:"Gun",-1:"Water"}
you=youDict[youstr]
print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")
if(you==computer):
    print("Draw!")
else:    
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")  
    elif(computer == 0 and you == 1):
        print("You Lose!")   
    else:
        print("Something went Wrong!") 
        