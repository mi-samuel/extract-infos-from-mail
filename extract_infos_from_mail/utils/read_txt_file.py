NB_COLUMNS = 34


def read_txt_file(path_to_file):
    excel_data = []

    with open(path_to_file, "r") as file:
        content = file.read()
        new_entry = [""] * NB_COLUMNS
        append = False
        is_city = False
        is_postal_code = False

        for line in content.split("\n"):
            if line.startswith("BEGIN"):
                if append:
                    excel_data.append(new_entry)
                    new_entry = [""] * NB_COLUMNS
                    is_city = False
                    is_postal_code = False

            elif line.startswith("Code pro partenaire :"):
                if len(line.split(": ")) > 1:
                    new_entry[0] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Civilité :"):
                if len(line.split(": ")) > 1:
                    new_entry[1] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Nom :"):
                if len(line.split(": ")) > 1:
                    new_entry[2] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Prénom :"):
                if len(line.split(": ")) > 1:
                    new_entry[3] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Adresse :"):
                if len(line.split(": ")) > 1:
                    new_entry[4] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Adresse (complément) :"):
                if len(line.split(": ")) > 1:
                    new_entry[5] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Code Postal :"):
                if len(line.split(": ")) > 1:
                    if is_postal_code is False:
                        new_entry[6] = line.split(": ")[1].split("\n")[0]
                        is_postal_code = True
                    else:
                        new_entry[25] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Ville :"):
                if len(line.split(": ")) > 1:
                    if is_city is False:
                        new_entry[7] = line.split(": ")[1].split("\n")[0]
                        is_city = True
                    else:
                        new_entry[26] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Email :"):
                if len(line.split(": ")) > 1:
                    new_entry[8] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Téléphone :"):
                if len(line.split(": ")) > 1:
                    new_entry[9] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Date de naissance :"):
                if len(line.split(": ")) > 1:
                    new_entry[10] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Date de permis :"):
                if len(line.split(": ")) > 1:
                    new_entry[11] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Profession :"):
                if len(line.split(": ")) > 1:
                    new_entry[12] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("CRM :"):
                if len(line.split(": ")) > 1:
                    new_entry[13] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Nombre de sinistres depuis les 36 derniers mois :"):
                if len(line.split(": ")) > 1:
                    new_entry[14] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Retrait ou suspension de permis :"):
                if len(line.split(": ")) > 1:
                    new_entry[15] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Marque :"):
                if len(line.split(": ")) > 1:
                    new_entry[16] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Modèle :"):
                if len(line.split(": ")) > 1:
                    new_entry[17] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Puissance :"):
                if len(line.split(": ")) > 1:
                    new_entry[18] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("PTAC :"):
                if len(line.split(": ")) > 1:
                    new_entry[19] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Carburant :"):
                if len(line.split(": ")) > 1:
                    new_entry[20] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Valeur actuelle en € :"):
                if len(line.split(": ")) > 1:
                    new_entry[21] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Date de première mise en circulation :"):
                if len(line.split(": ")) > 1:
                    new_entry[22] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Usage kilométrique annuel :"):
                if len(line.split(": ")) > 1:
                    new_entry[23] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Conducteurs :"):
                if len(line.split(": ")) > 1:
                    new_entry[24] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Type de garage :"):
                if len(line.split(": ")) > 1:
                    new_entry[27] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Formule :"):
                if len(line.split(": ")) > 1:
                    new_entry[28] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("Comment avez-vous entendu parler de nous?"):
                if len(line.split("?")) > 1:
                    new_entry[29] = line.split("?")[1].split("\n")[0]
            elif line.startswith("Louez-vous ou comptez-vous louer votre camping-car?"):
                if len(line.split("?")) > 1:
                    new_entry[30] = line.split("?")[1].split("\n")[0]
            elif (
                line.startswith("COTISATION ANNUELLE TTC :")
                or line.startswith("COTISATION ANNUELLE TTC : ")
                or line.startswith("COTISATION ANNUELLE TTC :")
            ):
                if len(line.split(": ")) > 1:
                    new_entry[31] = line.split(": ")[1].split("\n")[0]
            elif line.startswith("FIRST"):
                if len(line.split(" ")) > 1:
                    new_entry[32] = line.split(" ")[1].split("\n")[0]
            elif line.startswith("PREMIUM"):
                if len(line.split(" ")) > 1:
                    new_entry[33] = line.split(" ")[1].split("\n")[0]
            else:
                append = True

    return excel_data
