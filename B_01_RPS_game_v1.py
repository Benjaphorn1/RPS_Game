#Checks for an integer mroe than 0 (allows <enter>
def int_checker(question):
    """checks users enters an integer more than/equal to 1"""

    error = "please enter an integer that is 1 or more"

    while True:

        to_check = input(question)

        #check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            if response < 1:
               print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine starts here

# Initialise game variable
mode = "regular"
rounds_played = 0

print()
print("🪨📄✂️ Rock Paper Scissors ✂️📄🪨️")

#sk user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push enter for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#Game loop start here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds played:", rounds_played)

    #if users are mode infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)

#Game loop ends here

# Game history / Statistics area