import main_menu.add_player as add_player
import main_menu.game_starter as game_starter
import main_menu.play_again as play_again
import main_menu.show_scores as show_scores


playerInfo = game_starter.player_info

Menu_Add_Player = "1"
Menu_Start_Game = "2"
Menu_Show_Scores = "3"
Menu_Exit = "4"

while(True):

    # Show Main Menu
    print("Add Player : 1") 
    print("Start Game : 2")
    print("Show Scores : 3")
    print("Exit : 4 \n")

    selectedMenu = input("Choose : ") # Get the user choose 

    if(selectedMenu == Menu_Add_Player): # Add Player

        add_player.set_player_name() 

        continue # Back to Main Menu
    
    elif(selectedMenu == Menu_Start_Game): # Start Game

         # Check empty name or full name
        if(add_player.validate_player_names()):
        
            continue # Back to Main Menu

        game_starter.start_game()
                
        play_again.play_again()
        
        continue # Back to Main Menu

    elif(selectedMenu == Menu_Show_Scores): # Show Scores

        # Check empty name or full name
        if(add_player.validate_player_names()): 
        
            continue # Back to Main Menu

        show_scores.show_player_info()

        continue # Back to Main Menu
    
    elif(selectedMenu == Menu_Exit): # Exite

        break # Exit Main Menu

    else: # another Choose

        print("Please choose correctly \n")
        
        continue # Back to Main Menu