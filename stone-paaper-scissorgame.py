
# print(s)
x = int(input("enter no. of rounds you want to play"))
# for i in range(1,11):
y = 1
for i in range(1,x+1):
    import random

    your_turn_no = 0
    computer_turn_no = 0
    game_round = 0
    list = ["stone", "paper", "scissors"]
    comp = random.choice(list)
    y += 1
    user = str(input("enter s for stone \n"
                     "p for paper\n"
                     "r for scissor\n"))
    if user == "s":
        if comp == "stone":
            print("computer choose", comp)
            print("oh its tie...")
            game_round+=1
        elif comp == "scissors":
            print("computer choose",comp)
            print("you won this round")
            your_turn_no+=1
        elif comp =='paper':
            print("computer choose",comp)
            print("oh you lose this round")
            computer_turn_no+=1
    if user == "p":
        if comp == "paper":
            print("computer choose", comp)
            print("oh its tie...")
            game_round+=1
        elif comp == "stone":
            print("computer choose",comp)
            print("you won this round")
            your_turn_no+=1
        elif comp =='scissor':
            print("computer choose",comp)
            print("oh you lose this round")
            computer_turn_no+=1
    if user == "r":
        if comp == "scissors":
            print("computer choose", comp)
            print("oh its tie...")
            game_round+=1
        elif comp == "paper":
            print("computer choose",comp)
            print("you won this round")
            your_turn_no+=1
        elif comp =='stone':
            print("computer choose",comp)
            print("oh you lose this round")
            computer_turn_no+=1

print("thanks for playing")
