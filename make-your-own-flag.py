from tkinter import *
import turtle as t
from tkinter import messagebox

# Setting up the tkinter window
tk = Tk()
tk.title("Make your own flag!")
tk.geometry("200x475")


# Functions
def canvas():
    tk.withdraw()
    t.reset()
    t.hideturtle()
    t.clear()
    t.home()
    # positions turtle at centre
    t.back(175)

    # makes rectangle
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(200)
      t.left(90)

    t.up()
    tk.deiconify()

def stripes():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.left(90)
    t.up()
    t.forward(200)
    
    # stripes
    t.color('#B22234')
    t.right(90)
    t.forward(175)
    t.right(90)
    t.down()

    stripe = 14.3

    for x in range(1, 5):
        t.begin_fill()
        t.forward(stripe)
        stripe = 14.3
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(stripe)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.end_fill()
        stripe = stripe * 3

    for x in range(1, 4):
        t.begin_fill()
        t.forward(stripe)
        stripe = 14.3
        t.right(90)
        t.forward(350)
        t.right(90)
        t.forward(stripe)
        t.right(90)
        t.forward(350)
        t.right(90)
        t.end_fill()
        stripe = stripe * 3

    # Getting rid of extra stripe (white one at bottom)
    t.forward(14.3)# don't combine this with the other 14.3 one.
    t.color('white')
    t.forward(14.3)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(14.3)
    t.up()
    tk.deiconify()    

def hs():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.back(175)
    t.right(90)
    t.back(120)

    # Hammer and Sickle + star
    t.color('yellow')
    t.left(90)
    t.up()
    t.forward(20)
    t.write("☭", font=("Arial", 45, "normal"))
    t.back(10)
    t.left(90)
    t.forward(57)
    t.right(90)
    t.forward(30)
    t.write("⭐", font=("Arial", 7, "normal"))
    t.up()
    tk.deiconify()

def sun():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.left(90)
    t.up()
    t.forward(45)
    t.right(90)
    

    t.down()
    t.color('red')
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.up()
    tk.deiconify()
    t.up()
    tk.deiconify()


def stars():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.back(175)
    t.left(90)
    t.up()
    t.forward(185)
    t.right(90)
    t.color('white')

    star = 10

    for x in range(1, 5):
        for x in range(1, 7):
            t.forward(star)
            star = 15
            t.write("★", font=("Arial", 7, "normal"))
            star = star + 10

        t.back(135)
        t.right(90)
        t.forward(10)
        t.left(90)
        star = 20

        for x in range(1, 6):
            t.forward(star)
            star = 15
            t.write("★", font=("Arial", 7, "normal"))
            star = star + 10

        t.back(135)
        t.right(90)
        t.forward(10)
        t.left(90)

    for x in range(1, 7):
        t.forward(star)
        star = 15
        t.write("★", font=("Arial", 7, "normal"))
        star = star + 10

    t.up()
    tk.deiconify()

def box():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.back(175)
    t.left(90)
    t.forward(200)
    t.back(100)
    t.color('#3C3B6E')
    t.right(90)
    t.forward(150)
    t.begin_fill()
    for x in range(1, 3):
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(150)

    t.end_fill()

    t.up()
    tk.deiconify()


def sundial():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.up()
    t.left(90)
    t.forward(100)
    t.left(90)
    t.back(25)
    t.right(90)
    # Blue circle
    t.color('blue')
    t.down()
    t.circle(25)

    t.up()
    t.left(90)
    t.forward(25)
        
    # 24 hour dial
    for x in range(1, 25):
        t.down()
        t.forward(25)
        t.back(25)
        t.left(15)
        t.forward(25)
        t.back(25)

    t.up()
    tk.deiconify()

def dprkstar():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.up()
    t.left(90)
    t.forward(135)
    t.left(90)
    t.forward(25)
    t.color('white')
    # white circle
    t.forward(50)
    t.down()
    t.begin_fill()
    t.circle(35)
    t.end_fill()
   

    #star
    t.up()
    t.color('red')
    t.left(90)
    t.forward(75)
    t.right(90)
    t.forward(35)
    t.write("★", font=("Arial", 55, "normal"))
    t.up()
    tk.deiconify()

def chinaStars():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.back(175)
    t.right(90)
    t.back(130)

    t.color('yellow')
    t.left(90)
    t.up()
    t.forward(10)
    t.write("★", font=("Arial", 40, "normal"))
    t.back(10)
    t.left(90)
    t.forward(45)
    t.right(90)
    t.forward(65)
    t.write("★", font=("Arial", 13, "normal"))
    t.back(55)
    t.left(90)
    t.back(20)
    t.right(90)
    t.forward(70)
    t.write("★", font=("Arial", 13, "normal"))
    t.back(70)
    t.left(90)
    t.back(25)
    t.right(90)
    t.forward(70)
    t.write("★", font=("Arial", 13, "normal"))
    t.back(70)
    t.left(90)
    t.back(25)
    t.right(90)
    t.forward(55)
    t.write("★", font=("Arial", 13, "normal"))

    tk.deiconify()

