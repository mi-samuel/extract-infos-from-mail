from extract_infos_from_mail.utils.read_txt_file import read_txt_file
from extract_infos_from_mail.utils.write_to_excel import write_to_excel
from extract_infos_from_mail.utils.clean_file import clean_file


def initialisation(file_path, excel_file, is_cleaned=False) -> None:
    # Lire les fichiers .msg dans le dossier spécifié
    if is_cleaned:
        file_path = clean_file(file_path)

    excel_data = read_txt_file(file_path)
    if not excel_data:
        print("No .txt file found. Exiting...")
        return

    try:
        # Écrire les données dans le fichier Excel spécifié
        write_to_excel(excel_data, excel_file)
        print("Excel file created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
