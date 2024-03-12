from tkinter import Tk, filedialog


def select_excel_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        title="Save Excel File",
    )
    return file_path
