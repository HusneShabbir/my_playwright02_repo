from playwright.sync_api import Page, expect






def test_example(page: Page) -> None:
    page.goto("https://www.google.com/?gws_rd=ssl")
    print(page.url)
    google_link = page.url
    page.get_by_label("Gmail (opens a new tab)").click()
    print(page.url)
    gmail_link = page.url
    page.go_back()
    print(page.url)

    if page.url == google_link:
        print("Back function working fine")
    else:
        print("Back function not working")
    page.go_forward()
    print(page.url)
    if page.url == gmail_link:
        print("fwd function working fine")
    else:
        print("fwd function not working")

    page.get_by_role("link", name="Sign in").click()
    page.get_by_label("Email or phone").fill("12345@gmail.com")
    page.get_by_label("Email or phone").fill("")
    page.get_by_label("Email or phone").type("67890@gmail.com")
    page.get_by_label("Email or phone").press("Control+A")
    page.get_by_label("Email or phone").press("Backspace")
    page.get_by_label("Email or phone").type("shabbirhusne447@gmail.com", delay=1000)







    # ---------------------
