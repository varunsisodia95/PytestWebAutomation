import pytest
import json
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


@pytest.fixture(scope='session')
def config():
    with open('tests/config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture
def browser(config):
    if config['browser'] == 'chrome':
        driver = Chrome()
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')

    driver.implicitly_wait(config['wait_time'])
    yield driver
    driver.quit()


@pytest.mark.parametrize("phrase", ['panda', 'santa claus', 'Trump towers'])
def test_basic_duckduckgo_search(browser, phrase):
    """
    Navigate to the DuckDuckGo home page
    Enter some search phrases
    Verify that:
    1. Results appear on the results page
    2. The search phrase appears in the search bar
    3. At least one search result contains the search phrase
    """

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(phrase)

    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(phrase) > 0
    assert result_page.search_input_value() == phrase


@pytest.mark.parametrize("filter", ['Past day',
                                    'Past week',
                                    'Past month',
                                    'Past year'])
def test_find_top_news(browser, filter):
    """
    1. Navigate to the DuckDuckGo home page
    2. Enter some search phrase
    3. Verify the top search result in the past week, past year, past month.
    """
    phrase = "Bible"
    expected_headline = "Official King James Bible Online: Authorized King James Version (Kjv)"

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(phrase)

    result_page = DuckDuckGoResultPage(browser)
    assert result_page.setSearchFilter(filter) == expected_headline


