from colorama import Back, Style
from src.user.utils.ineractive_user import user_interactive_display


class User:

    def __init__(self, id, name, address, phone, email, password):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        self.curr_rest = ""
        self.curr_orders = []
        self.foodlist = []

    def update_cart(self, menuitem):
        self.foodlist.append(menuitem)
        print("\n Item Added Successfully")

    def remove_fromcart(self, index):
        self.foodlist.pop(index-1)
        print("\nSucessfully removed from cart")

    def check_cart(self):
        if (len(self.foodlist) == 0):
            print(Back.YELLOW + "\n\nYour Cart is Empty" + Style.RESET_ALL)
        else:
            totalprice = 0
            for item in self.foodlist:
                totalprice += item.price
            print(Back.YELLOW)
            print("\nCurrent items in your cart")
            count = 1
            for i in self.foodlist:
                print(count, end="  ")
                count = count + 1
                i.display_menuitem()
            print("Total Bill is", totalprice)
            print(Style.RESET_ALL)

    def check_order(self):
        if (len(self.curr_orders) == 0):
            print(Back.YELLOW)
            print("No Current Orders")
            print(Style.RESET_ALL)
        else:
            for i in self.curr_orders:
                i.show_order()

    def handle_user_interaction(self, z):
        user_interactive_display(self, z)
