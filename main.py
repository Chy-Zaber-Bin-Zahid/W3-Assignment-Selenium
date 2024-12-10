import tests.test_h1_tag as h1_test
import tests.test_html_sequence as h1_h6_test
import tests.test_image_alt as image_test
import tests.test_url_status as url_test
import tests.test_currency_filter as filter_test
import tests.test_scrape_data as scrape_test


if __name__ == "__main__":
    h1_test.test_h1_tag()
    h1_h6_test.test_html_sequence()
    image_test.test_image_alt()
    url_test.test_url_status()
    filter_test.test_currency_filter()
    scrape_test.test_scrape_data()