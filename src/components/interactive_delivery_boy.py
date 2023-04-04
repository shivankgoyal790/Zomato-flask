from colorama import Back, Style


def delivery_interactive(delivery, z):
    choice = "1"
    while (choice != "4"):
        delivery.display_details()
        print(Back.RED)
        print("\nENTER 1 TO CHECK YOUR ORDERS ASSIGNED ")
        print("ENTER 2 TO UPDATE YOUR STATUS ")
        print("ENTER 3 TO UPDATE DELIVERY STATUS ")
        print("ENTER 4 TO EXIT ")
        print(Style.RESET_ALL)
        choice = input()
        if (choice == "1"):
            delivery.check_orders()
        elif (choice == "2"):
            delivery.update_status()
        elif (choice == "3"):
            z.list_of_orders.remove(delivery.myorders[0])
            delivery.update_delivery_status()
