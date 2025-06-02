# CORE LOGIC 

# import random
# guessing_number = random.randint(1,100)
# number = int(input("Guess the number between 1 to 100 : "))
# game_over = False
# while not game_over:
#     if number == guessing_number:
#         print("You guessed it correct")
#         game_over = True
#     else:
#         if number > guessing_number:
#             print("Too High")
#         else:
#             print("Too low")
#         number = int(input("Guess the number between 1 to 100 : "))



# Adding Functionalites


import random

print("Difficulty")
selected = ['Easy : 1', 'Medium : 2', 'Hard : 3']
print(selected)
print("Choose Difficulty Level:")
print("1 - Easy (1 to 10, 3 attempts)")
print("2 - Medium (1 to 50, 5 attempts)")
print("3 - Hard (1 to 100, 7 attempts)")


while True:
    try: 
        choice = int(input("select your choice from 1 to 3 : "))
        end = 0 
        if choice == 1 :
            maximum = 3
            end = 10
            maxi = 10
            difficulty = "Easy"
        elif choice == 2 : 
            maximum = 5
            end = 50
            maxi = 50
            difficulty = "Medium"
        else: 
            maximum =  7
            end = 100
            maxi = 100
            difficulty = "Hard"

        guessing_number = random.randint(1,end)
        game_over = False
        attempt = 1

        while not game_over and attempt <= maximum:
            while True:
                number = int(input(f"Guess the number between 1 to {maxi} : "))
                if number < 1 or number > maxi:
                    print(f"Please enter a number between 1 and {maxi}")
                else:
                    break  

            if number == guessing_number:
                print(f"Correct! You guessed the number in {attempt} attempt(s).")
                game_over = True
            else:
                if number > guessing_number:
                    print("Too High")
                else:
                    print("Too low")
                attempt += 1

        if not game_over:
            print("Maximum number of attempts completed")

        with open("game_history.txt", "a") as file:
            if game_over:
                result = f"Difficulty: {difficulty}, Result: Win, Attempts: {attempt}\n"
            else:
                result = f"Difficulty: {difficulty}, Result: Loss, Correct Number: {guessing_number}\n"
            file.write(result)
        
        play = input("Do you want to play again (yes/no) : ").lower()
        # if play == "yes": 
        #     pass
        # else:
        #     print("Thanks for playing!")
        #     break
        if play != "yes":
            print("Thanks for playing!")
            break

    except ValueError:
        print("Invalid input! Please enter a valid integer.")