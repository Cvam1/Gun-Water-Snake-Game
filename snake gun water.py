import random

def get_computer_choice():
    """Return a random choice for the computer from 'Gun', 'Water', or 'Snake'."""
    choices = ['Gun', 'Water', 'Snake']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determine the winner based on the choices made by the player and computer."""
    if player_choice == computer_choice:
        return 'Tie'
    elif (player_choice == 'Gun' and computer_choice == 'Snake') or \
         (player_choice == 'Snake' and computer_choice == 'Water') or \
         (player_choice == 'Water' and computer_choice == 'Gun'):
        return 'Player'
    else:
        return 'Computer'

def main():
    """Main function to run the game."""
    print("Welcome to the Gun-Water-Snake game!")
    choices = ['Gun', 'Water', 'Snake']
    
    while True:
        player_choice = input("Enter your choice (Gun, Water, Snake): ").capitalize()
        
        if player_choice not in choices:
            print("Invalid choice. Please choose Gun, Water, or Snake.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(player_choice, computer_choice)
        if winner == 'Tie':
            print("It's a tie!")
        elif winner == 'Player':
            print("You win!")
        else:
            print("Computer wins!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
       
       
       
       

 


    