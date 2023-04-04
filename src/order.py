from colorama import Back, Style


class Order:
    def __init__(self, id, user, rest, agent, price):
        self.id = id
        self.rest = rest
        self.user = user
        self.agent = agent
        self.itemlist = user.foodlist
        self.totalpayment = price
        self.status = "not delivered"

    def show_order(self):
        print(Back.YELLOW)
        print("\nORDER SUMMARY !!")
        print("\nORDER ID :  ", self.id)
        print("RESTAURANT NAME :  ", self.rest.name)
        print("DELIVER TO :  ", self.user.name)
        print("DELIVERY LOCATION :", self.user.address)
        print("DELIVERY BOY : ", self.agent.name)
        print("TOTAL BILL :  ", self.totalpayment)
        print("STATUS :", self.status)
        print(Style.RESET_ALL)
        print("\n\nITEMS ORDERED")

        for i in self.itemlist:
            i.display_menuitem()
