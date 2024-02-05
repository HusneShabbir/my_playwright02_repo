from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/shadowdom")
    # txt = page.locator("my-paragraph").filter(has_text="Let's have some different text! My default text").get_by_role("paragraph")
    nxt = page.locator("span")
    # inner_txt = txt.inner_text()
    outer_txt = nxt.inner_text()
    print(outer_txt)
    page.wait_for_timeout(2000)
    # print(inner_txt)

