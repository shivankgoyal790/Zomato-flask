from src.menuitems import Menuitems
from src.item import Item
import unittest
from unittest.mock import patch


# print ke andar print mock
class Test_Menuitems(unittest.TestCase):

    @patch.object(Item, 'display_item')
    def test_display_menuitem(self, mock_display_item):
        mock_display_item.side_effect = lambda price, rating, no_of_ratings: None
        item = Item("1", "Dosa")
        Menuitem = Menuitems(item, 100)

        Menuitem.display_menuitem()
        mock_display_item.assert_called_once_with(100, 0, 0)

    def test_can_create_obj(self):
        item = Item("1", "Dosa")
        Menuitem = Menuitems(item, 100)


if __name__ == '__main__':
    unittest.main()
