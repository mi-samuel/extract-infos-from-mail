import re

from extract_infos_from_mail.utils.constants.HEADERS import HEADERS


regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")


def isValid(email) -> bool:
    if re.fullmatch(regex, email):
        return True
    return False


def read_txt_file(path_to_file):
    excel_data = []
    with open(path_to_file, "r") as file:
        content = file.read()
        new_entry = []
        for line in content.split("\n"):
            if line.startswith("BEGIN"):
                if len(new_entry) > 0:
                    excel_data.append(new_entry)
                new_entry = []
            elif line.startswith("Code pro partenaire :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Civilité :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Nom :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Prénom :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Adresse :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Adresse (complément) :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Code Postal :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Ville :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Email :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Téléphone :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Date de naissance :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Date de permis :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Profession :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("CRM :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Nombre de sinistres depuis les 36 derniers mois :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Retrait ou suspension de permis :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Marque :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Modèle :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Puissance :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("PTAC :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Carburant :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Valeur actuelle en € :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Date de première mise en circulation :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Usage kilométrique annuel :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Conducteurs :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Type de garage :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Formule :"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("Comment avez-vous entendu parler de nous?"):
                new_entry.append(line.split("?")[1].split("\n")[0])
            elif line.startswith("Louez-vous ou comptez-vous louer votre camping-car?"):
                new_entry.append(line.split("?")[1].split("\n")[0])
            elif line.startswith("COTISATION ANNUELLE TTC	:"):
                new_entry.append(line.split(": ")[1].split("\n")[0])
            elif line.startswith("FIRST"):
                if len(line.split("\t")) > 1:
                    new_entry.append(line.split("\t")[1].split("\n")[0])
                else:
                    new_entry.append("")
            elif line.startswith("PREMIUM"):
                if len(line.split("\t")) > 1:
                    new_entry.append(line.split("\t")[1].split("\n")[0])
                else:
                    new_entry.append("")

    return excel_data
