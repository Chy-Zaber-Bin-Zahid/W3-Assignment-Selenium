from selenium import webdriver
from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from utils.excel_handler import write_to_excel  # Updated to use the Excel handler

def test_h1_tag():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    try:
        # Find the H1 tag
        h1_tag = driver.find_element(By.TAG_NAME, 'h1')
        if h1_tag:
            write_to_excel(BASE_URL, "H1 Tag Test", "pass", "H1 tag exists")
    except Exception as e:
        # Write failure result to Excel
        write_to_excel(BASE_URL, "H1 Tag Test", "fail", f"H1 tag missing: {str(e)}")
    finally:
        # Quit the browser
        driver.quit()

if __name__ == "__main__":
    test_h1_tag()
