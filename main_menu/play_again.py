import main_menu.game_starter as game_starter


def play_again(): # Play again

    while True :

        # Get answer for play again
        playAgain = input("Do you want play again ? (yes/no) : ").lower() 

        if(playAgain == "yes"):

            game_starter.start_game()

            continue # Yes for play again
        
        break # No or other answers