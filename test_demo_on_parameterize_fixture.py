import pytest
from playwright.sync_api import Page, expect


Password = "secret_sauce"
#["standard_user","locked_out_user", "problem_user", "performance_glitch_user" ]


@pytest.mark.parametrize("username","password",[("standard_user","secret_sauce"),
                                                pytest.param("locked_out_user","secret_sauce",marks=pytest.mark.xfail),("performance_glitch_user","secret_sauce"),("problem_user","secret_sauce")])
def test_login_with_multiple_users(page: Page,username,password) -> None:

        page.goto("https://www.saucedemo.com/v1/")
        page.locator("[data-test=\"username\"]").fill(username)
        page.locator("[data-test=\"password\"]").fill(password)
        page.get_by_role("button", name="LOGIN").click()
        if page.get_by_text("Products").is_visible(timeout=5000):
            print("login sucessfull")
        else:
            print("login failed")