from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page.get_by_role("combobox").select_option(index=9)
    #page.wait_for_timeout(3000)
    page.get_by_role("combobox").select_option(value="AF")
    #page.wait_for_timeout(3000)
    page.get_by_role("combobox").select_option(label="India")
    page.wait_for_timeout(3000)
    page.get_by_role("listbox").select_option(index=1,label="March")
    #page.wait_for_timeout(3000)

def test_list_of_webelements(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    all_list_down_opts = page.get_by_role("combobox")
    print(all_list_down_opts.all_inner_texts())
    print(all_list_down_opts.count())
