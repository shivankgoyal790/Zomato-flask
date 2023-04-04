def phonechecker():
    phone = input("Enter YOUR PHONE NUMBER ")
    while (len(phone) < 10):
        print("MOBILE NUMBER SHOULD BE 10 DIGITS ENTER AGAIN ")
        phone = input("ENTER YOUR PHONE NUMBER ")
    return phone
