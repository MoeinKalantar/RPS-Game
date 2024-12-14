# Winner Selector

Drwa_Round = "0"
Player1_Win_Round = "1"
Player2_Win_Round = "2"

def winner_selector (player1, player2):
    
    if (player1 == player2):

        return Drwa_Round # Draw round
    
    elif(player1 == "rock" and player2 == "snips"):

        return Player1_Win_Round #Player1 win the round 
    
    elif(player1 == "snips" and player2 == "paper"):

        return Player1_Win_Round #Player1 win the round 
    
    elif(player1 == "paper" and player2 == "rock"):

        return Player1_Win_Round #Player1 win the round 
    else:
        
        return Player2_Win_Round #Player2 win the round 
