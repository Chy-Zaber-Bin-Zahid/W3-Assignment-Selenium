import openpyxl
import os

EXCEL_PATH = "./reports/test_report.xlsx"

def write_to_excel(page_url, testcase, status, comment):
    """
    Appends test results to an Excel file without overwriting previous data.
    
    If the file does not exist, it creates a new workbook and writes the header row first.

    Args:
        page_url (str): The URL of the page being tested.
        testcase (str): The name of the test case.
        status (str): Pass/Fail status of the test case.
        comment (str): Additional comments or error messages.
    """
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
