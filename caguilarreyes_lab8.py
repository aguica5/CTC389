#Carmen Aguilar-Reyes
#Lab 8 --story with 5 decisions and 3 options each

def playgame(): 
    name = input ("Welcome adventurer!What is your name?: ")

    print ("Hello", name, "you have discovered a mysterious island filled with ancient secrets.")
    print ("Your goal is to find the legendary Crystal to help you escape the island.")

    print ("You arrived at a fork in the path")

    print("1. Enter the jungle")
    print("2. Climb the mountain trail")
    print("3. Follow the beach")
    choice1 = input("Which path do you choose? ")


    if choice1 == "1":
        print(name, "enters the jungle.")
    elif choice1 == "2":
        print(name, "climbs the mountain trail.")
    elif choice1 == "3":
        print(name, "follows the beach.")
    else:
        print("You got lost and the adventure ends.")
        return

# Decision 2

    print("You discover an abandoned camp with three useful items.")
    print("1. Compass")
    print("2. Flashlight")
    print("3. Rope")
    choice2 = input("Which item do you take? ")


    if choice2 == "1":
        print("You take the compass.")
    elif choice2 == "2":
        print("You take the flashlight.")
    elif choice2 == "3":
        print("You take the rope.")
    else:
        print("You waste too much time and the adventure ends.")
        return 

# Decision 3

    print("Later, you reach a rushing river.")
    print("1. Swim across")
    print("2. Build a raft")
    print("3. Search for a bridge")
    choice3 = input("What do you do? ")

    if choice3 == "1":
        print("You carefully swim across.")
    elif choice3 == "2":
        print("You build a sturdy raft.")
    elif choice3 == "3":
        print("You find an old bridge and cross safely.")
    else:
        print("You fall into the river and lose the adventure.")
        return

# Decision 4

    print("You discover the entrance to an ancient temple.")
    print("1. Enter through the main gate")
    print("2. Use a hidden side entrance")
    print("3. Climb through a rooftop opening")
    choice4 = input("How will you enter? ")

    if choice4 == "1":
        print("You walk through the massive gate.")
    elif choice4 == "2":
        print("You sneak through the side entrance.")
    elif choice4 == "3":
        print("You climb into the temple from above.")
    else:
        print("You trigger a trap and lose.")
        return

# Decision 5

    print("Inside the temple are three crystal pedestals.")
    print("1. Red Crystal")
    print("2. Blue Crystal")
    print("3. Green Crystal")
    choice5 = input("Which crystal will you take? ")

    if choice5 == "1":
        print("The temple begins to glow!")

    elif choice5 == "2":
        print("The temple begins to glow!")
    elif choice5 == "3":
        print("The temple begins to glow!")
    else:
        print("The temple collapses before you make a choice.")
        return

# Decision 6

    print("You must escape the island.")
    print("1. Sail away on a boat")
    print("2. Fly away in an ancient airship")
    print("3. Use a hidden portal")
    choice6 = input("How will you escape? ")

    if choice6 == "1":
        print("Congratulations", name,  "! You sail away with the Crystal of Destiny and win!")
    elif choice6 == "2":
        print("Congratulations", name, "! You fly away with the Crystal of Destiny and win!")
    elif choice6 == "3":
        print("Congratulations", name, "! You step through the portal with the Crystal of Destiny and win!")
    else:
        print("You hesitate too long and remain trapped on the island.")

# Main game loop

play_again = "yes"

while play_again.lower() == "yes":
    playgame()
    play_again = input("\nWould you like to play again? ")

print("Thanks for playing!")

