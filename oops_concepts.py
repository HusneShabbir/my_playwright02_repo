from playwright.sync_api import Playwright, sync_playwright, expect
from Base_class_e2e import necessaries


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    necessaries1 =  necessaries(page)
    #page.goto("https://symonstorozhenko.wixsite.com/website-1")
    necessaries1.navigate()
    necessaries1.__init__(page)
    # page.get_by_text("Celebrating Beauty and Style").is_visible()
    # page.get_by_role("button", name="Shop Now").is_enabled()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
