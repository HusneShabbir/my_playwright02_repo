import pytest
from playwright.sync_api import Page, expect

#random added code

@pytest.mark.regression
def test_login_logout(set_up) -> None:
    page = set_up
    print("fixture is working fine")

@pytest.mark.regression
@pytest.mark.SIT
def test_Check_in(set_up) -> None:
    page = set_up
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
