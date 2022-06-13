from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://b2b.11467.com/search/1-2.htm
    page.goto("http://b2b.11467.com/search/1-2.htm")

    # Click text=下一页
    page.locator("text=下一页").click()
    # expect(page).to_have_url("http://b2b.11467.com/search/1-3.htm")

    # Click a:has-text("甘肃宾利达农牧发展有限公司")
    with page.expect_popup() as popup_info:
        page.locator("a:has-text(\"甘肃宾利达农牧发展有限公司\")").click()
    page1 = popup_info.value

    # Close page
    page1.close()

    # Click text=农、林、牧、渔业公司
    page.locator("text=农、林、牧、渔业公司").click()
    # expect(page).to_have_url("http://b2b.11467.com/search/1.htm")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
