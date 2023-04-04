import maskpass


def password_checker():
    password = maskpass.askpass(mask="*")
    while (len(password) < 8):
        print("PASSWORD SHOULD BE MINIMUM 8 CHARACTERS ENTER AGAIN ")
        password = maskpass.askpass(mask="*")
    return password
