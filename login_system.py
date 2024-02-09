import re

f = open('c:\\Users\\User\\Desktop\\login_system.txt', 'a')

# Credits
print("Login System made by Tushar Passi. ਤੁਸ਼ਾਰ ਪਾਸੀ ਨੇ ਲਾਗਿਨ ਸਿਸਟਮ ਬਣਾਇਆ")
print("Help with Stack Overflow. Stack Overflow ਨਾਲ ਮਦਤ ਕੀਤਾ")
print("Whatever does not work, email it at tusharpassi2005@gmail.com")
print("Language: English ਭਾਸ਼ਾ: ਅੰਗ੍ਰੇਜ਼ੀ")
print("")

# The first question
loginsystem = input("Welcome to this login system. Would you like to create \
an account or login? (create/login): ")
    
# registration information / saving it to the file
def registration():
    print("")
    global username

    # Username to get for user
    username = input("Enter a username that you want. \n\
Type 'forbidden usernames' to see usernames that are not allowed: ")

    while len(username) > 15: # If username is greater than 15 characters
        print("")
        print("Your username is too long. 15 characters is the max.")
        print("")
        username = input("Enter a username that you want. \n\
Type 'forbidden usernames' to see usernames that are not allowed: ")

    while username == "": # if no username is typed
        print("Please enter an username.")
        username = input("Enter a username that you want. \n\
Type 'forbidden usernames' to see usernames that are not allowed: ")
        
    if username == "forbidden usernames": # To view forbidden names.
        print("Usernames NOT allowed (seperated by commas): create, ,")
        username = input("Enter a username that you want: ")
        
    while username == "create": # If player tries to pick 'create' as name
        print("This username is forbidden.")
        username = input("Enter a username that you want: ")
        
    email = input("Enter your email: ") # To get user email 
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', \
                     email)  # To check if user typed an email

    while match == None: # if email typed is not an email
        print("The email you've typed is not an email.")
        email = input("Enter your email: ")
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', \
                     email)
        
    # To get password 
    global password
    password = input("Enter a password: ")
    confirm_password = input("Type your password again: ")
    
    while confirm_password != password: #if password != confirmation of password
        print("The passwords do not match.")
        password = input("Enter a password: ")
        confirm_password = input("Type your password again: ")
        
    if confirm_password == password: # if password == confirmation of password
        print("Your account has now been registered")
                    
    user = [username, password, email, "\n"] # To write information to txt file
    for line in user:
        f.write(line)
        f.write(" ")

# Login system defined in a object
def login():
    print("")
    try:
        username = input("What is your username?: ")
        password = input("What is the password?: ")
        for line in open("c:\\Users\\User\\Desktop\\login_system.txt", "r").readlines():
            login_info = line.split()
            if username == login_info[0] and password == login_info[1]:
                print("")
                print("You have logged in successfully!")
                return True
    except IndexError:
        print("")
        print("Invalid credentials. Try again")
        login()
    else:
        pass
    
    
# If the response to the first question was not valid
while loginsystem != "create" and loginsystem != "login":
    print("")
    print("Invalid response. Try again.")
    print("Make sure you've spelled the word correctly. Capitalisation matters.")
    print("")
    loginsystem = input("Welcome to this login system. Would you like to create \
an account or login? (create/login): ")
    
    
#if the first question's response was "create"
while loginsystem == "create":
    registration()
    print("")
    loginsystem = input("Welcome to this login system. Would you like to create \
an account or login? (create/login): ")

# To close file after accounts have been created               
f.close()

#If the first question's response was "login"
if loginsystem == "login":
    login()
    
