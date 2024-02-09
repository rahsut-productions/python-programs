import time
phonebook = dict()

print("ਜੋ ਵੀ ਕੰਮ ਨਹੀਂ ਕਰਦਾ, tusharpassi2005@gmail.com 'ਤੇ ਈਮੇਲ ਕਰੋ")
print("ਤੁਸੀਂ ਫੋਨਬੁੱਕ ਵੇਖ ਨਹੀਂ ਕਰ ਸਕਦੇ ਜੇ ਤੁਸੀਂ ਇਕ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਦੇਪੇ ਫੋਨੇਬੂਕ ਵਿਚ")
print("")
first_question = input("ਫੋਨੇਬੂਕ ਵੇਖਾਨੂੰ,ਟਾਈਪ ਕਰੋ print(phonebook).\n\
ਇਕ ਸੰਪਰਕ ਨੂੰ ਫੋਨੇਬੂਕ ਸਵੈ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Save'. ਇਕ ਸੰਪਰਕ ਮਿਟਾਨਾਨੂੰ, ਟਾਈਪ ਕਰੋ 'Delete'. \n\
ਪ੍ਰੋਗ੍ਰਾਮ ਵਿਚ ਨਿਕਾਸ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Exit': ")

# If person give invalid response to the "first question"
while first_question != "print(phonebook)" and first_question != "Save" \
and first_question !=  "Delete" and first_question != "Exit":  
    print("ਗਲਤ ਲਿਖਇਆ. ਇਕ ਹੋਰ ਵਰੀ ਲਿਖੋ")
    first_question = input("ਫੋਨੇਬੂਕ ਵੇਖਾਨੂੰ,ਟਾਈਪ ਕਰੋ print(phonebook).\n\
ਇਕ ਸੰਪਰਕ ਨੂੰ ਫੋਨੇਬੂਕ ਸਵੈ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Save'. ਇਕ ਸੰਪਰਕ ਮਿਟਾਨਾਨੂੰ, ਟਾਈਪ ਕਰੋ 'Delete'. \n\
ਪ੍ਰੋਗ੍ਰਾਮ ਵਿਚ ਨਿਕਾਸ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Exit': ")

# if the person wanna save a contact
while first_question == "Save":
    contact = input("ਸੰਪਰਕ ਦਾ ਨਾਮ ਟਾਈਪ ਕਰੋ: ")
    phonenumber = input("ਸੰਪਰਕ ਦਾ ਨੰਬਰ ਟਾਈਪ ਕਰੋ: ")
    phonebook[contact] = phonenumber
    second_question = input("ਇਕ ਹੋਰ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਨਾ?: (Yes/No): ")
    # If person give invalid response
    while second_question != "Yes" and second_question != "No":
        print("ਗਲਤ ਲਿਖਇਆ. ਇਕ ਹੋਰ ਵਰੀ ਲਿਖੋ")
        second_question = input("ਇਕ ਹੋਰ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਨਾ?: (Yes/No): ")
    # if person wanna add 2nd contact
    if second_question == "Yes":
        contact1 = input("ਸੰਪਰਕ ਦਾ ਨਾਮ ਟਾਈਪ ਕਰੋ: ")
        phonenumber1 = input("ਸੰਪਰਕ ਦਾ ਨੰਬਰ ਟਾਈਪ ਕਰੋ: ")
        phonebook[contact1] = phonenumber1
        second_question = input("ਇਕ ਹੋਰ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਨਾ?: (Yes/No): ")
   # If person give invalid response
    while second_question != "Yes" and second_question != "No":
        print("ਗਲਤ ਲਿਖਇਆ. ਇਕ ਹੋਰ ਵਰੀ ਲਿਖੋ")
        second_question = input("ਇਕ ਹੋਰ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਨਾ?: (Yes/No): ")
    # if person wanna add 3rd contact
    if second_question == "Yes":
        contact2 = input("ਸੰਪਰਕ ਦਾ ਨਾਮ ਟਾਈਪ ਕਰੋ: ")
        phonenumber2 = input("ਸੰਪਰਕ ਦਾ ਨੰਬਰ ਟਾਈਪ ਕਰੋ: ")
        phonebook[contact2] = phonenumber2
        second_question = input("ਇਕ ਹੋਰ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਨਾ?: (Yes/No): ")
     # If person give invalid response
    while second_question != "Yes" and second_question != "No":
        print("ਗਲਤ ਲਿਖਇਆ. ਇਕ ਹੋਰ ਵਰੀ ਲਿਖੋ")
        second_question = input("ਇਕ ਹੋਰ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਨਾ?: (Yes/No): ")
    # if person wanna add 4th contact
    if second_question == "Yes":
        contact3 = input("ਸੰਪਰਕ ਦਾ ਨਾਮ ਟਾਈਪ ਕਰੋ: ")
        phonenumber3 = input("ਸੰਪਰਕ ਦਾ ਨੰਬਰ ਟਾਈਪ ਕਰੋ: ")
        phonebook[contact3] = phonenumber3
        second_question = input("ਇਕ ਹੋਰ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਨਾ?: (Yes/No): ")
     # If person give invalid response
    while second_question != "Yes" and second_question != "No":
        print("ਗਲਤ ਲਿਖਇਆ. ਇਕ ਹੋਰ ਵਰੀ ਲਿਖੋ")
        second_question = input("ਇਕ ਹੋਰ ਸੰਪਰਕ ਨੂੰ ਜੋੜ ਨਾ?: (Yes/No): ")
    # if person wanna add 5th contact
    if second_question == "Yes":
        contact4 = input("ਸੰਪਰਕ ਦਾ ਨਾਮ ਟਾਈਪ ਕਰੋ: ")
        phonenumber4 = input("ਸੰਪਰਕ ਦਾ ਨੰਬਰ ਟਾਈਪ ਕਰੋ: ")
        phonebook[contact4] = phonenumber4
        input("5 ਸੰਪਰਕ ਤੇ ਹੋਰ ਨਹੀਂ ਪਾਨ ਸਕਦੇ")
    # if person don't wanna add another contact
    if second_question == "No":
        first_question = input("ਫੋਨੇਬੂਕ ਵੇਖਾਨੂੰ,ਟਾਈਪ ਕਰੋ print(phonebook).\n\
ਇਕ ਸੰਪਰਕ ਨੂੰ ਫੋਨੇਬੂਕ ਸਵੈ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Save'. ਇਕ ਸੰਪਰਕ ਮਿਟਾਨਾਨੂੰ, ਟਾਈਪ ਕਰੋ 'Delete'. \n\
ਪ੍ਰੋਗ੍ਰਾਮ ਵਿਚ ਨਿਕਾਸ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Exit': ")

