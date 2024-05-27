import random
from enum import Enum

# Enum with the values rock paper and scissors
class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        return self.name.lower()


# Function to get the user move
def get_user_move():
    error_message = "Invalid move. Please enter 1, 2, 3 or the move name."
    while True:
        user_input = input("Enter your move (1: rock, 2: paper, 3: scissors or the move name): ")
        try:
            if user_input.isdigit():
                move = Move(int(user_input))
            else:
                move = Move[user_input.upper()]
            return move
        except (ValueError, KeyError):
            print(error_message)


# Function to get the computer move
def get_computer_move():
    return random.choice([Move.ROCK, Move.PAPER, Move.SCISSORS])


# Function to determine the winner
def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "It's a tie!"
    elif (user_move == Move.ROCK and computer_move == Move.SCISSORS) or \
         (user_move == Move.PAPER and computer_move == Move.ROCK) or \
         (user_move == Move.SCISSORS and computer_move == Move.PAPER):
        return "You win!"
    else:
        return "You lose!"


# Main function
def main():
    try:
        print("Welcome to Rock, Paper, Scissors!")
        computer_score = 0
        user_score = 0
        while True:
            user_move = get_user_move()
            computer_move = get_computer_move()
            print(f"Your move: {user_move.name}")
            print(f"Computer move: {computer_move.name}")
            
            result = determine_winner(user_move, computer_move)
            print(result)
            
            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1
                
            print(f"Score: You {user_score} - {computer_score} Computer")
    except KeyboardInterrupt:
        print("\nThank you for playing Rock, Paper, Scissors!")


if __name__ == "__main__":
    main()

