import json
import os
import urllib
import subprocess

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

capabilities = {
    'browserName': 'Chrome',
    # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': 'Windows 11',
        'build': 'scenario2_lamdatest',
        'name': 'Chrome_scenario2 with Windows 11',
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


def test_scenario2_run():
    with sync_playwright() as playwright:
        playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion

        lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(
            json.dumps(capabilities))
        browser = playwright.chromium.connect(lt_cdp_url, timeout=120000)
        page = browser.new_page()
        try:
            page.goto("https://www.lambdatest.com/selenium-playground/")
            page.get_by_role("link", name="Drag & Drop Sliders").click()
            slider = page.locator("//input[@value='15']")
            slider.click()
            page.locator("//output[@id='rangeSuccess']").inner_text()

            while True:
                if page.locator("//output[@id='rangeSuccess']").inner_text() == "95":
                    break
                slider.press('ArrowRight')

            if page.locator("//output[@id='rangeSuccess']").inner_text() == "95":
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
