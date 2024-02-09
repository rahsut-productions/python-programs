from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
# The main window
tk = Tk(className = "ਟੈਕਸਟ ਐਡੀਟਰ Text Editor ")
texteditor = scrolledtext.ScrolledText(tk, width=100, height=45)


# Functions
def new():
    # If there is content?
    if len(texteditor.get("1.0", END+"-1c")) > 0:
        if messagebox.askyesno("Save?", "Would you like to save?"):
            Save()

    
def Open():
    file = filedialog.askopenfile(parent=tk, title="Select a text file you'd like to open. ਇਕ .txt ਫਾਇਲ ਨੂੰ ਕੋਲਲੋ", filetypes=(("Text File", "*.txt"), ("All files", "*.*")))

    if file != None:
        texteditor.delete(0.0, END)
        text = file.read()
        texteditor.insert("1.0", text)
        file.close()

def Exit():
    tk.destroy()
    

def Save():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt", title="Save as.. ਫ਼ਾਇਲ ਨੂੰ ਇਸ ਤਰਾਂ ਨੂੰ ਸੇਵ ਕਰੋ..", filetypes=(("HTML file", "*.html"), ("Text file", "*.txt"), ("All files", "*.*")))

    if file != None:
        # slices off hte last character from get, as an extra return/enter is added
        text = texteditor.get("1.0", END+'-1c')
        file.write(text)
        file.close()

def credit():
    messagebox.showinfo("Credits", "Original Code by Djogo the Coder \n\
Translated by Tushar Passi \n\
Modified by Tushar Passi")
    messagebox.showinfo("ਕ੍ਰੈਡਿਟਸ", "ਅਸਲੀ ਕੋਡ: Djogo the Coder \n\
ਅਨੁਵਾਦ: ਤੁਸ਼ਾਰ ਪਾਸੀ \n\
ਕੋਡ ਦਾ ਸੋਧ: ਤੁਸ਼ਾਰ ਪਾਸੀ")

def about():
    messagebox.showinfo("About", "An altrenative to Notepad made entirely in Python. \n\
\n\
Program Language: English and Punjabi")
    messagebox.showinfo("ਟੈਕਸਟ ਐਡੀਟਰ ਬਾਰੇ", "ਇਕ Notepad ਬਦਲ Python ਵਿੱਚ| \n\
\n\
ਪ੍ਰੋਗ੍ਰਾਮ ਦਾ ਭਾਸ਼ਾ: ਅੰਗ੍ਰੇਜ਼ੀ ਅਤੇ ਪੰਜਾਬੀ")

def find():
    findtext = simpledialog.askstring("Find.. ਕੀ ਲਬਾਂ..", "Enter Text ਟੇਕਸ ਲਿਖੋ")
    textdata = texteditor.get('1.0', END)

    print("If there is an AttributeError, ignore it. Python is complaining because you clicked cancel.")
    occurances = textdata.upper().count(findtext.upper())    
    if textdata.upper().count(findtext.upper()) > 0:
        messagebox.showinfo("Results", findtext + " has " + str(occurances) + " occurance(s).")
        messagebox.showinfo("ਨਤੀਜੇ", findtext + " " + str(occurances) + " ਵਰੀ ਲਬਿਆ")
    else:
        messagebox.showinfo("Results", "No results found.")
        messagebox.showinfo("ਨਤੀਜੇ", "ਕੋਈ ਨਤੀਜੇ ਨਹੀਂ ਲਬੇ")
    
           
# Menu
menu = Menu(tk)
tk.config(menu=menu)
fileoption = Menu(menu) 

#File menu
menu.add_cascade(label="File  ਫ਼ਾਇਲ", menu=fileoption)
fileoption.add_command(label="New ਨਵਾਂ", command=new)
fileoption.add_command(label="Open ਖੋਲ੍ਹੋ", command=Open)
fileoption.add_command(label="Save ਸੇਵ", command=Save)
fileoption.add_command(label="Find ਲਬੋ", command=find)
fileoption.add_separator() # Separates the options from exit
fileoption.add_command(label="Exit ਨਿਕਾਸ", command=Exit)

helpoption = Menu(menu)
menu.add_cascade(label="About ਟੈਕਸਟ ਐਡੀਟਰ ਬਾਰੇ", command=about)
menu.add_cascade(label="Credits ਕ੍ਰੈਡਿਟਸ", command=credit)

texteditor.pack()

#mainloop
tk.mainloop()
