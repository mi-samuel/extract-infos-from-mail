from tkinter import Tk, filedialog


def select_directory():
    root = Tk()
    root.withdraw()

    directory = filedialog.askdirectory(title="Select Directory Containing .msg Files")

    root.destroy()

    return directory
