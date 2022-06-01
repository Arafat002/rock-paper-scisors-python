import random

comp_wins = 0
player_wins =0

def Choose_Options():
    user_choice = input("Choose Rock, Paper or Scissors:")
    if user_choice in ["Rock", "rock", "r", "r"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P" ]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("Error,Please try again.")
        Choose_Options()
    return user_choice
def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice
while True:
    print("")
    user_choice = Choose_Options()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("you chose rock. The computer chose rock. you tied.")
        elif comp_choice == "p":
            print("you chose scissors. The computer chose paper. you win.")
            player_wins += 1
        elif comp_choice == "s":
            print("you chose scissors. The computer chose scissors. you tied.")

    print("")
    print("player wins: " + str(player_wins))
    print("computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (yes/no)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "No", "no"]:
        break
    else:
        break
