import random

# List of valid choices
choices = ["rock", "paper", "scissors"]

# Get player input and convert to lowercase
player = input("Enter your choice (rock, paper, scissors): ").lower()

# Computer randomly picks from the choices list
computer = random.choice(choices)

# Display both choices
print(f"Your choice: {player}")
print(f"Computer choice: {computer}")

# Check for draw first (both chose the same)
if player == computer:
    print("It's a draw!")

# Check all winning combinations for the player
elif (player, computer) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
    print("You win!")

# If not a draw and not a win, player loses
else:
    print("You lose!")