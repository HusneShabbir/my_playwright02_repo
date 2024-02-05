from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")
    check_box = page.get_by_role("checkbox")
    loading = page.locator("#loading").get_by_role("img")
    expect(loading).not_to_be_visible()
    check_box.click()
    page.get_by_role("button", name="Remove").click()
    expect(loading).to_be_visible()
    output_txt = page.get_by_text("It's gone!").inner_text()
    print(output_txt)
    assert output_txt == "It's gone!"
    add_btn = page.get_by_role("button", name="Add")
    add_btn.click()
    pre_loading = page.locator("#checkbox-example").get_by_role("img")
    expect(pre_loading).to_be_visible()
    back_ele = page.get_by_text("It's back!")
    expect(back_ele).to_be_visible()
    page.locator("#checkbox").check()


def test_right_click(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/context_menu")
    loc = page.locator("#hot-spot")
    loc.click(button="right")


def test_double_click(page: Page) -> None:
    page.goto("https://clickspeedtest.net/double-click-test.php")
    loc = page.get_by_role("button", name="Score Double Click/s")
    print(loc.inner_text())
    i = 0
    while i < 3:
        page.get_by_role("button", name="Click Here").dblclick()
        i = i + 1
    print(loc.inner_text())

