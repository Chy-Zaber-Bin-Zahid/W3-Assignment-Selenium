import pandas as pd
import os
from config.settings import EXCEL_PATH


def write_to_excel_scrape(site_url, campaign_id, site_name, browser, country_code, ip):
    # Prepare the data
    new_data = {
        "Site URL": [site_url],
        "Campaign ID": [campaign_id],
        "Site Name": [site_name],
        "Browser": [browser],
        "Country Code": [country_code],
        "IP": [ip]
    }
    new_row = pd.DataFrame(new_data)

    # Check if the Excel file exists
    if not os.path.exists(EXCEL_PATH):
        # Create a new DataFrame and save as a new Excel file
        new_row.to_excel(EXCEL_PATH, index=False, sheet_name="Scrape Data")
    else:
        # Load the existing Excel file
        with pd.ExcelFile(EXCEL_PATH) as existing_file:
            # Check if the sheet exists
            if 'Scrape Data' not in existing_file.sheet_names:
                # Create a new sheet 'Scrape Data' if it doesn't exist
                with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl', mode='a') as writer:
                    new_row.to_excel(writer, index=False, sheet_name="Scrape Data")
            else:
                # Load the existing sheet and append the new data
                existing_data = pd.read_excel(EXCEL_PATH, sheet_name="Scrape Data")
                updated_data = pd.concat([existing_data, new_row], ignore_index=True)
                updated_data.to_excel(EXCEL_PATH, index=False, sheet_name="Scrape Data")


def write_to_excel_test_results(page_url, testcase, status, comment):
    # Prepare the new row as a dictionary for test results
    new_data = {
        "Page URL": [page_url],
        "Test Case": [testcase],
        "Pass/Fail": [status],
        "Comments": [comment]
    }
    new_row = pd.DataFrame(new_data)

    # Check if the file exists
    if not os.path.exists(EXCEL_PATH):
        # Create a new DataFrame with headers if the file doesn't exist
        new_row.to_excel(EXCEL_PATH, index=False, sheet_name="Test Results")
    else:
        # Load the existing Excel file
        existing_data = pd.read_excel(EXCEL_PATH, sheet_name="Test Results", engine='openpyxl')

        # Append the new data
        updated_data = pd.concat([existing_data, new_row], ignore_index=True)

        # Save the updated data back to the "Test Results" sheet
        updated_data.to_excel(EXCEL_PATH, index=False, sheet_name="Test Results")
