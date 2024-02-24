import json
import os
import urllib
import subprocess

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

capabilities = {
    'browserName': 'pw-webkit',
    # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': 'macOS Sonoma',
        'build': 'Playwright_Certification_101',
        'name': 'scenario3 with macOS Sonoma',
        'user': 'shabbirhusne447',
        'accessKey': 'ZxM4deURbRUFkWatZ2CRum2t8CSVJ4PgwDWsI2ChY1FnxboO3B',
        'network': True,
        'video': True,
        'visual': True,
        'console': True,
        'tunnel': False,  # Add tunnel configuration if testing locally hosted webpage
        'tunnelName': '',  # Optional
        'geoLocation': '',  # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
    }
}


def test_scenario3_run():
    with sync_playwright() as playwright:
        playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion

        lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(
            json.dumps(capabilities))
        browser = playwright.chromium.connect(lt_cdp_url, timeout=120000)
        page = browser.new_page()
        try:
            page.goto("https://www.lambdatest.com/selenium-playground/")
            page.get_by_role("link", name="Input Form Submit").click()
            submit_button = page.get_by_role("button", name="Submit")
            submit_button.click()
            page.get_by_placeholder("Name", exact=True).fill("shabbir")
            page.get_by_placeholder("Email", exact=True).fill("shabbirhusne447@gmail.com")
            page.get_by_placeholder("Password").fill("password")
            page.get_by_placeholder("Company").fill("cognizant")
            page.get_by_placeholder("Website").fill("lamdatest")
            page.get_by_role("combobox").click()
            page.get_by_role("combobox").select_option(value="US")
            page.get_by_placeholder("City").fill("Newyork")
            page.get_by_placeholder("Address 1").fill("Unkown address1")
            page.get_by_placeholder("Address 2").fill("Unkown address2")
            page.get_by_placeholder("State").fill("hawaii")
            page.get_by_placeholder("Zip code").fill("007")
            submit_button.click()
            if page.get_by_text("Thanks for contacting us, we").is_visible(timeout=1000):
                set_test_status(page, "passed", "Message matched")
            else:
                set_test_status(page, "failed", "Message did not match")
        except Exception as err:
            print("Error:: ", err)
            set_test_status(page, "failed", str(err))

        browser.close()


def set_test_status(page, status, remark):
    page.evaluate("_ => {}",
                  "lambdatest_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")
