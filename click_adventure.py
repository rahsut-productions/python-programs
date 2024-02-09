from tkinter import *
tk = Tk()

# Functions
def no(): # A dummy command
    pass

def leave(): # Destroys window
    tk.destroy()
## The click functions below move the "program" along
    
def click16():
    credit1 = Label(tk,text="Made by Tushar Passi \n\
    ਤੁਸ਼ਾਰ ਪਾਸੀ ਨੇ ਬਣਾਇਆ")
    credit = Label(tk, text="Program Language: English \n\
    ਪ੍ਰੋਗ੍ਰਾਮ ਦਾ ਭਾਸ਼ਾ: ਅੰਗ੍ਰੇਜ਼ੀ")
    credit.pack()
    credit1.pack()
    Exit = Button(text="Exit", command=leave)
    btn.configure(command=no)
    Exit.pack()

def click15():
    btn.config(text="Wait a minute... cake?", command=click16)

def click14():
    btn.config(text="Click me", command=click15)
    btn1.config(text="fake Click me 1", command=click15)
    btn2.config(text="fake Click me 2", command=click15)
    btn3.config(text="cake Click me 3", command=no)

def click13():
    btn1.config(text="Deal!", command=click14)
    btn2.config(text="Deal!", command=click14)
    btn3.config(text="Deal!", command=click14)

def click12():
    btn.config(text="Fine you can live here but I'm still the real 'Click me' button", command=click13)

def click11():
    btn1.config(text="Nooooo. I have no where else to go.", command=click12)
    btn2.config(text="Me too, please let us live here.", command=click12)
    btn3.config(text="Yeah! Plz King *real* Click me button", command=click12)

def click10():
    btn.config(text="Now, the rest of you get out!", command=click11)

def click9():
    btn.config(text="See, I'm the real 'Click me' button", command=click10)
    
def click8():
    btn.config(text="Paper", command=click9)
    btn1.config(text="Rock", command=no)
    btn2.config(text="Rock", command=no)
    btn3.config(text="Rock", command=no)
def click7():
    btn.config(text="Rock, Paper, Sicssors...", command=click8)
    btn1.config(text="Rock, Paper, Sicssors...", command=click8)
    btn2.config(text="Rock, Paper, Sicssors...", command=click8)
    btn3.config(text="Rock, Paper, Sicssors...", command=click8)

def click6():
    btn1.config(text="all righty", command=click7)
    btn2.config(text="I like this", command=click7)
    btn3.config(text="Ok let's do it", command=click7)
    
def click5():
    btn.config(text="Let's just play Rock Paper Sicssors to decide who's real.", command=click6)

def click4():
    btn.config(text="Shut up", command=click5)
    btn3.config(command=no)
    
def click3():
    global btn3
    btn3 = Button(tk, text="No, I am the real one.", command=click4)
    btn2.config(command=no)
    btn3.pack()
    
def click2():
    global btn2
    btn1.config(command=no)
    btn2 = Button(tk, text="No, I'm the real 'Click me' button.", command=click3)
    btn2.pack()
def click():
    global btn1
    btn.config(command=no)
    btn1 = Button(tk, text="I'm the real 'Click me' button", command=click2)
    btn1.pack()

# This is the first button. 
btn = Button(tk, text="Click me", command=click)   
btn.pack()
