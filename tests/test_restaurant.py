from src.menu import Menu
from src.item import Item
from src.menuitems import Menuitems
from src.restaurant.restaurant import Restaurant
import pytest
from io import StringIO
import unittest
from unittest.mock import patch


@pytest.fixture()
def setup1():
    rest = Restaurant("123", "Sagar Ratna", "GTBNagar",
                      "sagar@gmail.com", "12345678")
    return rest


@pytest.fixture()
def setup(setup1):
    mymenu = Menu("123", setup1.rest_id)
    return mymenu


@pytest.fixture()
def setup3(setup1, setup):
    setup1.menu = setup
    return setup1


def test_can_add_item_in_menu(setup3, monkeypatch):
    number_inputs = StringIO('Shahi Paneer\n100\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    response = setup3.create_new_menuitem()
    item = Item(1, "Shahi Paneer")
    newitem = Menuitems(item, 100)
    assert response.item.name == newitem.item.name


def test_remove_item_no_item_in_list(setup3):
    expected_output = "NOTHING TO REMOVE\n"
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        setup3.deleteitem_from_menu()
        assert mock_stdout.getvalue(), expected_output


def test_can_remove_item(setup3, monkeypatch):
    number_inputs = StringIO('1\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    item = Item(1, "Shahi Paneer")
    newitem = Menuitems(item, 100)
    setup3.menu.menuitemlist.append(newitem)
    setup3.deleteitem_from_menu()
    assert len(setup3.menu.menuitemlist) == 0


def test_check_no_order_is_placed(setup1):
    expected_output = "\n\nNO CURRENT ORDERS\n"
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        setup1.check_orders()
        assert mock_stdout.getvalue(), expected_output


def test_checklist_of_orders(setup1):
    setup1.check_orders()


def test_can_update_status(setup1):
    setup1.update_status()
    assert setup1.status == "closed"
