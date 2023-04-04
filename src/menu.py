class Menu:
    def __init__(self, id, rest_id):
        self.id = id
        self.menuitemlist = []
        self.rest_id = rest_id

    def find_item(self, index):
        if (index > len(self.menuitemlist)):
            return 0
        return self.menuitemlist[index - 1]

    def display_allitems(self):
        if (len(self.menuitemlist) == 0):
            print("NO ITEMS IN THE MENU")
        else:
            for item in self.menuitemlist:
                print(self.menuitemlist.index(item) + 1, end="  ")
                item.display_menuitem()
