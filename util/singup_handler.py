
def signup_handler(z):
    print("IF YOU ARE A USER SELECT 1 ")
    print("IF YOU ARE A RESTAURANT SELECT 2 ")
    print("IF YOU ARE A DELIVERY AGENT SELECT 3")
    choice = input()

    if (choice == '1'):
        user = z.register("customer")
    elif (choice == '2'):
        rest = z.register("restaurant")
    else:
        agent = z.register("deliveryboy")
