from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    login_id = ["standard_user","problem_user","performance_glitch_user","locked_out_user"]
    Password = "secret_sauce"
    for i in login_id:
        print(i)
        page.goto("https://www.saucedemo.com/v1/")
        page.locator("[data-test=\"username\"]").fill(i)
        page.locator("[data-test=\"password\"]").fill(Password)
        page.get_by_role("button", name="LOGIN").click()
        if page.get_by_text("Products").is_visible(timeout=5000):
            print("login sucessfull")
        else:
            print("login failed")
        page.get_by_role("button", name="Open Menu").click()
        page.get_by_role("link", name="Logout").click()
        if page.get_by_role("button", name="LOGIN").is_visible():
            print("logout sucessfull")
        else:
            print("logout failed")











with sync_playwright() as playwright:
    run(playwright)
