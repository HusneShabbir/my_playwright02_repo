import pytest_check as xyz
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://jqueryui.com/autocomplete/")
    page.frame_locator("iframe").get_by_label("Tags:").type("shabbir",delay=2000)
    src_loc = page.frame_locator("iframe").get_by_label("Tags:")
    src_loc.fill("shabbir")
    xyz.equal(src_loc.inner_text(),"shabbir")
    src_loc.fill("")
    src_loc = page.frame_locator("iframe").get_by_label("Tags:")
    src_loc.type("Tanveer")
    xyz.equal(src_loc.inner_text,"Tanveer")


