from selenium import webdriver
from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from utils.excel_handler import write_to_excel_test_results


def test_h1_tag():
    print('Test 1 started.')
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    try:
        h1_tag = driver.find_element(By.TAG_NAME, 'h1')
        if h1_tag:
            write_to_excel_test_results(BASE_URL, "H1 Tag Test", "Pass", "H1 tag exists")
            print('Test 1 passed.')
    except Exception as e:
        write_to_excel_test_results(BASE_URL, "H1 Tag Test", "Fail", f"H1 tag missing: {str(e)}")
        print('Test 1 failed.')
    finally:
        driver.quit()
        print('Test 1 closed.')


if __name__ == "__main__":
    test_h1_tag()
