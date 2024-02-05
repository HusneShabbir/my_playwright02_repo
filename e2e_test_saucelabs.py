capability = {
    'browserVersion': 'latest',

    'browserName': 'Chrome',  # Browsers allowed: "Chrome`, `MicrosoftEdge`, `pw-chromium", "pw-firefox am
    "LT:Options": {
        'platform': 'Windows 10',
        'build': 'Playwright Demo Build',
        'name': 'Playwright Test For Windows 10',
        "username": "shabbirhusne447",
        "accessKey": "ZxM4deURbRUFkWatZ2CRum2t8CSVJ4PgwDWsI2ChY1FnxboO3B",
        'network': True,
        'video': True,
        'visual': True,
        'console': True,
        'tunnel': False,

    }
}
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    login_id = ["standard_user", "problem_user", "performance_glitch_user"]
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
        page.locator("div:nth-child(6) > .pricebar > .btn_primary").click()
        page.get_by_role("button", name="REMOVE").is_visible(timeout=5000)
        page.get_by_role("link", name="1").click()
        page.get_by_role("link", name="Continue Shopping").click()
        page.get_by_role("button", name="ADD TO CART").nth(1).click()
        page.get_by_role("link", name="2").click()
        page.get_by_role("link", name="CHECKOUT").click()
        page.locator("[data-test=\"firstName\"]").fill("shabbir")
        page.locator("[data-test=\"lastName\"]").fill("Shaik")
        page.locator("[data-test=\"postalCode\"]").fill("522001")
        page.get_by_role("button", name="CONTINUE").click()
        if page.get_by_text("Checkout: Overview").is_visible():
            print("checkout Sucessfull")
        else:
            print("checkout Failed")
        page.get_by_role("link", name="FINISH").click()
        page.get_by_text("Finish").is_visible()
        expect(page.get_by_role("heading", name="THANK YOU FOR YOUR ORDER")).to_be_visible()
        page.get_by_role("button", name="Open Menu").click()
        page.get_by_role("link", name="Logout").click()
        if page.get_by_role("button", name="LOGIN").is_visible():
            print("Logged successfully")
        else:
            print("Failed to logout")


with sync_playwright() as playwright:
    run(playwright)
