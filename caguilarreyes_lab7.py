#Carmen Aguilar-Reyes
#Lab7 EC

mynumber = 3

guess = int(input("Guess my number: "))

while abs(guess-mynumber) <= 2 and guess != mynumber: 
    guess = int(input("Close, try gain: "))

if guess ==mynumber: 
    print ("well done! You guessed my number")
else: 
    if guess>mynumber: 
        print ("Sorry, you lost. Your guess was higher than my number which is", mynumber)
    else: 
        print ("Sorry, you lost. Your guess was lower than my number which is", mynumber)


