from extract_infos_from_mail.utils.select_directory import select_directory
from extract_infos_from_mail.utils.select_excel_file import select_excel_file
from extract_infos_from_mail.utils.read_msg_files import read_msg_files
from extract_infos_from_mail.utils.write_to_excel import write_to_excel


def main():
    directory = select_directory()
    if not directory:
        print("No directory selected. Exiting...\n")
        return
    excel_file_path = select_excel_file()
    if not excel_file_path:
        print("No Excel file selected. Exiting...\n")
        return
    excel_data = read_msg_files(directory)
    write_to_excel(excel_data, excel_file_path)
    print("Excel file created successfully.\n")


if __name__ == "__main__":
    main()
