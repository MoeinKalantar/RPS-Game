import main_menu.game_starter as game_starter

playerInfo=game_starter.player_info # Get plyer info

def set_player_name(): # Set player name

    # Get player1 name
    playerInfo["player1"]["name"] = input("Player1 enters your name : ") 

    # Get player2 name
    playerInfo["player2"]["name"] = input("Player2 enters your name : ") 

def validate_player_names(): # Validation to enter name

    if(playerInfo["player1"]["name"] == "" or playerInfo["player2"]["name"] == ""): 

        print("Please enter your name \n")

        return True # Name is empty
    
    return False # Full name
