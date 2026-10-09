import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS GAME =====")
print("First to 3 points wins!")
print("Type rock, paper, or scissors.")
print("Type quit to exit the game.")

while user_score < 3 and computer_score < 3:

    user = input("\nYour choice: ").lower().strip()

    if user == "quit":
        print("Game exited!")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score: You {user_score} - Computer {computer_score}")

if user_score == 3:
    print("\nCongratulations! You won the game!")

elif computer_score == 3:
    print("\nComputer won the game! Better luck next time!")

print("Thanks for playing!")
