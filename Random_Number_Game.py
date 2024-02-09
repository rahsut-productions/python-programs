import random
import time
# Opening to game 
print("Game made by Tushar Passi ਤੁਸ਼ਾਰ ਪਾਸੀ ਨੇ ਗੇਮ ਬਣਾਇਆ")
print("To continue through dialouge, press 'Enter'")
print("")
print("Welcome to the Random Number Game, in this game you have to guess what\n\
number the computer picked!")
print("")
difficulty = input("Easy mode or Hard mode? (Easy/Hard): ")
while difficulty != "Easy" and difficulty != "Hard":
    print("Invalid response. Try again.")
    difficulty = input("Easy mode or Hard mode? (Easy/Hard): ")


# If easy mode is chosen

if difficulty == "Easy":
    i = random.randint(1, 100)
    print("Picking the number..")
    time.sleep(1)

while difficulty == "Easy":
    guess = input("What number from 1-100 did the computer pick?: ")
    if int(guess) == i:
        print("You won mate! ਤੁਸੀਂ ਜਿਤਗੇ!")
        break
    if int(guess) < i:
        print("Try higher.")
    if int(guess) > i:
        print("Try lower.")
        
    

# If Hard mode chosen

if difficulty == "Hard":
    i = random.randint(1, 10)
    print("Picking the number..")
    time.sleep(1)
    guess = input("What number did the computer pick from 1-10: ")
    if guess != str(i):
        print("You were wrong, but don't worry, try again. You have 2 more chances.")
        guess = input("What number did the computer pick from 1-10: ")
    if guess != str(i):
        print("You were wrong, but don't worry, try again. You have 1 more chance.")
        guess = input("What number did the computer pick from 1-10: ")
        print("")
    if guess == str(i):
        print("Correct!")
    if guess != str(i):
        print("You were wrong, but don't feel sad. You can restart the game and \n\
play again :)")
        print("")
        print("You guessed:", guess)
        print("But the computer picked:", i)