# if person wants to delete a contact
while first_question == "Delete":
    del_q = input("ਕਿਹੜੇ ਵਾਲਾ ਨੂੰ ਮਿਟਾਨਾ? (1, 2, 3, 4, 5, all): ")
    if del_q == "1":
        try:
            contact
        except NameError:
            print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact]
            print("ਸੰਪਰਕ ਮਿਟਾਲਿਆ")
            print(phonebook)
    if del_q == "2":
       try:
            contact1
       except NameError:
            print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
       else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact1]
            print("ਸੰਪਰਕ ਮਿਟਾਲਿਆ")
            print(phonebook)
    if del_q == "3":
        try:
            contact2
        except NameError:
            print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact2]
            print("ਸੰਪਰਕ ਮਿਟਾਲਿਆ")
            print(phonebook)
    if del_q == "4":
        try:
            contact3
        except NameError:
            print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact3]
            print("ਸੰਪਰਕ ਮਿਟਾਲਿਆ")
            print(phonebook)
    if del_q == "5":
        try:
            contact4
        except NameError:
           print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact4]
            print("ਸੰਪਰਕ ਮਿਟਾਲਿਆ")
    # if person wanna delete all contacts
    if del_q == "all":
        try:
            contact
        except NameError:
           print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact]
            print("ਸੰਪਰਕ 1 ਮਿਟਾਲਿਆ")
        try:
            contact1
        except NameError:
           print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact1]
            print("ਸੰਪਰਕ 2 ਮਿਟਾਲਿਆ")
        try:
            contact2
        except NameError:
           print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact2]
            print("ਸੰਪਰਕ 3 ਮਿਟਾਲਿਆ")
        try:
            contact3
        except NameError:
           print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact3]
            print("ਸੰਪਰਕ 4 ਮਿਟਾਲਿਆ")
        try:
            contact4
        except NameError:
           print("ਸੰਪਰਕ ਨਹੀਂ ਮਿਟਾਨ ਸਕਦੇ. ਕ੍ਯੂਂ?: ਸੰਪਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ")
        else:
            print("ਸੰਪਰਕ ਮਿਟਾਨੇ ਪੇ.. ")
            time.sleep(1)
            del phonebook[contact4]
            print("ਸਾਰੇ ਸੰਪਰਕ ਮਿਟਾਲਿਆ")
        print(phonebook)
    contact_question = input("Do you want to delete another contact? \
(y, n): ")
    if contact_question == "No":
        first_question = input("ਫੋਨੇਬੂਕ ਵੇਖਾਨੂੰ,ਟਾਈਪ ਕਰੋ print(phonebook).\n\
ਇਕ ਸੰਪਰਕ ਨੂੰ ਫੋਨੇਬੂਕ ਸਵੈ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Save'. ਇਕ ਸੰਪਰਕ ਮਿਟਾਨਾਨੂੰ, ਟਾਈਪ ਕਰੋ 'Delete'. \n\
ਪ੍ਰੋਗ੍ਰਾਮ ਵਿਚ ਨਿਕਾਸ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Exit': ")     

# If person wanna exit program
if first_question == "Exit":
        print("ਪ੍ਰੋਗ੍ਰਾਮ ਨੂੰ ਬਾਦ ਕਰਲਿਆ")

# if u wanna view phonebook
if first_question == "print(phonebook)":
    print(phonebook)
    first_question = input("ਫੋਨੇਬੂਕ ਵੇਖਾਨੂੰ,ਟਾਈਪ ਕਰੋ print(phonebook).\n\
ਇਕ ਸੰਪਰਕ ਨੂੰ ਫੋਨੇਬੂਕ ਸਵੈ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Save'. ਇਕ ਸੰਪਰਕ ਮਿਟਾਨਾਨੂੰ, ਟਾਈਪ ਕਰੋ 'Delete'. \n\
ਪ੍ਰੋਗ੍ਰਾਮ ਵਿਚ ਨਿਕਾਸ ਕਰਨੂੰ, ਟਾਈਪ ਕਰੋ 'Exit': ")


f = open('c:\\Users\\User\\Desktop\\phonebook.txt', 'a')
f.write(str(phonebook))
f.close()
