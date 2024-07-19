import random
import time

#prinr_pause function to make 2 seconds delay between printing each line
def print_pause(*s):
    for word in s:
        time.sleep(1)
        print(word)


# Global score
score = 0
#turns
turns = 0

# What does (friend) give to Dora
reward = ['jar of cookies', 'bag full of candy', 'donut', 'jar of biscuits']
random_reward = random.choice(reward)

# Who does Dora meet
friend = ["John", "Tom", "Nate", "Diego"]
friend_random = random.choice(friend)

#to print the player's score after every action
def total_score():
    global score
    print_pause(f"Your total score is: {score} SP")

#After each encounter this function checks if the player's score >= 25 if it does you win imedietly
def check_win():
    global score
    if score >= 25:
        print_pause(f"CONGRATULATIONs!!, YOU WON :with {score} SP", 
        "and successfully reached your grandma's house, and she is very happy."
        )
        play_again()

#to check the number of turns if it >=5 ,The adventure ends.
def check_turns():
    global turns
    if turns >= 5:
        final_outcome()
        play_again()
        
       

#explains your sitiuation(first encounter)
def intro():
    global score, turns
    print_pause(
        "Your name is Dora. You are going to visit your grandma in the woods.",
        "First, you encounter a small water spring.",
        "1. Cross it on your legs",
        "2. Try to jump on some rocks to cross",
        "3. Open your map to find another way"
    )
    choice = input("Choose 1, 2, or 3: ")
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid input, please try again? [1/2/3]: ")
    if choice == "1":
        score -= 5
        print_pause("You got wet, losing 5 SP.")
    elif choice == "2":
        score -= 10
        print_pause("You fell and got hurt, losing 10 SP.")
    elif choice == "3":
        score += 10
        print_pause(
            "The map showed you a nearby bridge and you crossed it, gaining 10 SP."
        )
    turns += 1
    total_score()
    check_win()
    check_turns()

#second encounter "you bumb into your friend"
def second_encounter():
    global score, reward, random_reward, friend, friend_random, turns
    print_pause(
        f"You bump into your friend {friend_random}, who asks for your help to get his cat stuck on a tree.",
        "1. Help him get his cat",
        "2. Ignore him"
    )
    choice = input("Choose 1 or 2: ")
    while choice not in ["1", "2"]:
        choice = input("Invalid input, please try again? [1/2]: ")
    if choice == "1":
        score += 5
        turns += 1
        print_pause(f"{friend_random} is grateful for you, gained 5 SP.")
        total_score()
        print_pause(
            "Now you need to get the cat down.",
            "1. Throw a stone",
            f"2. Sing the bag song and see how it can help you to get {friend_random}'s cat")
        choice = input("Choose 1 or 2: ")
        while choice not in ["1", "2"]:
            choice = input("Invalid input, please try again? [1/2]: ")
        if choice == "1":
            score -= 10
            turns += 1
            print_pause(
                f"The cat scratched you and {friend_random} got mad. You lost 10 SP but got a {random_reward}."
            )
        elif choice == "2":
            score += 10
            turns += 1
            print_pause("The bag gave you a ladder and you used it to get the cat.")
            print_pause(f"{friend_random} is very happy and gave you a {random_reward}.")
    elif choice == "2":
        score -= 5
        turns += 1
        print_pause(f"You ignored {friend_random} and he got really upset. You lost 5 SP.")
    total_score()
    check_win()
    check_turns()

#third encounter (swiper stealing your gift)
def third_encounter():
    global score, turns
    print_pause(
        "You continue your journey and meet Swiper, who tries to steal your gift to grandma.",
        "1. Say 'Swiper, don't steal' 3 times",
        "2. Run away"
    )
    choice = input("Choose 1 or 2: ")
    while choice not in ["1", "2"]:
        choice = input("Invalid input, please try again? [1/2]: ")
    if choice == "1":
        score += 10
        print_pause("You said 'Swiper, don't steal' 3 times and Swiper goes away. You gained 10 SP.")
    elif choice == "2":
        score -= 10
        print_pause("You ran away and lost grandma's gift, losing 10 SP.")
    turns += 1
    total_score()
    check_win()
    check_turns()

#forth encounter(boots riddle)
def forth_encounter():
    global score, turns
    print_pause("Your friend boots wants to challenge you with a riddle",
    "The Riddle: I have keys but open no locks. I have space but no room. You can enter, but you can't go outside. What am I? ",
    "1. Piano",
    "2. keyboard")
    choice = input("Choose 1 or 2: ")
    while choice not in ["1", "2"]:
        choice = input("Invalid input, please try again? [1/2]: ")
    if choice == "1":
        score -= 5
        print_pause("'wrong answer'boots said laughing")
    elif choice == "2":
        score += 10
        print_pause("correct answer, boots cheered for you.")
    turns += 1
    total_score()
    check_win()
    check_turns()

#another riddle
def fifth_riddle():
    global score, turns
    print_pause("You got excited for another riddle ",
    "boots wants to beat you, you have to win this",
    "The Riddle: 'What has a head, a tail, but does not have a body?'",
    "1. snake",
    "2. coin")
    choice = input("Choose 1 or 2: ")
    while choice not in ["1", "2"]:
        choice = input("Invalid input, please try again? [1/2]: ")
    if choice == "1":
        score -= 5
        print_pause("'wrong answer'you're so sad")
    elif choice == "2":
        score += 10
        print_pause("correct answer, boots cheered for you.")
    turns += 1
    total_score()
    check_win()
    check_turns()
   


def final_outcome():
    global score, turns
    print_pause(
        "Your adventure is over",
        f"Your final score is: {score} SP, Turns = {turns}"
    )
    if score >= 25:
        print_pause(
            "CONGRATULATION!!, YOU WON!, You successfully reached your grandma's house, and she is very happy."
        )
    else:
        print_pause("unfortunetly, you lost",
            "You couldn't reach your grandma's house and had to go back home."
        )


def adventure_game():
    global score, reward, random_reward, friend, friend_random, turns
    intro()
    second_encounter()
    third_encounter()
    forth_encounter()
    fifth_riddle()


#askes the player to play again
def play_again():
    while True:
        play = input("Do you want to play again? [yes/no]: ").lower()
        if play == "yes":
            global score
            score = 0  # Reset the score
            turns = 0  # Reset turns
            adventure_game()
        elif play == "no":
            print("Thank you for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'?")

#game call
adventure_game()
play_again()
