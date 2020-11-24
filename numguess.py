'''guessing number
'''
import random
attempts_list = []
def view_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score.")
    else:  
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 20))
    print("Hello There! Welcome")
    player_name = input("what's your name? ")
    wanna_play = input("Hi {} ,Wanna play the game? (Yes/No)".format(player_name))

    attempts = 0
    view_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Guess the number between 1 to 20 ")
            if int(guess) < 1 or int(guess) > 20:
                raise ValueError("Enter the number within the given range") 
            if int(guess) == random_number:
                print("Great! You got it..")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                start_again = input("would you like to play again? Enter(Yes/No)")
                attempts = 0
                view_score()
                random_number = int(random.randint(1,20))
                if start_again.lower() == "no":
                    print("okay! Good one..")
                    break
            elif int(guess) > random_number: 
                print("A bit lower")
                attempts += 1
            elif int(guess)  < random_number:
                print("a bit higher")
                attempts += 1
        except ValueError as error:
            print("Oops! That's an invalid entry, try again")    
            print("({})".format(error))
    else:
        print("That's ok, Have a good one") 
if __name__ == '__main__':
    start_game()







