import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='ch',
        help='Please, choose a browser: ch, ff, ie'
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "ch":
        print("\nstart browser chrome for test...")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "ff":
        print("\nstart browser firefox for test...")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
    elif browser_name == "ie":
        print("\nstart browser ie for test...")
        browser = webdriver.Ie()
    else:
        print("Browser {} still is not implemented".format(browser_name))

    def final():
        print(f"\n close browser {browser_name}")
        browser.quit()

    request.addfinalizer(final)

    return browser
