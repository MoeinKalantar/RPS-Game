#To validate the value in the list

def validate_player (value):

    valid_value = ["rock", "paper", "snips"] # Player choose

    if (value in valid_value):

        return True
    
    return False 