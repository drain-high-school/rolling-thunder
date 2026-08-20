
# Yatzy

import random

turns_left = 13  # A turn consists of three rolls.
current_hand = [0,0,0,0,0]

def roll_dice(current_hand, dice_to_reroll):
    for roll in range(len(dice_to_reroll)):
        if dice_to_reroll[roll] == True:
            current_hand[roll] = random.randint(1,6)
    return current_hand
    
def choose_category():
    pass

def roll(rolls_left, current_hand):
    
    dice_to_reroll = [False, False, False, False, False]
    
    if rolls_left == 3:  # The user's turn just started, so roll the inital dice.
        current_hand = roll_dice(current_hand, [True, True, True, True, True])
        rolls_left -= 1
        print(current_hand)

    while rolls_left != 0:
        dice_to_reroll = [False, False, False, False, False]
        user_input = input("Which dice would you like to reroll? Press Enter to reroll none, else separate with spaces.")
        if user_input == "":
            rolls_left = 0
        else:
            for i in user_input:
                if i != " ":
                    dice_to_reroll[int(i)-1] = True
            rolls_left -= 1
        roll_dice(current_hand, dice_to_reroll)

roll(3, current_hand)
