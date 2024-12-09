from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.excel_handler import write_to_excel_test_results
from config.settings import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_currency_filter():
    # Initialize the WebDriver (ensure you have the appropriate driver installed, e.g., chromedriver)
    driver = webdriver.Chrome()  # Update the path if needed
    driver.get(BASE_URL)  # Go to the base URL

    # Find and click the currency dropdown button
    wait = WebDriverWait(driver, 10)
    currency_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "js-currency-sort-footer")))

    driver.execute_script("arguments[0].scrollIntoView(true);", currency_dropdown)
    
    # Click the currency dropdown button
    currency_dropdown.click()
    # # Wait for the dropdown options to appear
    # time.sleep(2)

    # # Find the 'BDT' option (Bangladesh Taka) from the dropdown list
    # bdt_option = driver.find_element(By.XPATH, "//li[@data-currency-country='BD']//p[contains(text(), '৳ (BDT)')]")

    # # Click on the 'BDT' option
    # bdt_option.click()

    # # Wait for the page to reflect the currency change
    # time.sleep(3)

    # # Print the selected currency text
    # selected_currency = bdt_option.text.strip()
    # print(f"Selected Currency: {selected_currency}")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_currency_filter()
