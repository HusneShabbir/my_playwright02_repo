from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://jqueryui.com/autocomplete/")
    page.frame_locator("iframe").get_by_label("Tags:").type("shabbir",delay=2000)



def test_site(page: Page) -> None:
    page.goto("https://www.rediff.com/")
    text= page.frame_locator("iframe[name=\"moneyiframe\"]").get_by_role("link", name="NSE").inner_text()
    print(text)
