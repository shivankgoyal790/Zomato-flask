from src.zomato import Zomato
from src.restaurant.restaurant import Restaurant
from src.delivery_boy import Deliveryboy
import random
from colorama import Back, Style
from util.login_handler import loginhandler
from util.singup_handler import signup_handler

print(Style.RESET_ALL)
z = Zomato()


def cached_details():

    newrest = Restaurant("201", "Mc Donalds", "sector 142",
                         "mcd@gmail.com", "12345678")
    newrest.create_menu()
    menuitem1 = newrest.create_new_menuitem()
    menuitem2 = newrest.create_new_menuitem()
    z.list_of_items.append(menuitem1)
    z.list_of_items.append(menuitem2)

    z.list_of_enities.append(newrest)

    deliveragent1 = Deliveryboy(random.randint(
        5000, 6000), "sam", "9897653285", "sam@gmail.com", "12345678")
    deliveragent2 = Deliveryboy(random.randint(
        5000, 6000), "rakesh", "9897653285", "rakesh@gmail.com", "12345678")

    z.list_of_enities.append(deliveragent1)
    z.list_of_enities.append(deliveragent2)


cached_details()


def main():

    ch = '0'

    while (ch != '9'):

        print("\n\n\nWELCOME TO ZOMATO")
        z.display_restaurants()

        print(Back.RED + "\nENTER 1 TO LOGIN")
        print("ENTER 2 TO SIGN UP")
        choice = input("ENTER CHOICE " + Style.RESET_ALL)

        if (choice == '1'):
            loginhandler(z)

        else:
            signup_handler(z)


main()
