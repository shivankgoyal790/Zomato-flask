from src.user.user import User
from src.menuitems import Menuitems
from src.item import Item
import pytest
from unittest.mock import patch
from io import StringIO


@ pytest.fixture()
def setup():
    user = User("1221", "shivank", "sector 134",
                "7906558590", "goyal@gmail.com", "12345678")
    return user


def test_can_updatecart(setup):
    item = Item("124", "pasta")
    menuitem = Menuitems(item, 100)
    setup.update_cart(menuitem)
    assert setup.foodlist[0] == menuitem


def test_checkcart_is_empty(setup, monkeypatch):
    expected_output = "\n\nYour Cart is Empty"
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        setup.check_cart()
        assert mock_stdout.getvalue(), expected_output


def test_check_cart(setup):


def test_removefromcart(setup):
    item = Item("124", "pasta")
    menuitem = Menuitems(item, 100)
    setup.foodlist.append(menuitem)
    setup.remove_fromcart(1)
