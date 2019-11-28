def test_example(browser):
    browser.get("https://www.google.ru/")
    assert "Google" in browser.title
