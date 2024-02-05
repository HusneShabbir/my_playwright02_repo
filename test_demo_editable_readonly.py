from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://jsfiddle.net/L96svw3c")
    read_only=page.frame_locator("iframe[name=\"result\"]").locator("#readOnly")
    editable= page.frame_locator("iframe[name=\"result\"]").locator("#readonly")

    expect(read_only).not_to_be_editable()
    expect(editable).to_be_editable()
    x = "shabbir"
    editable.fill("")
    editable.type(x)
    page.wait_for_timeout(1000)
    text = editable.inner_text()
    print(text)

