from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    src = page.locator("#column-a")
    tgt = page.locator("#column-b")
    src.drag_to(tgt)
    expect(tgt).to_have_text("A")
    expect(src).to_have_text("B")


#
# def drag_and_drop(page, n):
#     # src = page.locator("#column-a")
#     # tgt = page.locator("#column-b")
#     i = 0
#     while i < n:
#         page.drag_and_drop("#column-a", "#column-b")
#         i = i + 1
#
#
# def expect_trail(page, n):
#     src = page.get_by_test_id("column-a")
#     tgt = page.get_by_test_id("column-b")
#     if n % 2 == 0:
#         expect(tgt).to_have_text("B")
#         expect(src).to_have_text("A")
#     else:
#         expect(tgt).to_have_text("A")
#         expect(src).to_have_text("B")
