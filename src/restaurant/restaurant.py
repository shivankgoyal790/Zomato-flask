from src.restaurant.utils.interactive_res import res_interactive
from colorama import Back, Style
import random
from src.menuitems import Menuitems
from src.item import Item
from src.menu import Menu


class Restaurant:

    def __init__(self, id, name, address, email, password):
        self.rest_id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        self.status = "open"
        self.rating = 0
        self.no_of_ratings = 0
        self.curr_orders = []

    def create_menu(self):
        mymenu = Menu(random.randint(1000, 2000), self.rest_id)
        self.menu = mymenu

    def create_new_menuitem(self):
        name = input("\nENTER NAME OF THE DISH ")
        price = int(input("ENTER PRICE OF DISH "))
        item = Item(random.randint(1, 1000), name)
        newitem = Menuitems(item, price)
        self.menu.menuitemlist.append(newitem)
        print("\nITEM SUCCESSFULLY ADDED")
        return newitem

    def add_item_from_existing_list(self, item, price):
        newitem = Menuitems(item, price)
        self.menu.menuitemlist.append(newitem)
        print("NEW ITEM ADDED TO MENU")

    def deleteitem_from_menu(self):
        if (len(self.menu.menuitemlist) == 0):
            print(Back.YELLOW)
            print("NOTHING TO REMOVE")
            print(Style.RESET_ALL)
            return 0
        else:
            dish = int(input("\nENTER THE INDEX OF ITEM TO DELETE"))
            item = self.menu.menuitemlist[dish - 1]
            self.menu.menuitemlist.remove(item)
            return 1

    def update_status(self):
        if (self.status == "open"):
            self.status = "closed"
        else:
            self.status = "open"

    def check_orders(self):
        if (len(self.curr_orders) == 0):
            print(Back.YELLOW)
            print("\n\nNO CURRENT ORDERS\n")
            print(Style.RESET_ALL)
        else:
            for i in self.curr_orders:
                i.show_order()

    def show_menu(self):
        self.menu.display_allitems()

    def find_item(self, item_id):
        return self.menu.find_item(item_id)

    def display_rest(self):

        print("RESTAURANT NAME :", self.name, "   ", "LOCATION :", self.address,
              "    ", "RATING :", "N/A" if (self.rating == 0) else self.rating, "    ", "NO OF RATINGS :", self.no_of_ratings, "    ", "STATUS :", self.status)

    def handle_restaurant_interaction(self, z):
        res_interactive(self, z)
