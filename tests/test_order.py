from src.order import Order
from src.user.user import User
from src.restaurant.restaurant import Restaurant
from src.delivery_boy import Deliveryboy
import pytest


@pytest.fixture()
def order():
    user = User("124", "shivnak", "Asfg", "7894561230",
                "goyal@gmail.com", "12345678")
    rest = Restaurant("1245", "sam", "asfdg", "dominos@gmail.com", "12345678")
    agent = Deliveryboy("467", "rakesh", "7894561230",
                        "sam@gmail.com", "12345678")
    order = Order('113', user, rest, agent,
                  100)
    return order


# def test_createobj():
#     user = User("124", "shivnak", "Asfg", "7894561230",
#                 "goyal@gmail.com", "12345678")
#     rest = Restaurant("1245", "sam", "asfdg", "dominos@gmail.com", "12345678")
#     agent = Deliveryboy("467", "rakesh", "7894561230",
#                         "sam@gmail.com", "12345678")
#     order = Order('113', user, rest, agent,
#                   100)


def test_showobj(order):
    order.show_order()
