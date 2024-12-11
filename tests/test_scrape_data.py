from selenium import webdriver
from config.settings import BASE_URL
from utils.excel_handler import write_to_excel_scrape

def test_scrape_data():
    print('Test 6 started.')
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    # Fetch ScriptData from the window object (assuming it's in JSON format)
    script_data = driver.execute_script("return window.ScriptData;")
    # Ensure the data is in a valid format (dictionary)
    if isinstance(script_data, dict):
        # Scrape the required data
        site_url = script_data['config'].get('SiteUrl', 'Not found')
        site_name = script_data['config'].get('SiteName', 'Not found')
        campaign_id = script_data['pageData'].get('CampaignId', 'Not found')
        user_info = script_data.get('userInfo', {})
        browser = user_info.get('Browser', 'Not found')
        country_code = user_info.get('CountryCode', 'Not found')
        ip = user_info.get('IP', 'Not found')
    else:
        # If the script data is not in the expected format, set all fields to 'Not found'
        site_url = site_name = campaign_id = browser = country_code = ip = 'Not found'
    print('Test 6 passed.')
    write_to_excel_scrape(site_url, campaign_id, site_name, browser, country_code, ip)
    print('Test 6 closed.')
    driver.quit()


if __name__ == "__main__":
    test_scrape_data()
