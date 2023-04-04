# Service class
from src.registration import CreateUser, CreateRestaurant, CreateDeliveryBoy
import random
from src.restaurant.restaurant import Restaurant
from src.delivery_boy import Deliveryboy
from colorama import Back, Style
from src.order import Order


class Zomato:
    def __init__(self):

        self.list_of_orders = []
        self.list_of_enities = []
        self.list_of_restaurant = []
        self.list_of_users = []
        self.list_of_items = []
        self.list_of_delivery_boy = []

    @staticmethod
    def get_restaurant_list(entities):
        list_of_restaurant = []

        for i in entities:
            if (isinstance(i, Restaurant)):
                list_of_restaurant.append(i)

        return list_of_restaurant

    def register(self, type):

        if (type == 'customer'):
            user = CreateUser()
            myuser = user.Register(self.list_of_enities)
            self.list_of_enities.append(myuser)
        elif (type == "restaurant"):
            res = CreateRestaurant()
            myrest = res.Register(self.list_of_enities)
            self.list_of_enities.append(myrest)
        elif (type == "deliveryboy"):
            agent = CreateDeliveryBoy()
            myagent = agent.Register(self.list_of_enities)
            self.list_of_enities.append(myagent)

    def display_restaurants(self):

        list_of_rest = Zomato.get_restaurant_list(self.list_of_enities)
        for i in list_of_rest:
            if (i.status == 'open'):
                print(list_of_rest.index(i) + 1, end="  ")
                i.display_rest()

    def authenticate(self, email, password):

        for i in self.list_of_enities:
            if (i.email == email and i.password == password):
                return i

        return 0

    def check_orders(self):

        for i in self.list_of_orders:
            i.show_order()

    def assign_delivery(self):

        list_of_delivery_boy = []

        for i in self.list_of_enities:
            if (isinstance(i, Deliveryboy)):
                list_of_delivery_boy.append(i)

        return random.choice(self.list_of_delivery_boy)

    def update_list_of_orders(self, order):
        self.list_of_orders.append(order)

    def find_restaurant(self, index):

        list_of_restaurant = Zomato.get_restaurant_list(self.list_of_enities)

        if (index > len(list_of_restaurant)):
            return 0

        return list_of_restaurant[index-1]

    def place_order(self, user, rest, agent):
        print("\nOrder Placed")
        totalprice = 0
        for item in user.foodlist:
            totalprice += item.price
        order = Order(random.randint(6000, 7000),
                      user, rest, agent, totalprice)
        order.show_order()
        user.curr_orders.append(order)
        self.list_of_orders.append(order)
        rest.curr_orders.append(order)
        agent.myorders.append(order)
        user.foodlist = []

    def find_item(self, index):
        if (index > len(self.list_of_items)):
            return 0
        return self.list_of_items[index - 1]

    def display_all_items(self):
        for i in self.list_of_items:
            print(self.list_of_items.index(i) + 1, end=" ")
            i.display_menuitem()

    def update_rest_rating(self, index, rate):

        list_of_restaurant = Zomato.get_restaurant_list(self.list_of_enities)

        while (index > len(list_of_restaurant)):
            index = int(input("ENTER A VALID INDEX AGAIN"))

        rest = list_of_restaurant[index - 1]
        avg = (rest.rating*(rest.no_of_ratings) + rate) / \
            (rest.no_of_ratings + 1)
        rest.no_of_ratings += 1
        rest.rating = avg

        print(Back.YELLOW + "\nRATING UPDATED" + Style.RESET_ALL)

    def update_item_rating(self, index, rate):

        while (index > len(self.list_of_items)):
            index = int(input("ENTER A VALID INDEX AGAIN"))

        item = self.list_of_items[index - 1]

        avg = (item.rating*(item.no_of_ratings) + rate) / \
            (item.no_of_ratings + 1)
        item.no_of_ratings += 1
        item.rating = avg

        print(Back.YELLOW + "\nRATING UPDATED" + Style.RESET_ALL)

    def rate_current_rest(self, rest, rate):
        list_of_restaurant = Zomato.get_restaurant_list()

        res = 0
        for i in list_of_restaurant:
            if i.rest_id == rest:
                res = i
                break

        avg = (res.rating*(res.no_of_ratings) + rate) / \
            (res.no_of_ratings + 1)
        res.no_of_ratings += 1
        res.rating = avg

        print(Back.YELLOW + "\nRATING UPDATED" + Style.RESET_ALL)
