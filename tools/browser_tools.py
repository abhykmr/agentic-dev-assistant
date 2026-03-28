from playwright.sync_api import sync_playwright


def browse_website(url:str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page();
        page.goto(url)
        content  = page.title()
        browser.close()


    return f"Page title: {content}"