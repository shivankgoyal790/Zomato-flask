from colorama import Back, Style


class Deliveryboy:
    def __init__(self, id, name, phone, email, password):
        self.id = id
        self.name = name
        self.earnings = 0
        self.status = "free"
        self.myorders = []
        self.phone = phone
        self.email = email
        self.password = password

    def check_orders(self):
        if (len(self.myorders) == 0):
            print("\nNO CURRENT ORDERS")
        else:
            for i in self.myorders:
                i.show_order()

    def update_status(self):
        if (self.status == "free"):
            self.status = "engaged"
        elif (self.status == "engaged"):
            if (len(self.myorders) > 0):
                print("PLEASE DELIVER THE CURRENT ORDERS FIRST")
            else:
                print(Back.YELLOW)
                print("\nSTATUS UPDATED")
                print(Style.RESET_ALL)
                self.status = "free"

    def update_delivery_status(self):
        if (len(self.myorders) == 0):
            print(Back.YELLOW)
            print("NO ORDERS IN THE QUEUE TO UPDATE")
            print(Style.RESET_ALL)
        else:
            self.earnings = self.earnings + 0.1 * \
                (self.myorders[0].totalpayment)
            self.myorders = []
            self.update_status()
            print(Back.YELLOW)
            print("\n ORDER DELIVERD")
            print(Style.RESET_ALL)

    def pickup_delivery(self, orders):
        self.myorders.append(orders)

    def display_details(self):
        print(Back.YELLOW)
        print("\nNAME :", self.name)
        print("PHONE :", self.phone)
        print("EARNINGS :", self.earnings)
        print("STATUS :", self.status)
        print(Style.RESET_ALL)
