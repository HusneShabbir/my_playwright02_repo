from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    expectation_text = "The email address or mobile number you entered isn't connected to an account. Find your account and log in."
    page.goto("https://www.facebook.com/login.php/")
    page.get_by_placeholder("Email address or phone number").is_visible()
    page.get_by_placeholder("Email address or phone number").fill("saniamirza@gampoorekharza.com")
    page.get_by_placeholder("Password").is_visible()
    page.get_by_placeholder("Password").fill("pasword@secret")
    page.get_by_role("button", name="Log in").is_visible()
    page.get_by_role("button", name="Log in").click()
    error_msg = page.get_by_text("The email address or mobile").inner_text()
    assert error_msg == expectation_text


