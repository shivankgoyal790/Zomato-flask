import abc
from src.user.user import User
from src.delivery_boy import Deliveryboy
from src.restaurant.restaurant import Restaurant
import random
from src.helper.emailchecker import validemailcheck
from src.helper.password_checker import password_checker
from src.helper.phonechecker import phonechecker


class Registration():
    @abc.abstractmethod
    def Register(self):
        pass


class CreateRestaurant(Registration):

    def Register(self, entity_list):

        id = random.randint(3000, 4000)
        name = input("Enter Your Restaurant Name ")
        address = input("Enter Your Address ")
        email = validemailcheck(entity_list)
        password = password_checker()
        res = Restaurant(id, name, address, email, password)
        res.create_menu()
        return res


class CreateDeliveryBoy(Registration):

    def Register(self, entity_list):

        id = random.randint(5000, 6000)
        name = input("ENTER NAME OF AGENT ")
        phone = phonechecker()
        email = validemailcheck(entity_list)
        password = password_checker()
        agent = Deliveryboy(id, name, phone, email, password)

        return agent


class CreateUser(Registration):

    def Register(self, entity_list):

        id = random.randint(4000, 5000)
        name = input("ENTER YOUR NAME ")
        address = input("ENTER YOUR ADDRESS ")
        phone = phonechecker()
        email = validemailcheck(entity_list)
        password = password_checker()
        user = User(id, name, address, phone, email, password)

        print("\nYOU ARE SUCCESSFULLY REGISTERED\n")

        return user
