import time
phonebook = dict()

print("Whatever does not work please email it at tusharpassi2005@gmail.com")
print("You cannot view phonebook if you are trying to add or delete a \
contact.")
print("")
first_question = input("To view Phonebook, type print(phonebook).\n\
To Save a contact, type 'Save'. To Delete a contact, type 'Delete'. \n\
To Exit the program, type 'Exit': ")

# If person give invalid response to the "first question"
while first_question != "print(phonebook)" and first_question != "Save" \
and first_question !=  "Delete" and first_question != "Exit":  
    print("Invalid Response. Try again.")
    first_question = input("To view Phonebook, type print(phonebook).\n\
To Save a contact, type 'Save'. To Delete a contact, type 'Delete'. \n\
To Exit the program, type 'Exit': ")

# if the person wanna save a contact
while first_question == "Save":
    contact = input("Enter a contact you'd like to save: ")
    phonenumber = input("Enter the phonenumber to contact: ")
    phonebook[contact] = phonenumber
    second_question = input("Would you like to add another contact?: (y/n): ")
    # If person give invalid response
    while second_question != "y" and second_question != "n":
        print("Invalid response. Try again.")
        second_question = input("Would you like to add another contact? (y/n): ")
    # if person wanna add 2nd contact
    if second_question == "y":
        contact1 = input("Enter a contact you'd like to save: ")
        phonenumber1 = input("Enter the phonenumber to contact: ")
        phonebook[contact1] = phonenumber1
        second_question = input("Would you like to add another contact? (y/n): ")
    # If person give invalid response
    while second_question != "y" and second_question != "n":
        print("Invalid response. Try again.")
        second_question = input("Would you like to add another contact? (y/n): ")
    # if person wanna add 3rd contact
    if second_question == "y":
        contact2 = input("Enter a contact you'd like to save: ")
        phonenumber2 = input("Enter the phonenumber to contact: ")
        phonebook[contact2] = phonenumber2
        second_question = input("Would you like to add another contact? (y/n): ")
    # If person give invalid response
    while second_question != "y" and second_question != "n":
        print("Invalid response. Try again.")
        second_question = input("Would you like to add another contact? (y/n): ")
    # if person wanna add 4th contact
    if second_question == "y":
        contact3 = input("Enter a contact you'd like to save: ")
        phonenumber3 = input("Enter the phonenumber to contact: ")
        phonebook[contact3] = phonenumber3
        second_question = input("Would you like to add another contact? (y/n): ")
    # If person give invalid response
    while second_question != "y" and second_question != "n":
        print("Invalid response. Try again.")
        second_question = input("Would you like to add another contact? (y/n): ")
    # if person wanna add 5th contact
    if second_question == "y":
        contact4 = input("Enter a contact you'd like to save: ")
        phonenumber4 = input("Enter the phonenumber to contact: ")
        phonebook[contact4] = phonenumber4
        input("Maximum of 5 contacts allowed.")
    # if person don't wanna add another contact
    if second_question == "n":
        print("")
        input("Your contacts are saved in a file called 'phonebook.txt'.")
        print("")
        first_question = input("To view Phonebook, type print(phonebook).\n\
To Save a contact, type 'Save'. To Delete a contact, type 'Delete'. \n\
To Exit the program, type 'Exit': ")

# if person wants to delete a contact
while first_question == "Delete":
    del_q = input("Which contact do you want to delete? (1, 2, 3, 4, 5, all): ")
    if del_q == "1":
        try:
            contact
        except NameError:
            print("Contact cannot be deleted. Reason: It doesn't exist")
        else:
            print("Deleting contact..")
            time.sleep(1)
            del phonebook[contact]
            print("Contact deleted.")
            print(phonebook)
    if del_q == "2":
       try:
            contact1
       except NameError:
            print("Contact cannot be deleted. Reason: It doesn't exist")
       else:
            print("Deleting contact..")
            time.sleep(1)
            del phonebook[contact1]
            print("Contact deleted.")
            print(phonebook)
    if del_q == "3":
        try:
            contact2
        except NameError:
            print("Contact cannot be deleted. Reason: It doesn't exist")
        else:
            print("Deleting contact..")
            time.sleep(1)
            del phonebook[contact2]
            print("Contact deleted.")
            print(phonebook)
    if del_q == "4":
        try:
            contact3
        except NameError:
            print("Contact cannot be deleted. Reason: It doesn't exist")
        else:
            print("Deleting contact..")
            time.sleep(1)
            del phonebook[contact3]
            print("Contact deleted.")
            print(phonebook)
    if del_q == "5":
        try:
            contact4
        except NameError:
            print("Contact cannot be deleted. Reason: It doesn't exist")
        else:
            print("Deleting contact..")
            time.sleep(0.01)
            del phonebook[contact4]
            print("Contact deleted.")
            print(phonebook)
    if del_q == "all":
        try:
            contact
        except NameError:
            pass
        else:
            print("Deleting contact..")
            time.sleep(1)
            del phonebook[contact]
            print("Contact deleted.")
        try:
            contact1
        except NameError:
            pass
        else:
            print("Deleting contact..")
            time.sleep(1)
            del phonebook[contact1]
            print("Contact deleted.")
        try:
            contact2
        except NameError:
            pass
        else:
            print("Deleting contact..")
            time.sleep(0.01)
            del phonebook[contact2]
            print("Contact deleted.")
        try:
            contact3
        except NameError:
            pass
        else:
            print("Deleting contact..")
            time.sleep(1)
            del phonebook[contact3]
            print("Contact deleted.")
        try:
            contact4
        except NameError:
            pass
        else:
            print("Deleting contact..")
            time.sleep(1)
            del phonebook[contact4]
            print("All contacts deleted.")
        print(phonebook)
    contact_question = input("Do you want to delete another contact? \
(y, n): ")
    if contact_question == "n":
        first_question = input("To view Phonebook, type print(phonebook).\n\
To Save a contact, type 'Save'. To Delete a contact, type 'Delete' \
To Exit the program, type 'Exit': ")
        
# If person wanna exit program
if first_question == "Exit":
        print("Exiting program...")
        time.sleep(1)
        print("Exited program.")

# if u wanna view phonebook
if first_question == "print(phonebook)":
    print(phonebook)
    first_question = input("To view Phonebook, type print(phonebook).\n\
To Save a contact, type 'Save'. To Delete a contact, type 'Delete' \
To Exit the program, type 'Exit': ")

f = open('c:\\Users\\User\\Desktop\\phonebook.txt', 'a')
f.write(str(phonebook))
f.close()
