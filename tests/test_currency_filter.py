import time  # Import time for delays
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import BASE_URL
from utils.excel_handler import write_to_excel_test_results

def test_currency_filter():
    driver = webdriver.Chrome()

    # Open the website
    driver.get(BASE_URL)

    try:
        # Wait until the dropdown is visible and scroll it into view
        dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "js-currency-sort-footer"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)

        # Use JavaScript click to open the dropdown
        driver.execute_script("arguments[0].click();", dropdown)

        # Add a delay to make the dropdown opening slower
        time.sleep(2)

        # Wait for the options to load
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-currency-sort-footer ul.select-ul li"))
        )

        # Iterate through options
        for i, option in enumerate(options):
            currency_text = option.text.strip()
            print(f"Option {i + 1}: {currency_text}")

            try:
                # Scroll and click the option
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
                time.sleep(1)  # Delay before clicking the option
                driver.execute_script("arguments[0].click();", option)

                # Add a delay to simulate waiting for the price to update
                time.sleep(2)

                # Wait for price info to update
                price_info = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".price-info.js-price-value"))
                )
                print(f"Price info after selecting {currency_text}: {price_info.text}")

                # Write successful test result to Excel
                write_to_excel_test_results(
                    page_url=BASE_URL,
                    testcase=f"Currency Filter - {currency_text}",
                    status="Pass",
                    comment=f"Successfully updated price info: {price_info.text}"
                )

            except Exception as e:
                print(f"Error for currency {currency_text}: {e}")
                # Write failed test result to Excel
                write_to_excel_test_results(
                    page_url=BASE_URL,
                    testcase=f"Currency Filter - {currency_text}",
                    status="Fail",
                    comment=str(e)
                )

            # Reopen the dropdown for the next iteration
            dropdown = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "js-currency-sort-footer"))
            )
            time.sleep(1)  # Delay before reopening the dropdown
            driver.execute_script("arguments[0].click();", dropdown)

    except Exception as e:
        print(f"An error occurred: {e}")
        # Log the overall test failure
        write_to_excel_test_results(
            page_url=BASE_URL,
            testcase="Currency Filter",
            status="Fail",
            comment=str(e)
        )
    finally:
        driver.quit()

if __name__ == "__main__":
    test_currency_filter()
