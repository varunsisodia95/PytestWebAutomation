from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
"""
Note that the interaction methods do not make assertions. 
They simply return state. Assertions are a concern for a test case, not page objects.
"""


class DuckDuckGoResultPage:
    noOfLinksXpath = f"//ol[@class='react-results--main']/child::li"
    LINK_DIVS = (By.XPATH, noOfLinksXpath)
    SEARCH_INPUT = (By.ID, 'search_form_input')

    filter_btn_xpath = f"//div[contains(@class, 'dropdown  dropdown--date')]/child::a"
    FILTER_BTN = (By.XPATH, filter_btn_xpath)

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//ol[@class='react-results--main']/child::li//*[contains(text(), '{phrase}')]"
        return By.XPATH, xpath

    @classmethod
    def FILTER_RESULTS(cls, filterToBeSet):
        duration_filter_xpath = f"//ol[@class='modal__list']/child::li/a[contains(text(), '{filterToBeSet}')]"
        return By.XPATH, duration_filter_xpath

    def __init__(self, browser):
        self.browser = browser

    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def phrase_result_count(self, phrase):
        # The * operator expands the self.PHRASE_RESULTS into positional arguments
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)

    def search_input_value(self):
        # The * operator expands the sself.SEARCH_INPUT into positional arguments
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    def get_headline_element(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*/li[@data-layout='organic']/article[@id='r1-0']/child::div["
                                            "2]/h2/descendant::span"))
        )
        return element

    def getTopHeadline(self):
        captured_string = self.get_headline_element().get_attribute("innerHTML")
        print(captured_string)
        return captured_string

    def setSearchFilter(self, filter_to_set):
        filter_btn = self.browser.find_element(*self.FILTER_BTN)
        filter_btn.click()

        filtered_results = self.browser.find_element(*self.FILTER_RESULTS(filter_to_set))
        filtered_results.click()

        time.sleep(2)
        current_headline = self.getTopHeadline()

        return current_headline
