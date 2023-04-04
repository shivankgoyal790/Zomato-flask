class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_item(self, price, rating, no_of_rating):
        print("id :", self.id, "   ", "Dish Name", self.name, "   ", "rating :",
              "N/A" if (rating == 0) else rating, "   ", "NUMBER OF RATINGS :", no_of_rating, "   ", "price:", price)
