from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
from config.settings import BASE_URL
from utils.excel_handler import write_to_excel
import requests


def get_all_links(driver):
    """Extract all anchor tag links from the page."""
    links = set()
    elements = driver.find_elements(By.TAG_NAME, "a")
    for element in elements:
        href = element.get_attribute("href")
        if href:  # Filter out empty or None hrefs
            links.add(href)
    return links


def test_url_status():
    print('Test 4 started.')
    """Check the status of all links on the page and log results in Excel."""
    driver = webdriver.Chrome()
    try:
        # Open the base URL
        driver.get(BASE_URL)
        
        # Extract all links from the page
        links = get_all_links(driver)
        
        for link in links:
            # Resolve relative URLs
            full_url = urljoin(BASE_URL, link)
            try:
                # Check the status of the URL
                response = requests.get(full_url, timeout=10)
                status_code = response.status_code
                
                if status_code == 404:
                    write_to_excel(full_url, "URL Status Test", "Fail", "Status code 404")
                    print(f"Test 4 failed url -> {full_url} - 404")
                else:
                    write_to_excel(full_url, "URL Status Test", "Pass", f"Status code {status_code}")
                    print(f"Test 4 passed url -> {full_url} - 200")
            except Exception as e:
                # Handle errors like timeouts or invalid URLs
                write_to_excel(full_url, "URL Status Test", "Fail", f"Error: {str(e)}")
                print(f"Test 4 failed url -> {full_url} - 404")
    finally:
        # Quit the browser
        driver.quit()
        print('Test 4 closed.')


if __name__ == "__main__":
    test_url_status()
