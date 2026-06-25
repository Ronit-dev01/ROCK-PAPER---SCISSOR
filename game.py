import random
while True:
    stack=["scissor","rock","paper"]
    com=random.choice(stack)
    user=input("pick one out of rock , paper & scissor : ").lower()

    if user==com:
        print("match tie ")
    elif user=="rock" and com == "scissor":
        print("user win")
    elif user == "scissor" and com == "paper":
        print("user wins")
    elif user=="paper" and com == "rock":
        print("user wins")
    else:
        print("computer wins")
    print("computer chooses: ",com)
    play=input("wanna play again yes or no : ").lower()
    if play=="no":
        print("thanks for playing ")
        break
    
        
