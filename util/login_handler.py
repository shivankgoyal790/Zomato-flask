from src import validemailcheck
from src import password_checker
from src import Restaurant
from src import User
from src import Deliveryboy
from src import delivery_interactive
from colorama import Back, Style, Fore


def loginhandler(z):

    email = validemailcheck()
    password = password_checker()

    ch = "1"
    while (ch != "2"):
        entity = z.authenticate(email, password)

        ch = "2"
        if (isinstance(entity, Restaurant)):
            entity.handle_restaurant_interaction(z)

        elif (isinstance(entity, User)):
            entity.handle_user_interaction(z)

        elif (isinstance(entity, Deliveryboy)):
            delivery_interactive(entity, z)

        else:
            print(Back.YELLOW+Fore.BLACK +
                  "\nINVALID LOGIN CREDENTIALS\n" + Style.RESET_ALL)
            break
