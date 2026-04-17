#RP
#PS
#SR
import random
def result(you ,comp):
    if ((you=='R'and comp=='P')or
        (you=='P'and comp=='S')or
        (you=='S'and comp=='R')):
        return -1  #you lose
    if(you==comp):
        return 0   #match draw
    else:
        return 1  #you win 
#Generate the computer choice
num=random.randint(1,100)    
if num<=33:
    comp='R'
elif num>33 and num<=66:
    comp='P'
else:
    comp='S'
#prompt user for choice
print ("Enter your choice 'R' for Rock, 'P' for Paper,'S' for scissor")
you=input().strip().upper()  #convert to uppercase
print(f"you choose {you} and computer choose {comp}")

conclue=result(you,comp)
if conclue==-1:
    print("You Loose!")
elif conclue==0:
    print("Game Draw")
else:
    print("You Win")        

      

    
