# This program uses Control Flow and Logical Operators to allow users to choose their own paths in finding a treasure.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# If the user wants to start over later in the game, we can loop it back here.
continue_game = True
real_game = True

while continue_game:
    while real_game:

        ################## USER FIRST CHOICE TRAIL ################################
        # Continue this loop if the user makes an invalid answer.
        check_answer = False
        while check_answer == False:
            # The first choice the user has to make.
            user_choice_route = input("Do you want to go through the left or right forest trail? ")
            # Convert the answer to lower case.
            user_choice_route = user_choice_route.lower()
            # If the user doesn't type left or right, prompt them back to the beggining of this loop.
            if user_choice_route == "left" or user_choice_route == "right":
                check_answer = True # Break out of the loop.
            else:
                print("Invalid response. Try again. ")

        # If the user picks "right", they will die and be prompted to start over if they want.
        if user_choice_route == "right":
            # User picks the wrong choice. Ask them if they want to try again. If yes, start over from the top.
            try_again = input("You fell into a trap hole and died. Try again? (Y = yes/ N = no) ")
            try_again = try_again.lower()
            if try_again == "n":
                break
        else :
            print("You hear the sounds of a river. You follow the sound. ")

        ################## USER SECOND CHOICE RIVER ################################
        river_proceed = False
        while river_proceed == False:
            # The second choice the user has to make.
            user_choice_river = input("You finally made your way towards the river. Do you swim or wait? ")
            # Convert the answer to lower case.
            user_choice_river = user_choice_river.lower()
            # Ask user again if the answer wasn't swim or wait
            if user_choice_river == 'swim' or user_choice_river == 'wait':
                river_proceed = True
            else:
                print("Invalid response. Try again. ")
        # River death/ try again.
        if user_choice_river == "swim":
            try_again = input("You swam out for about 15 minutes before you are washed away by the current. You are dead. Try again? (Y = yes/ N = no) ")
            try_again = try_again.lower()
            if try_again == "n":
                real_game = False
                continue_game = False
            else:
                break
        print("You wait by the river until the current slows down. You swim across the river safely.")

        ################## USER THIRD CHOICE DOOR ################################

        check_answer = False
        while check_answer == False:
            # The first choice the user has to make.
            user_choice_door = input("You stumbled upon TWO gold doors. Do you want to go through the left or right door? ")
            # Convert the answer to lower case.
            user_choice_door = user_choice_door.lower()
            # print(f"User choice = {user_choice_route}")
            # If the user doesn't type left or right, prompt them back to the beggining of this loop.
            if user_choice_door == "left" or user_choice_door == "right":
                check_answer = True # Break out of the loop.
            else:
                print("Invalid response. Try again. ")

        # If the user picks "right", they will die and be prompted to start over if they want.
        if user_choice_route == "right":
            # User picks the wrong choice. Ask them if they want to try again. If yes, start over from the top.
            try_again = input("You were ambushed by barbarians. You are dead. Try again? (Y = yes/ N = no) ")
            try_again = try_again.lower()
            if try_again == "n":
                break
        else :
            print("Congrats you found the treasure!!! ")
            continue_game = False
            real_game = False
print("Good bye.")



#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
