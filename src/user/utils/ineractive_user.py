from colorama import Back, Style
from src.user.utils.userchoice_interaction import user_choice_interaction
from src.user.utils.users_tasks_handler import remove_from_cart, place_order
from src.user.utils.choice_handler import handle_choice_1, handle_choice_6, handle_choice_7


def user_interactive_display(user, z):

    ch = '0'
    while (ch != "8"):
        print("\nHELLO!! HERE IS THE LIST OF RESTRAUNTS CURRENTLY ACCEPTING ORDERS")
        z.display_restaurants()

        user_choice_interaction()
        ch = int(input("ENTER CHOICE "))

        handle_choice = {
            1: lambda: handle_choice_1(),
            2: lambda: user.check_cart(),
            3: lambda: remove_from_cart(user),
            4: lambda: place_order(user, z, user.curr_rest),
            5: lambda: user.check_order(),
            6: lambda: handle_choice_6(z),
            7: lambda: handle_choice_7(z)}

        if (ch >= 8):
            break

        handle_choice[ch]()
