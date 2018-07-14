import random #for random number generation

rand_num = random.randrange(0,100) #random number(within range 0 to 100) is generated and stored
guessCheck = "wrong" #for contolling the loop

print("Welcome to Number Guess")

#loop
while guessCheck == "wrong":
    user_input = int(input("Please input a number between 0 and 100:")) #user input is taken as integer
    
    #checks for the correctness of guess
    if user_input < rand_num:
        print("Its Lower than actual number. Try Again.") #if guess is lower again executes the loop
    elif user_input > rand_num:
        print("Its Higher than actual number. Try Again.") #if guess is higher again executes the loop
    else:
        print("Bravo, You Got It!")
        guessCheck = "correct" #if guess is correct terminates loop by updating value of loop variable 

print("Thank You for Playing Number Guess. See You Again") #executes when loop terminated
        
