
# Web UI testing using Pytest, Python, Selenium webdriver

The following project performs UI automation of the search engine DuckDuckGo.


## Tech Stack

**Language:** Python

**Framework:** Pytest framework

**Design pattern used:** Page Object Model (POM)

**Reporting mechanism:** HTML reports

## Test cases and Utilities

### Test cases

- Test cases for all projects are located under the <b> /TestCases </b> directory of the respective project.
1) [DuckDuckGo search engine automation](https://github.com/varunsisodia95/PytestWebAutomation/blob/master/tests/test_web.py)
2) [Basic Math operations](https://github.com/varunsisodia95/PytestWebAutomation/blob/master/tests/test_math.py)


## Running test cases
### Preconditions
Install following python packages 

```bash
Selenium
Pytest
Pytest-html
Pytest-xdist
```
Note: The requirements.txt file is attached in the project directory itself.

### Running tests
The test cases are located in the /tests directory. 
They can be executed using the following command:

```bash
python -m pytest --html=report.html -n 2 .\tests\
```


