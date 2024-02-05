from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://codepen.io/BoringCode/pen/nYbrep")
    src_loc = page.frame_locator("iframe[name=\"CodePen\"]").get_by_role("button", name="Send >>")
    tgt_loc = page.frame_locator("iframe[name=\"CodePen\"]").get_by_text("Slide to Send")
    src_loc.click()
    src_loc.drag_to(tgt_loc)

