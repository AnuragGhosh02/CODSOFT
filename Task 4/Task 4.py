import random
print("Your options are: \nRock\nPaper\nScissor")
option=("Rock", "Paper", "Scissor")
a=True
while a:
    player=None
    computer=random.choice(option)
    while (player not in option):
        player=input("Enter your choice: ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if (player==computer):
        print("It's a tie!")
    elif(player=="Rock" and computer=="Scissor"):
        print("You win!")
    elif(player=="Paper" and computer=="Rock"):
        print("You win!")
    elif(player=="Scissor" and computer=="Paper"):
        print("You win!")
    else:
        print("Computer wins!")
    b=input("Do you want to play again? (y/n): ").lower()
    if not(b=="y"):
        a=False
print("Thank you for playing this game!")
