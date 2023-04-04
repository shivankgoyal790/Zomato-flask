class Menuitems:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.rating = 0
        self.no_of_ratings = 0

    def display_menuitem(self):
        self.item.display_item(self.price, self.rating, self.no_of_ratings)
