import random
choices = ["rock", "paper", "scissor"]
print("Welcome to Rock, Paper, Scissor Game!")
while True:
    user = input("Enter Your Choice(rock, paper or scissor) ? : ").lower()
    computer = random.choice(choices)

    print("Computer choice:", computer)

    if user == computer:
        print("Tie!")
    elif (user == "rock" and computer == "scissor") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissor" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
    print()
    again = input("Play again ? (yes/no): ")
    if again.lower() != "yes":
        break
print("Thanks for playing!")
