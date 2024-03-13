import argparse

from extract_infos_from_mail.utils.initialisation import initialisation


if __name__ == "__main__":
    # Configuration de l'analyseur d'arguments de ligne de commande
    parser = argparse.ArgumentParser(
        description="Extract informations from .txt file and write to an Excel file."
    )
    parser.add_argument("file", help="Path to the file containing the informations")
    parser.add_argument("excel_file", help="Excel file name")

    # Analyse des arguments de la ligne de commande
    args = parser.parse_args()

    # Appel de la fonction principale avec les arguments fournis
    initialisation(args.file, args.excel_file)
