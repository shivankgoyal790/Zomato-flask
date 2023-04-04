from src.user.utils.userchoice_interaction import user_choice_interaction2
from src.user.utils.users_tasks_handler import update_cart, remove_from_cart, place_order


def handle_choice_1(z, user):

    index = int(input(
                "\nENTER THE INDEX TO CHECK MENU OF THAT RESTAUTANT "))
    rest = z.find_restaurant(index)

    mychoice = "1"
    while (mychoice != "4"):

        print("\n\nCheck Our Menu")
        rest.show_menu()

        user_choice_interaction2()
        mychoice = int(input())

        handle_choice_dict = {
            1: update_cart(user, rest),
            2: remove_from_cart(user),
            3: place_order(user, z, rest)}

        if (mychoice >= 4):
            break

        handle_choice_dict[mychoice]


def handle_choice_6(z):

    index = int(input("ENTER THE INDEX OF RESTAURANT TO RATE "))
    rate = int(input("ENTER THE RATING BETWEEN 0-5 "))
    while (rate < 0 or rate > 5):
        rate = int(input("ENTER THE RATING BETWEEN 0-5 "))
    z.update_rest_rating(index, rate)


def handle_choice_7(z):
    z.display_all_items()

    index = int(input("ENTER THE INDEX OF ITEM TO RATE "))
    rate = int(input("ENTER THE RATING BETWEEN 0-5 "))

    while (rate < 0 or rate > 5):
        rate = int(input("ENTER THE RATING BETWEEN 0-5 "))

    z.update_item_rating(index, rate)
