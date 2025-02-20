# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            #check if the user response is the same
            #as the first letter of an item in a list
            elif user_response == item[0]:
                return item

        #print error message if something isn't valid
        print(error)
        print()


def instructions():
    """prints instructions"""

    print("""
 *** Instructions ***

 To begin choose the number of rounds(or play
 infinite mode)

 Then play agaisnt computer. You need to choose R (rock), 
 P (Paper) or S (Scissors).

 The rules are as follows:
o Paper beats rock
o Rock beats scissors
o Scissors beats paper

Good Luck!
    """)


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

rps_list = ["rock","paper","scissor", "xxx"]

print("🪨📄✂️ Rock Paper Scissors ✂️📄🪨️")
print()

# ask user if they want instructions
want_instructions = string_checker("Do you want to see instructions? ")

#if user says yes display instructions
if want_instructions == "yes":
    instructions()


#sk user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#Game loop start here
while rounds_played < num_rounds:

    #Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n ♾️♾️♾️ Round {rounds_played + 1} (Infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    user_choice = string_checker("Choose: ", rps_list)
    print("you chose:", user_choice)

    if user_choice == "xxx":
        break

    rounds_played += 1

    #if users are mode infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

#Game loop ends here

# Game history / Statistics area