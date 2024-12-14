import game_logic.field_validation as field_validation
import game_logic.vote_winner as vote_winner

#Player information
player_info = {

    "player1" : {

        "score": 0 ,
        "name": ""
    },

    "player2" : {

        "score": 0 ,
        "name": ""
    }
}

Drwa_Round = vote_winner.Drwa_Round
Player1_Win_Round = vote_winner.Player1_Win_Round
Player2_Win_Round = vote_winner.Player2_Win_Round

def start_game ():

    # Get number of Round
    countOfRound = int(input("Enter the number of rounds: "))

    roundPalay = 1

    while roundPalay <= countOfRound :

        print(f"Round{roundPalay}") # Show the current Round

        player1 = input("player1 choice: ") # Get player1 choice

        # Validate player1
        if (not field_validation.validate_player(player1)):

            print("You entered the wrong entry")

            continue # ‌‌Back to round

        player2 = input("player2 choice: ") # Get player2 choice

         # Validate player2
        if (not field_validation.validate_player(player2)):

            print("You entered the wrong entry")

            continue # ‌‌Back to round

        # Drwa round
        if (vote_winner.winner_selector(player1, player2) == Drwa_Round):
            
            print ("The round was tied \n")

        # Player1 win the round
        if (vote_winner.winner_selector(player1, player2) == Player1_Win_Round):
            print ("Player1 win \n")

            player_info["player1"]["score"] +=1 # Change point player1
        
        # Player2 win the round
        if (vote_winner.winner_selector(player1, player2) == Player2_Win_Round):
    
            print ("Player2 win \n")

            player_info["player2"]["score"] +=1 # Change point player2

        roundPalay += 1
        




    
