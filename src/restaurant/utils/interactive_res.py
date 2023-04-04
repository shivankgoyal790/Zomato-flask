from colorama import Style
from src.restaurant.utils.rest_tasks_handler import add_new_menuitem, check_rest_orders, add_existing_item, update_status, deleteitems
from src.components.display_restaurant_interaction import display_res_interaction


def res_interactive(res, z):
    ch = 0
    while (ch != 6):

        print("\n CHECK OUR MENU")

        res.display_rest()
        res.show_menu()

        display_res_interaction()

        ch = int(input("ENTER CHOICE " + Style.RESET_ALL))
        if (ch >= 6):
            break

        handle_choice = {
            1: lambda: add_new_menuitem(res, z),
            2: lambda: check_rest_orders(res),
            3: lambda: add_existing_item(res, z),
            4: lambda: update_status(res),
            5: lambda: deleteitems(res)}

        handle_choice[ch]()
