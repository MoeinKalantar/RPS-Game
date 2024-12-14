import main_menu.game_starter as game_starter

playerInfo=game_starter.player_info # Player information

def show_player_info(): # Show Player information

    print(f"Player1(Name) : {playerInfo["player1"]["name"]}") # Player1 name
    print(f"Player1(score) : {playerInfo["player1"]["score"]}") # player1 score

    print(f"Player2(Name) : {playerInfo["player2"]["name"]}") # Player2 name
    print(f"Player2(score) : {playerInfo["player2"]["score"]} \n") # player2 score

