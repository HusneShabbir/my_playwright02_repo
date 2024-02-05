from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://jqueryui.com/tooltip/")
    loc = page.frame_locator("iframe").get_by_label("Your age:")
    loc.hover()
    page.wait_for_timeout(10000)


def test_horizontal_slider(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")
    pt = page.get_by_role("slider")
    pt.click()
    msg = page.locator("#range").inner_text()
    while True:
        if msg == '4.5':
            break
        pt.press('ArrowRight')

    print(msg)
