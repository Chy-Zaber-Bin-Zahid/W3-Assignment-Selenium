from selenium import webdriver
from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from utils.excel_handler import write_to_excel_test_results

def test_image_alt():
    print('Test 3 started.')
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    try:
        # Find all image elements
        images = driver.find_elements(By.TAG_NAME, "img")
        
        if not images:
            write_to_excel_test_results(BASE_URL, "Image Alt Attribute Test", "Fail", "No images found")
            print('Test 3 failed.')
            return
        
        missing_alt = []  # List to store images missing alt attributes
        empty_alt = []    # List to store images with empty alt attributes

        for img in images:
            alt = img.get_attribute("alt")
            if alt is None:
                missing_alt.append(img.get_attribute("src") or "No src attribute")
            elif alt.strip() == "":
                empty_alt.append(img.get_attribute("src") or "No src attribute")

        # Report results
        if missing_alt or empty_alt:
            comments = []
            if missing_alt:
                comments.append(f"Missing alt attribute for images: {', '.join(missing_alt)}")
            if empty_alt:
                comments.append(f"Empty alt attribute for images: {', '.join(empty_alt)}")
            
            write_to_excel_test_results(BASE_URL, "Image Alt Attribute Test", "Fail", "; ".join(comments))
            print('Test 3 failed.')
        else:
            write_to_excel_test_results(BASE_URL, "Image Alt Attribute Test", "Pass", "All images have valid alt attributes")
            print('Test 3 passed.')

    except Exception as e:
        write_to_excel_test_results(BASE_URL, "Image Alt Attribute Test", "Fail", f"Error: {e}")
        print('Test 3 failed.')

    finally:
        driver.quit()
        print('Test 3 closed.')

if __name__ == "__main__":
    test_image_alt()
