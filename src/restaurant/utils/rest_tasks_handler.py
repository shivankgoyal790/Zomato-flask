from colorama import Back, Style


def add_new_menuitem(res, z):
    menuitem = res.create_new_menuitem()
    z.list_of_items.append(menuitem)


def check_rest_orders(res):
    res.check_orders()


def add_existing_item(res, z):
    z.display_all_items()
    index = int(input("\nENTER THE INDEX OF THE ITEM TO ADD"))
    menuitem = 0
    while (menuitem == 0):
        menuitem = z.find_item(index)
    if menuitem not in res.menu.menuitemlist:
        price = int(input("\nENTER THE PRICE OF ITEM "))
        res.add_item_from_existing_list(menuitem.item, price)
    else:
        print(Back.YELLOW + "\n\nITEM ALREADY EXIST" + Style.RESET_ALL)


def update_status(res):
    res.update_status()


def deleteitems(res):
    x = res.deleteitem_from_menu()
    if (x):
        print("\nITEM DELETED FROM MENU")
