from src.menu import Menu
import unittest
from unittest.mock import patch
from src.menuitems import Menuitems
from src.item import Item
from io import StringIO


class Test_Menu(unittest.TestCase):

    def test_display_allitems_no_items(self):
        menu = Menu("124", "456")
        expected_output = "NO ITEMS IN THE MENU\n"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            menu.display_allitems()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch.object(Menuitems, 'display_menuitem')
    def test_display_menuitem(self, mock_display_menuitem):
        item = Item("123", "dosa")
        menuitem1 = Menuitems(item, 10)
        menuitem2 = Menuitems(item, 20)
        menu = Menu("123", "456")
        menu.menuitemlist.append(menuitem1)
        menu.menuitemlist.append(menuitem2)
        mock_display_menuitem.side_effect = lambda: None
        menu.display_allitems()
        mock_display_menuitem.assert_called_with()


if __name__ == '__main__':
    unittest.main()
