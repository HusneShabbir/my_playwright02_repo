import re

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://codeseven.github.io/toastr/demo.html")
    toast_msg = page.get_by_role("button", name="Show Toast")
    toast_msg.click()
    msg = page.locator("div").filter(has_text=re.compile(r"^My name is Inigo Montoya\. You killed my father\. Prepare to die!$")).nth(1)
    expect(msg).to_be_visible()
    xyz = msg.inner_text()
    print(xyz)
    page.wait_for_timeout(5000)
    expect(msg).not_to_be_visible()
    expected_msg = "My name is Inigo Montoya. You killed my father. Prepare to die!"
    assert xyz == expected_msg

