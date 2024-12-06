import openpyxl
import os

EXCEL_PATH = "./reports/test_report.xlsx"

def write_to_excel(page_url, testcase, status, comment):
    # Check if the Excel file exists
    if not os.path.exists(EXCEL_PATH):
        # Create a new workbook and add a header row
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Test Results"
        sheet.append(["Page URL", "Test Case", "Pass/Fail", "Comments"])
        workbook.save(EXCEL_PATH)

    # Load the existing workbook
    workbook = openpyxl.load_workbook(EXCEL_PATH)
    sheet = workbook.active

    # Append the test result row
    sheet.append([page_url, testcase, status, comment])

    # Save changes to the Excel file
    workbook.save(EXCEL_PATH)
