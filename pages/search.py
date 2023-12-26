from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Uniquely and clearly identifies the page
class DuckDuckGoSearchPage:

    URL = 'https://www.duckduckgo.com'

    searchBarXpath = f"//input[@id='searchbox_input']"
    SEARCH_INPUT = (By.XPATH, searchBarXpath)

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        # The * operator expands self.SEARCH_INPUT into positional arguments for the method call
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)