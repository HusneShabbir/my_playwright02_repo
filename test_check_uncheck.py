from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.get_by_role("checkbox").first.check()
    page.wait_for_timeout(1000)
    assert page.get_by_role("checkbox").first.is_checked()
    page.get_by_role("checkbox").nth(1).uncheck()
    page.wait_for_timeout(1000)
    assert not page.get_by_role("checkbox").nth(1).is_checked()
