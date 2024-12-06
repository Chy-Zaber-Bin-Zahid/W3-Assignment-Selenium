from selenium import webdriver
from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from utils.excel_handler import write_to_excel  # Utility to write results to Excel


def test_html_sequence():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    try:
        # Find all heading tags (H1-H6)
        headings = driver.find_elements(By.XPATH, "//h1|//h2|//h3|//h4|//h5|//h6")

        if not headings:
            write_to_excel(BASE_URL, "HTML Tag Sequence Test", "fail", "No headings found on the page.")
            return

        # Extract heading levels (1 for <h1>, 2 for <h2>, etc.)
        heading_levels = [int(heading.tag_name[1]) for heading in headings]

        # Ensure the sequence is not broken or missing levels
        required_levels = set(range(1, max(heading_levels) + 1))  # Expected levels up to the highest found
        actual_levels = set(heading_levels)

        # Check for missing levels
        missing_levels = required_levels - actual_levels
        if missing_levels:
            write_to_excel(
                BASE_URL,
                "HTML Tag Sequence Test",
                "fail",
                f"Missing heading levels: {', '.join(f'H{level}' for level in sorted(missing_levels))}"
            )
            return

        # Ensure headings appear in proper order (e.g., H2 should not come before H1)
        for i in range(1, len(heading_levels)):
            if heading_levels[i] < heading_levels[i - 1]:
                write_to_excel(
                    BASE_URL,
                    "HTML Tag Sequence Test",
                    "fail",
                    f"Improper sequence: H{heading_levels[i]} appears before H{heading_levels[i - 1]}"
                )
                return

        # If all checks pass
        write_to_excel(BASE_URL, "HTML Tag Sequence Test", "pass", "Heading sequence is valid.")

    except Exception as e:
        write_to_excel(BASE_URL, "HTML Tag Sequence Test", "fail", f"Error occurred: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_html_sequence()
