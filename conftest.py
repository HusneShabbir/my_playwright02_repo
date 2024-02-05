import pytest


@pytest.fixture()

def set_up(page):
    i = "standard_user"
    Password = "secret_sauce"
    page.goto("https://www.saucedemo.com/v1/")
    page.locator("[data-test=\"username\"]").fill(i)
    page.locator("[data-test=\"password\"]").fill(Password)
    page.get_by_role("button", name="LOGIN").click()
    if page.get_by_text("Products").is_visible(timeout=5000):
        print("login sucessfull")
    else:
        print("login failed")
    yield page
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
    if page.get_by_role("button", name="LOGIN").is_visible():
        print("logout sucessfull")
    else:
        print("logout failed")