#Carmen Aguilar-Reyes
#Lab 7 EC Part 2

def guessgame(): 
    mynumber = 3

    guess = int(input("Guess my number: "))

    while abs (guess-mynumber)<= 2 and guess != mynumber: 
        guess = int(input("Close, try again: "))

    if guess == mynumber: 
        print ("well done! You guessed my number ...yay!!")
    else: 
        if guess > mynumber: 
            print ("Sorry, you lost. Your guess was higher than my number which is", mynumber)
        else: 
            print ("Sorry, you lost. Your guess was lower than my number which is", mynumber)

playagain = input ("Would you like to play my game? Type yes or no.")

while playagain == "yes": 
    guessgame()
    playagain = input ("Would you like to play my game? Type yes or no.")


