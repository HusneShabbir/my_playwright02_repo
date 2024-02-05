from playwright.sync_api import Page, expect


def test_example_1(page: Page) -> None:
    page.goto("http://uitestingplayground.com/ajax")
    page.get_by_role("button", name="Button Triggering AJAX Request").click()
    expected_text = page.get_by_text("Data loaded with AJAX get").inner_text()
    assert expected_text == "Data loaded with AJAX get request."


def test_example_2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    web_ele = page.get_by_role("heading", name="Hello World!")
    web_ele.is_visible()
    text = web_ele.inner_text()
    print(text)
    assert text == "Hello World!"


def test_example_3(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.get_by_role("button", name="Start").click()
    ele = page.get_by_role("heading", name="Hello World!")
    ele.is_visible()
    text_02=ele.inner_text()
    print(text_02)
    assert text_02=="Hello World!"