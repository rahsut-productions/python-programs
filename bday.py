from turtle import Turtle, Screen
import turtle as t
import time
import os

t.hideturtle()
t.up()
t.back(300)
os.system("c:\\Users\\User\\Music\\punjabi_music\\Daler_Mehndi_Bolo_Ta_Ta_Ra.wav")
wn = Screen()

rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

while 1:
    t.color('red')
    time.sleep(0.25)
    t.clear()
    t.write("ਜਨਮ ਦਿਨ ਦਾ ਮੁਬਾਰਕਾ", font=("Arial", 50, "bold"))
    time.sleep(0.25)
    t.color('orange')
    t.clear()
    t.write("Happy Birthday :)", font=("Arial", 50, "bold"))
    t.color('yellow')
    time.sleep(0.25)
    t.clear()
    t.write("जन्मदिन की मुबारक", font=("Arial", 50, "bold"))
    time.sleep(0.25)
    t.color('green')
    time.sleep(0.25)
    t.clear()
    t.write("ਜਨਮ ਦਿਨ ਦਾ ਮੁਬਾਰਕਾ", font=("Arial", 50, "bold"))
    time.sleep(0.25)
    t.color('blue')
    time.sleep(0.25)
    t.clear()
    t.write("Happy Birthday :)", font=("Arial", 50, "bold"))
    time.sleep(0.25)
    t.color('purple')
    time.sleep(0.25)
    t.clear()
    t.write("जन्मदिन की मुबारक", font=("Arial", 50, "bold"))
    time.sleep(0.25)



