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
