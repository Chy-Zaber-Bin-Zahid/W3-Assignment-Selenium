from selenium import webdriver
from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from utils.csv import write_to_csv

def test_h1_tag():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    try:
        h1_tag = driver.find_element(By.TAG_NAME, 'h1')
        write_to_csv(BASE_URL, "H1 Tag Test", "pass", "H1 tag exists")
    except Exception:
        write_to_csv(BASE_URL, "H1 Tag Test", "fail", "H1 tag missing")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_h1_tag()
