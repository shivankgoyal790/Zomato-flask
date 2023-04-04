from src.item import Item


def test_cancreateobject():
    item = Item('1', "dosa")
    print(item)


def test_candisplayitem():
    item = Item('1', "dosa")
    item.display_item(1, 2, 3)
