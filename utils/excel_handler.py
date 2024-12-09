import openpyxl
import os
from config.settings import EXCEL_PATH


def write_to_excel(page_url, testcase, status, comment):
    if not os.path.exists(EXCEL_PATH):
        # Create a new workbook and add a header row if the file doesn't exist
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Test Results"
        # Write header row
        sheet.append(["Page URL", "Test Case", "Pass/Fail", "Comments"])
        workbook.save(EXCEL_PATH)

    # Load the existing workbook
    workbook = openpyxl.load_workbook(EXCEL_PATH)
    sheet = workbook.active

    # Append the new test result row
    sheet.append([page_url, testcase, status, comment])

    # Save changes to the workbook
    workbook.save(EXCEL_PATH)
    workbook.close()
