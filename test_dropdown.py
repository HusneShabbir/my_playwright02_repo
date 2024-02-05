from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option(index=2)
    page.set_default_timeout(2000)
    page.locator("#dropdown").select_option("")
    page.set_default_timeout(2000)
    page.locator("#dropdown").select_option(label="Option 1")
    page.set_default_timeout(2000)
    page.locator("#dropdown").select_option("")
    page.set_default_timeout(2000)
    page.locator("#dropdown").select_option(value="2")
    page.set_default_timeout(2000)