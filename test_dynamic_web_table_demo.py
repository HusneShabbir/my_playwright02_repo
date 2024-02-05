from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.w3schools.com/html/html_tables.asp")
    text = page.get_by_role("cell", name="Centro comercial Moctezuma")
    print(text.inner_text())

    assert text.inner_text() == "Centro comercial Moctezuma"
    company_values(page)


def company_values(page):
    i = 0
    while i < 7:
        selector = "//*[@id='customers']/tbody/tr["+i+"]"
        print(page.locator(selector).inner_text())
        i += 1
