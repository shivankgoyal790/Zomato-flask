import re

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


def validemailcheck(email):
    if re.search(regex, email) == None:
        return 0

    return 1
