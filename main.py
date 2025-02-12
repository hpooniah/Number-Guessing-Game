import random

while True:
        # Greet the user
        name = input("What is your name? ").strip().lower()
        print(f"Hello {name}!\nThis is a Number Guessing Game called Guess It Right!!! ") # introducing the game

        # Ask if they are ready to play
        ready = input(f"{name} you ready to play Guess It Right? [y] or [n] ").strip().lower()
        if ready != "y": 
            print("Maybe next time! Goodbye!") # they dont want to play the game
            exit() # closes the game

        # If they want to play, start the game
        print("Guess away")
                        
        # Ask user for low and high number 
        def displayIntro(): # Start game from start
            while True:
                try: 
                    low_number = int(input("Enter the lowest number for the range: ").strip())
                    high_number = int(input("Enter the highest number for the range: ").strip())
                    if high_number > low_number:
                        break
                    print("The highest number must be greater than the lowest number. Try again.")
                except ValueError:
                    print("Only type integers!")

            # Ask for the number of attempts 
            while True:
                try: 
                    number_attempts =  int(input("Enter the amount of attempts you want: "))         
                    break
                except ValueError:
                    print("Only type integers!")
                
            # Generate a random number
            random_number = random.randint(low_number, high_number)

            attempts_used = 0 

            # Loop for guess attempts

            while attempts_used < number_attempts:
                try:
                    print(f"Guess a number between {low_number} and {high_number}.")
                    guess = int(input(f"{number_attempts - attempts_used} attempts remaining - Enter a guess for the random number: "))
                except ValueError:
                    print("Only type integers!")
                    continue 

                attempts_used += 1

                #Tell the user if the guess is to low, high, or he guessed it right
                if guess < random_number: 
                    print("Your guess is too low, give it another shot")
                elif guess > random_number:
                    print ("Your guess is too high, give it another shot")
                else: 
                    print(f"You did it!, You guess the correct number {random_number}\nYou had {number_attempts - attempts_used} attempts remaining")
                    break
            else:
                print(f"You have no more attempts left. The correct number was {random_number}.")
                                    
            # Ask the user if they want to play again
            try_again = input("Do You Wish to play Guess It Right again? [y] or [n]").strip().lower()
            while try_again not in ["y", "n"]:
                try_again = input("Please enter y for yes and n for no").strip().lower()
                                
            if try_again != "n":
                displayIntro()
            if try_again != "y":
                print(f"Thanks for playing Guess it right {name}!!! ")
                exit()

        displayIntro()