while True:

    # Greet the user
    name = input("What is your name? ").strip().lower()
    print(f"Hello {name}!\nThis is a Number Guessing Game called Guess It Right!!! ")

    # Ask if they are ready to play
    ready = input(f"{name} you ready to play Guess It Right? [y] or [n] ")
    if ready != "y": 
        print("Maybe next time! Goodbye!")
        break

    # If they want to play, start the game
    print("Let's Guess away")
            
    # Ask user for low and high number 
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
    
            
       
