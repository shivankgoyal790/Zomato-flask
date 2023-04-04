import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check_if_already_exists(entity_list, email):
    for i in entity_list:
        if (i.email == email):
            return 0
    return 1


def validemailcheck(entity_list=[]):
    email = input("ENTER YOUR VALID EMAIL ")
    while re.search(regex, email) == None or check_if_already_exists(entity_list, email) == 0:
        email = input("ENTER YOUR VALID EMAIL ")

    return email
