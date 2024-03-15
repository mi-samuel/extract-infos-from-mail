import argparse

from extract_infos_from_mail.utils.initialisation import initialisation


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract informations from .txt file and write to an Excel file."
    )
    parser.add_argument("file", help="Path to the file containing the informations")
    parser.add_argument("excel_file", help="Excel file name")

    parser.add_argument(
        "--clean",
        help="Clean the file before reading it",
        action="store_true",
    )

    args = parser.parse_args()

    initialisation(args.file, args.excel_file, args.clean)
