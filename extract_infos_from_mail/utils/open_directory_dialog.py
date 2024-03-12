from tkinter import Tk, Button, Label, messagebox
from extract_infos_from_mail.utils.select_directory import select_directory
from extract_infos_from_mail.utils.select_excel_file import select_excel_file
from extract_infos_from_mail.utils.read_msg_files import read_msg_files
from extract_infos_from_mail.utils.write_to_excel import write_to_excel


def open_directory_dialog():
    def quit_application():
        root.destroy()

    def update_selection_labels(directory, excel_file):
        directory_label.config(text=f"Selected directory: {directory}")
        excel_label.config(text=f"Selected Excel file: {excel_file}")

    def process_selection():
        while True:
            directory = select_directory()
            if not directory:
                messagebox.showerror(
                    "Error", "No directory selected. Please try again."
                )
                continue

            excel_file_path = select_excel_file()
            if not excel_file_path:
                messagebox.showerror(
                    "Error", "No Excel file selected. Please try again."
                )
                continue

            excel_data = read_msg_files(directory)
            if not excel_data:
                messagebox.showerror(
                    "Error", "No .msg files found in the selected directory."
                )
                continue

            try:
                write_to_excel(excel_data, excel_file_path)
                messagebox.showinfo("Success", "Excel file created successfully.")
                update_selection_labels(directory, excel_file_path)
                break
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    root = Tk()
    root.title("Extract Email Addresses from .msg Files")

    label = Label(
        root, text="Click the button to select a directory and an Excel file."
    )
    label.pack(pady=10)

    button = Button(
        root, text="Select Directory and Excel File", command=process_selection
    )
    button.pack(pady=5)

    quit_button = Button(root, text="Quit", command=quit_application)
    quit_button.pack(pady=5)

    directory_label = Label(root, text="")
    directory_label.pack()

    excel_label = Label(root, text="")
    excel_label.pack()

    root.mainloop()
