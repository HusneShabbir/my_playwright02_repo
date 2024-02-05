

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.spicejet.com/")
    page.get_by_test_id("to-testID-origin").locator("input[type=\"text\"]").click()
    # page.get_by_test_id("to-testID-origin").locator("input[type=\"text\"]").fill("ko")
    from_loc(page, "Hyderabad").click()
    # page.wait_for_timeout(2000)
    to_loc(page, "Ajmer").click()
    # page.wait_for_timeout(2000)
    departure_date(page, "undefined-month-January-2024", "29").click()
    # page.wait_for_timeout(2000)
    page.get_by_text("Return Date").click()
    return_date(page, "undefined-month-February-2024", "29").click()
    # page.wait_for_timeout(3000)
    page.get_by_test_id("home-page-travellers").get_by_text("Passengers").click()
    for j in range(3):
        no_of_passengers(page, "Adult-testID-plus-one-cta").click()

    page.wait_for_timeout(3000)
    page.get_by_test_id("home-page-travellers-done-cta").click()
    page.get_by_text("Currency").click()
    currency_type(page, "EUR").click()
    page.get_by_text("Family & Friends").check()
    page.get_by_test_id("home-page-flight-cta").click()
    page.get_by_role("img").locator("rect").check()
    #page.locator("div").filter(has_text=re.compile(r"^Continue$")).nth(1).click()


def from_loc(page, city):
    return page.get_by_text(city)


def to_loc(page, city):
    return page.get_by_text(city)


def departure_date(page, month, date):
    return page.get_by_test_id(month).get_by_text(date)


def return_date(page, month, date):
    return page.get_by_test_id(month).get_by_text(date)


def no_of_passengers(page, type):
    return page.get_by_test_id(type)


def currency_type(page, currency):
    return page.get_by_text(currency)

