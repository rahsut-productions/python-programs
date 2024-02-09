import time
from tkinter import *

class Game: # Game Class
    def __init__(self, name, days, stamina, strength):
        # the init function has the name of user, days left for user in game,
        # stamina left for user in game, strength left for user in the game
        self.name = name
        self.days = days
        self.stamina = stamina
        self.strength = strength
        global tk
        tk = Tk()


    global gameCode 
    def gameCode(): # the game code 
        if user.strength < 1: # if strenth is < 1, then set user's strength to 0
            user.strength = 0
        if user.stamina < 1: # if stamina is < 1, then set user's strength to 0
            user.stamina = 0
        print(user.days, "days left.", user.stamina, "stamina left. And", \
              user.strength, "strength left.")
        # ^ prints how much of everything left
        if user.days == 0: # if no more days are left
            print("Final score:", user.stamina, "stamina and", user.strength, \
                      "strength.")
            print("")
            print("Game will exit in 10 seconds")
            time.sleep(10) 
            exit()
            tk.destroy()
            tk.deiconify()
        if user.stamina > 100: # if the user has too much stamina
            print("You got too lazy. \n\
                    GAME OVER")
            time.sleep(3)
            exit()
            tk.destroy()
        if user.stamina < 1: # if the user has 0 stamina, game over
            print("No more stamina left. \n\
    GAME OVER")
            time.sleep(3)
            exit()
        if user.strength < 1:  # if user has 0 strength, game over
            print("No more strength left. \n\
    GAME OVER")
            time.sleep(3)
            exit()
        tk.deiconify()

    
    global run
    def run(): #if the player wants to run; function
        tk.withdraw()
        for x in range(1, 4):
            print("Running...")
            time.sleep(1)
        user.days = user.days - 1
        user.stamina = user.stamina - 15
        user.strength = user.strength + 15
        gameCode()

        
    global sleep
    def sleep(): # if the player wants to sleep; function
        tk.withdraw()
        for x in range(1, 4):
            print("Sleeping..")
            time.sleep(1)
        user.days = user.days - 1
        user.stamina = user.stamina + 15
        user.strength = user.strength - 10
        gameCode()

askforName = input("What is your name?: ")

while len(askforName) > 20 or len(askforName) < 2: # if name too long/short
        print("")
        print("Your name is too long/short.")
        print("")
        askforName = input("What is your name?: ")

if askforName: # if the computer asked for name 
    user = Game(askforName, 7, 50, 25)
    print("Hello", user.name, " , let's start the simulator.")
    print("")
    print("Directions: \n\
\n\
If the days left are 0, you lose. \n\
If the stamina is over 100, you lose because you start getting lazy for \n\
no good reason. If your strength reaches 0, you lose as well.  \n\
\n\
Try to get the most strength as possible.")
    print("")
    print("Would you like to run or sleep? \n\
\n\
7 days left. 50 stamina left. 25 strength left.")

btn = Button(tk, text="Sleep", command=sleep) # makes buttons 
btn.pack()
btn = Button(tk, text="Run", command=run) # makes buttonss
btn.pack()
