import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"),
                                               pytest.param("locked_out_user", "secret_sauce",marks=pytest.mark.xfail()),
                                               ("problem_user", "secret_sauce"),
                                               ("performance_glitch_user", "secret_sauce")])
def test_example(page, username, password) -> None:
    page.goto("https://www.saucedemo.com/v1/")
    usr_filed = page.locator("[data-test=\"username\"]")
    usr_filed.fill(username)
    pass_field = page.locator("[data-test=\"password\"]")
    pass_field.fill(password)
    login_btn = page.get_by_role("button", name="LOGIN")
    login_btn.click()
    prod_ele = page.get_by_text("Products")
    expect(prod_ele).to_be_visible()
