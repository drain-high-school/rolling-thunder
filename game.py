
# Yatzy

turns_left = 13  # A turn consists of three rolls.
current_hand = []

def roll_dice(dice_to_reroll):
    for roll in range(len(dice_to_reroll)):
        if roll == True:
            current_hand

def roll(rolls_left, current_hand):
    if rolls_left == 3:  # The user's turn just started, so roll the inital dice.
        current_hand = roll_dice([True, True, True, True, True])
        
    user_input = input("Which dice would you like to reroll? Press Enter to reroll none.")
