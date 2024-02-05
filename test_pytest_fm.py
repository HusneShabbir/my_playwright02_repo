import pytest
from playwright.sync_api import Page, expect, sync_playwright
import re
from playwright.sync_api import sync_playwright, Page, expect
import os
import subprocess
import urllib
import json
from dotenv import load_dotenv

capabilities = {
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


def test_playwright_for_multiple_browsers():
    with sync_playwright() as playwright:
        playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion
        lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse().quote(json.dumps(capabilities))
        browser = playwright.chromium.connect(lt_cdp_url)
        page = browser.new_page()
        try:
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
        finally:
            browser.close()

# i = "standard_user"
# Password = "secret_sauce"
# @pytest.mark.regression
# @pytest.mark.xfail(reason="Credentials expired")
# def test_login(page: Page) -> None:
#     login_id = ["standard_user","locked_out_user", "problem_user", "performance_glitch_user" ]
#     for j in login_id:
#         print(j)
#         page.goto("https://www.saucedemo.com/v1/")
#         page.locator("[data-test=\"username\"]").fill(j)
#         page.locator("[data-test=\"password\"]").fill(Password)
#         page.get_by_role("button", name="LOGIN").click()
#         if page.get_by_text("Products").is_visible(timeout=5000):
#             print("login sucessfull")
#         else:
#             print("login failed")
# @pytest.mark.regression
# def test_logot(page: Page) -> None:
#     print("2")
#     page.goto("https://www.saucedemo.com/v1/")
#     page.locator("[data-test=\"username\"]").fill(i)
#     page.locator("[data-test=\"password\"]").fill(Password)
#     page.get_by_role("button", name="LOGIN").click()
#     if page.get_by_text("Products").is_visible(timeout=5000):
#         print("login sucessfull")
#     else:
#         print("login failed")
#     page.get_by_role("button", name="Open Menu").click()
#     page.get_by_role("link", name="Logout").click()
#     if page.get_by_role("button", name="LOGIN").is_visible():
#         print("logout sucessfull")
#     else:
#         print("logout failed")
# @pytest.mark.SIT
# def test_Check_in(page: Page) -> None:
#     print("3")
#     page.goto("https://www.saucedemo.com/v1/")
#     page.locator("[data-test=\"username\"]").fill(i)
#     page.locator("[data-test=\"password\"]").fill(Password)
#     page.get_by_role("button", name="LOGIN").click()
#     if page.get_by_text("Products").is_visible(timeout=5000):
#         print("login sucessfull")
#     else:
#         print("login failed")
#     page.locator("div:nth-child(6) > .pricebar > .btn_primary").click()
#     page.get_by_role("button", name="REMOVE").is_visible(timeout=5000)
#     page.get_by_role("link", name="1").click()
#     page.get_by_role("link", name="Continue Shopping").click()
#     page.get_by_role("button", name="ADD TO CART").nth(1).click()
#     page.get_by_role("link", name="2").click()
#     page.get_by_role("link", name="CHECKOUT").click()
#     page.locator("[data-test=\"firstName\"]").fill("shabbir")
#     page.locator("[data-test=\"lastName\"]").fill("Shaik")
#     page.locator("[data-test=\"postalCode\"]").fill("522001")
#     page.get_by_role("button", name="CONTINUE").click()
#     page.screenshot(path="Artifacts_Draft/screenshot.png", full_page=True)
#     if page.get_by_text("Checkout: Overview").is_visible():
#         print("checkout Sucessfull")
#     else:
#         print("checkout Failed")
#     page.get_by_role("link", name="FINISH").click()
#     page.get_by_text("Finish").is_visible()
#     expect(page.get_by_role("heading", name="THANK YOU FOR YOUR ORDER")).to_be_visible()
#     page.get_by_role("button", name="Open Menu").click()
#     page.get_by_role("link", name="Logout").click()
#     if page.get_by_role("button", name="LOGIN").is_visible():
#         print("Logged successfully")
#     else:
#         print("Failed to logout")
