import random
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

 Then play against computer. You need to choose R (rock), 
 P (Paper) or S (Scissors).

 The rules are as follows:
o Paper beats rock
o Rock beats scissors
o Scissors beats paper

Good Luck!
    """)


#Checks for an integer more than 0 (allows <enter>
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


# Compare users and comp choice
# result win/lose/tie
def rps_compare(user, comp):

    # if user and computer choice the same, its tie
    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"

    # if it's not win/ tie its lose
    else:
        round_result = "lose"

    return round_result


# Main routine starts here

# Initialise game variable
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock","paper","scissor", "xxx"]

game_history = []

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

    # randomly choose from the rps list except the exit code
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice:", comp_choice)

    if user_choice == "xxx":
        break



    result = rps_compare(user_choice, comp_choice)

    #Adjust game lost / game tied counters and add results in game history
    if result == "tie":
        rounds_tied =+ 1
        feedback = "👔👔👔 It's a tie! 👔👔👔"
    elif result == "lose":
        rounds_lost =+ 1
        feedback = "😢😢 You lose. 😢😢"
    else:
        feedback = "👍👍 You won! 👍👍"

    #Set up round feedback and output it user
    # Add it to the game history list (include the round number)
    round_feedback =  f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    #if users are mode infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

#Game loop ends here

# Ask user if they want to see game history
want_history = string_checker("Do you want to see game history? ")

# output history if user says yes
if want_history == "yes":
    print("\n---Game History---")
    for item in game_history:
        print(item)
    print()

# Game history / Statistics area
rounds_won = rounds_played - rounds_tied - rounds_lost
percent_won =  rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
percent_tied = 100 - percent_won - percent_lost

# Output game statistics
print("📊📊📊 Game Statistics 📊📊📊")
print(f"👍 Won: {percent_won:.2f} \t "
      f"😢 Lost: {percent_lost:.2f} \t "
      f"👔 Tied: {percent_tied:.2f}")