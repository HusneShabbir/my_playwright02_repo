from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.vvitguntur.com/")
    page.get_by_text("Two Wheelers").hover()
    vehicle_type = page.get_by_role("link", name="Petrol Vehicles").inner_text()
    print(vehicle_type)
    page.get_by_role("link", name="Petrol Vehicles").click()
    visible_heading = page.get_by_role("heading", name="Petrol Vehicles").inner_text()
    expected_text = "Petrol Vehicles"
    assert visible_heading == expected_text


def test_dynamic_drop_downs(page: Page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_placeholder("First Name").type("Husne Shabbir")
    page.get_by_placeholder("Last Name").fill("Shaik")
    page.get_by_placeholder("name@example.com").fill("shabbir447@gmail.com")
    page.get_by_text("Male", exact=True).check()
    page.get_by_placeholder("Mobile Number").type("9492981739")
    page.locator('#dateOfBirthInput').click()
    page.get_by_label("Choose Monday, January 1st,").click()

    auto_suggestion = page.locator(".subjects-auto-complete__value-container")
    index = 0
    while index <= auto_suggestion.count():
        if auto_suggestion.nth(index).inner_text() == "English":
            auto_suggestion.nth(index).click()
        index += 1

    # page.locator('.subjects-auto-complete__value-container').fill("Maths")
    # page.get_by_text("Maths", exact=True).click()

    # subject_field(page,"Maths")

    # page.locator(".subjects-auto-complete__value-container").click()
    # page.locator('.subjects-auto-complete__value-container').fill("Chemistry")
    # subject_field(page,"Chemistry")
    # page.locator(".subjects-auto-complete__value-container").click()
    # page.locator('.subjects-auto-complete__value-container').fill("Physics")
    # subject_field(page, "Physics")
#     hobbies(page,"Sports")
#     hobbies(page,"Reading")
#     page.get_by_placeholder("Current Address").fill("65/20/1816,\nMagdum Nagar 4th lane,\nGuntur\nAP\npin:522001")
#
# # def subject_field(page,subject):
# #     return page.get_by_text(subject, exact=True).click()
#
#
# def hobbies(page,hobieees):
#     return page.get_by_text(hobieees).check()
