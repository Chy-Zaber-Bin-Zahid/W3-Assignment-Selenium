from selenium import webdriver
from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from utils.excel_handler import write_to_excel  # Updated to use the Excel handler

def test_html_sequence():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    try:
        # Find all heading tags (H1-H6)
        headings = driver.find_elements(By.XPATH, "//h1|//h2|//h3|//h4|//h5|//h6")
        
        if not headings:
            write_to_excel(BASE_URL, "HTML Tag Sequence Test", "fail", "No headings found")
            return

        # Extract tag names and positions
        heading_tags = [int(heading.tag_name[1]) for heading in headings]

        # Check for gaps in sequence (e.g., missing levels)
        for i in range(1, 7):
            if i in heading_tags:
                # Ensure proper sequence
                previous_tags = [x for x in heading_tags if x < i]
                if previous_tags and heading_tags.index(i) < heading_tags.index(min(previous_tags)):
                    write_to_excel(BASE_URL, "HTML Tag Sequence Test", "fail", f"Heading sequence broken at H{i}")
                    return

        # If all checks pass
        write_to_excel(BASE_URL, "HTML Tag Sequence Test", "pass", "Heading sequence is valid")

    except Exception as e:
        write_to_excel(BASE_URL, "HTML Tag Sequence Test", "fail", f"Error: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_html_sequence()
