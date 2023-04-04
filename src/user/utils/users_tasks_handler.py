from colorama import Back, Style


def remove_from_cart(user):
    if (len(user.foodlist) == 0):
        print(Back.YELLOW + "\nNothing to Remove Your Cart is Empty" + Style.RESET_ALL)

    else:
        index = 0
        while (index == 0):
            index = int(input(
                "\n\nEnter the valid of the item you want to remove "))

        user.remove_fromcart(index)
        user.check_cart()


def update_cart(user, rest):
    if (user.curr_rest != rest):
        user.curr_rest = rest
        user.foodlist = []

    menuitem = 0
    while (menuitem == 0):
        index = int(input(
            "\nEnter the valid index of the item you want to Add "))
        menuitem = rest.find_item(index)

        if (menuitem):
            user.update_cart(menuitem)
            user.check_cart()


def place_order(user, z, rest):
    if (len(user.foodlist) == 0):
        print(Back.YELLOW +
              "YOUR CART IS EMPTY PLEASE ADD SOMETHING TO CONTINUE"+Style.RESET_ALL)

    else:
        agent = z.assign_delivery()
        agent.update_status()

        z.place_order(user, rest, agent)

        print("\n WANT TO RATE THE CURRENT RESTAURANT ?")
        print("ENTER Y/y TO CONTINUE OR N/n TO RETURN TO HOMEPAGE")
        mych = input("ENTER CHOICE")

        if (mych == 'Y' or mych == 'y'):

            rate = int(input("ENTER THE RATING BETWEEN 0-5 "))
            while (rate < 0 or rate > 5):
                rate = int(input("ENTER A VALID RATING BETWEEN 0-5 "))

            rest = user.curr_rest
            z.rate_current_rest(rest, rate)
