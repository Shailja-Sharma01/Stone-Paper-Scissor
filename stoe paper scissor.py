import numpy as np
user=0
comp=0

for i in range(1,6):
    value=input("Enter Choice:")
    l=["Stone","Paper","Scissor"]
    computer=np.random.choice(l)
    print("Computer Choice",computer)
    if value=="Stone" and computer=="Paper":
        print("Paper wins")
        comp=comp+1
    elif value=="Stone" and computer=="Scissor":
        print("Stone wins")
        user=user+1
    elif value=="Paper" and  computer=="Scissor":
        print("Scissor wins")
        comp=comp+1
    elif value=="Paper" and computer=="Stone":
        print("Paper Wins")
        user=user+1
    elif value=="Scissor" and computer=="Stone":
        print("Stone Wins")
        comp=comp+1
    elif value=="Scissor" and computer=="Paper":
        print("Scissor wins")
        user=user+1
    else:
        print("Invalid choice")
print("Computer Score",comp)
print("User Score",user)
if comp>user:
    print("Computer Wins")
else:
    print("User wins")