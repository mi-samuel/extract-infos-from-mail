import re

regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")


def isValid(email) -> bool:
    if re.fullmatch(regex, email):
        return True
