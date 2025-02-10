import random


while True:
    def displayIntro(): # Start game from start
    # Greet the user
        name = input("What is your name? ").strip().lower()
        print(f"Hello {name}!\nThis is a Number Guessing Game called Guess It Right!!! ")

        # Ask if they are ready to play
        ready = input(f"{name} you ready to play Guess It Right? [y] or [n] ")
        if ready != "y": 
            print("Maybe next time! Goodbye!")
            

        # If they want to play, start the game
        print("Let's Guess away")
                
        # Ask user for low and high number 
        while True: 
            invalid = True

            while invalid:
                try: 
                    low_number = int(input("Enter the lowest number for the range: ").strip())
                    high_number = int(input("Enter the highest number for the range: ").strip())
                except ValueError:
                    print("Only type integers!")
                else: # when there is no error
                    invalid = False
                    if high_number > low_number:
                        break 
                    print("The highest number must be greater than the lowest number. Try again.")
                
        # Ask for the number of attempts 
            invalid = True

            while invalid:
                try: 
                    guess =  int(input("Enter the amount of guess you want:  "))         
                except ValueError:
                    print("Only type integers!")
                else: invalid = False

        # Generate a random number
            secret_number = random.randint(low_number, high_number)

        
        # try something but not working ask Mr.kung
            guess = 0 
            print(" You have no more attempts left.")
            try_agian_lost = input(f"The number was {secret_number} . Do you want to play again? [y] or [n]")
            if try_agian_lost != "y":   
                displayIntro()
            else:
                try_agian_lost == "n"
                print(f"Thanks for playing Guess it right {name}!!! ")

    displayIntro()
        # Loop for guess attempts