def germanColours():
    tk.withdraw()
    t.hideturtle()
    t.home()
    t.back(175)
    t.down()
    # getting ready for black stripe
    t.left(90)
    t.forward(132)
    t.right(90)
    t.begin_fill()

    # Black stripe
    t.color('black')
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(66)
      t.left(90)
    t.end_fill()

    # getting ready for red stripe
    t.color('red')
    t.begin_fill()

    # red stripe
    for x in range(1, 3):
      t.forward(350)
      t.right(90)
      t.forward(66)
      t.right(90)
    t.end_fill()

    # getting ready for yellow stripe
    t.right(90)
    t.forward(66)
    t.color('#FFCE00')
    t.left(90)

    # yellow stripe
    t.begin_fill()
    for x in range(1, 3):
      t.forward(350)
      t.right(90)
      t.forward(66)
      t.right(90)
    t.end_fill()

    t.up()
    tk.deiconify()

def russiaColours():
    tk.withdraw()
    t.home()
    t.back(175)
    t.right(90)
    t.back(133)
    
    # blue stripe
    t.down()
    t.begin_fill()
    t.left(90)
    t.color('#0033A0')
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.end_fill()

    # Getting ready for red stripe
    t.left(180)
    t.forward(66)

    # red stripe
    t.begin_fill()
    t.left(90)
    t.color('red')
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.end_fill()
    t.up()
    tk.deiconify()

def indianColours():
    tk.withdraw()
    t.home()
    t.back(175)
    t.right(90)
    t.back(133)
    t.down()
    
    # Orange stripe
    t.left(90)
    t.color('orange')
    t.begin_fill()
    t.forward(350)
    t.left(90)
    t.forward(66)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(66)
    t.end_fill()

    # Getting ready for green stripe
    t.color('black')
    t.forward(66)

    # Green stripe
    t.begin_fill()
    t.left(90)
    t.color('green')
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.end_fill()
    t.up()
    tk.deiconify()

def qatarMaroon():
    tk.withdraw()
    t.home()
    t.back(175)
    # making design
    t.down()
    t.forward(116)
    t.left(45)
    t.color('#8D1B3D')
    t.begin_fill()
    for x in range(1, 10):
      t.forward(15)
      t.left(90)
      t.forward(15)
      t.right(90)

    t.forward(13)
    t.right(45)
    t.forward(225)

    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(233)
    t.end_fill()
    t.up()
    tk.deiconify()

def vietStar():
    tk.withdraw()
    t.home()
    t.back(175)
    # star
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(110)
    t.color('yellow')
    t.write("★", font=("Arial", 100, "normal"))
    t.up()
    tk.deiconify()

def about():
    messagebox.showinfo("About", "Customise and make your own flags! \n\
You can screen cap to save image. \n\
\n\
For your own safety, you may NOT use this software in the People's Republic \
of China excluding the \n\
Hong Kong Special Administrative Region of the People's Republic of China. \
This means every place controlled by the People's Republic of China excluding \
the Hong Kong Special Administrative Region of the People's Republic of China. \n\
\n\
For your own safety, you may NOT use this software in the \
Democratic People's Republic of Korea. This means every place controlled by \
the Democratic People's Republic of Korea. \n\
\n\
I, the creator of this program, am not liable for anything that happens to \
you for using this program. You have been warned. \n\
\n\
Software made by [Name not given] \n\
Software Language: English ")

def Exit():
    exit()

# visual items such as buttons and labels
btn = Button(tk, text="Make canvas", command=canvas)
btn.pack()

directions = Label(tk, text="Things you can add to your flag:")
directions.pack()

btn = Button(tk, text="Hammer and Sickle", command=hs)
btn.pack()

btn = Button(tk, text="Sun", command=sun)
btn.pack()

btn = Button(tk, text="Stripes", command=stripes)
btn.pack()

btn = Button(tk, text="50 stars", command=stars)
btn.pack()

btn = Button(tk, text="Box in corner", command=box)
btn.pack()

btn = Button(tk, text="24 hour dial", command=sundial)
btn.pack()

btn = Button(tk, text="Communist Star", command=dprkstar)
btn.pack()

btn = Button(tk, text="Chinese Flag 5 stars", command=chinaStars)
btn.pack()

btn = Button(tk, text="German Stripes", command=germanColours)
btn.pack()

btn = Button(tk, text="Russian Stripes", command=russiaColours)
btn.pack()

btn = Button(tk, text="Indian Stripes", command=indianColours)
btn.pack()

btn = Button(tk, text="Qatari Al-Adaam Maroon Area", command=qatarMaroon)
btn.pack()

btn = Button(tk, text="Vietnamese Star", command=vietStar)
btn.pack()

w = Label(tk, text="---------------------------------------")
w.pack()

btn = Button(tk, text="About/Other Information", command=about)
btn.pack()

btn = Button(tk, text="Exit", command=Exit)
btn.pack()


# Warning 
messagebox.showinfo("Warning, Warnung, 경고, 警告, Предупреждение, 警告, تحذير, \
चेतावनी", "Diese Software wurde NICHT entwickelt, um die deutsche Flagge zu \
diffamieren. \n\
Это программное обеспечение не было сделано, чтобы опорочить российский флаг. \n\
यह सॉफ्टवेयर भारतीय गणराज्य झंडा को बदनाम करने के लिए नहीं बनाया गया था। \n\
该软件并非用来诽谤中华人民共和国的国旗。\n\
このソフトウェアは、日本の国旗を中傷するものではありません。\n\
لم يتم صنع هذا البرنامج لتشويه علم دولة قطر. \n\
This software was NOT made to defame the Flag of the Republic of India. \n\
Phần mềm này KHÔNG được tạo ra để phỉ báng cờ của nước Cộng hòa xã hội chủ \
nghĩa Việt Nam \n\
이 소프트웨어는 조선민주주의인민공화국의 국기를 비방하기 위해 만들어진 것이 아닙니다.")
