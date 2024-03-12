from openpyxl import Workbook


def write_to_excel(excel_data, file_path):
    wb = Workbook()
    ws = wb.active
    ws.append(["Email"])
    for row in excel_data:
        ws.append(row)
    wb.save(file_path)
