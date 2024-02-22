import json
import os
import urllib
import subprocess

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

capabilities = {
    'browserName': 'pw-firefox',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': 'macOS Big Sur',
        'build': 'sample firefox with macOS Big Sur',
        'name': 'Firefox_Playwright Test with macOS',
        'user': 'shabbirhusne447',
        'accessKey': 'ZxM4deURbRUFkWatZ2CRum2t8CSVJ4PgwDWsI2ChY1FnxboO3B',
        'network': True,
        'video': True,
        'console': True,
        'tunnel': False,  # Add tunnel configuration if testing locally hosted webpage
        'tunnelName': '',  # Optional
        'geoLocation': '',  # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
    }
}


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"),
                                               pytest.param("locked_out_user", "secret_sauce",
                                                            marks=pytest.mark.xfail()),
                                               ("problem_user", "secret_sauce"),
                                               ("performance_glitch_user", "secret_sauce")])
def test_sample_run(username, password):
    with sync_playwright() as playwright:
        playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion

        lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(
            json.dumps(capabilities))
        browser = playwright.chromium.connect(lt_cdp_url, timeout=120000)
        page = browser.new_page()
        try:
            page.goto("https://www.saucedemo.com/v1/")
            # Generate lighthouse report for the required URL.
            # You can generate multiple lighthouse reports in a test by executing this function anywhere in the test.
            # generate_lighthouse_report(page, "https://duckduckgo.com")
            page.locator("[data-test=\"username\"]").fill(username)
            page.locator("[data-test=\"password\"]").fill(password)
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
                set_test_status(page, "passed", "Title matched")
            else:
                set_test_status(page, "failed", "Title did not match")
        except Exception as err:
            print("Error:: ", err)
            set_test_status(page, "failed", str(err))

        browser.close()


def set_test_status(page, status, remark):
    page.evaluate("_ => {}",
                  "lambdatest_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")
