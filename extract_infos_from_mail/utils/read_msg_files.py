import os
import extract_msg
import re

regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")


def isValid(email) -> bool:
    if re.fullmatch(regex, email):
        return True
    return False


def read_msg_files(directory) -> list[list[str]]:
    excel_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".msg"):
            msg = extract_msg.openMsg(os.path.join(directory, filename))
            body = msg.body
            email = body.split("Email :")[1].split("\n")[0].split(" ")[1].strip()
            if isValid(email) and [email] not in excel_data:
                excel_data.append([email])
    return excel_data
