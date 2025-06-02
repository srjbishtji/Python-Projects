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

selected = ['easy : 1', 'medium : 2', 'hard : 3']
print(selected)
choice = int(input("select your choice from 1 to 3 : "))
maximum = 3
end = 0 
if choice == 1 :
    maximum = 3
    end = 100
    maxi = 100
elif choice == 2 : 
    maximum = 5
    end = 500
    maxi = 500
else: 
    maximum =  7
    end = 1000
    maxi = 1000
    
guessing_number = random.randint(1,end)
game_over = False
attempt = 1


while not game_over and attempt <= maximum:
    number = int(input(f"Guess the number between 1 to {maxi} : "))
    if number == guessing_number:
        print("You guessed it correct")
        game_over = True
    else:
        if number > guessing_number:
            print("Too High")
        else:
            print("Too low")
        attempt += 1
if not game_over:
    print("Maximum number of attempts completed")
        