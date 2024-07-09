import random

# Function to get user's choice
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

# Function to get computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner of a single round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to display choices and result
def display_choices_and_result(user_choice, computer_choice, result):
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        result = determine_winner(user_choice, computer_choice)
        display_choices_and_result(user_choice, computer_choice, result)
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        # Display current score
        print(f"Your score: {user_score} | Computer's score: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thankyou for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()