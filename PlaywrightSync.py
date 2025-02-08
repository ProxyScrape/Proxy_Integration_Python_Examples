import time

from playwright.sync_api import sync_playwright

datacenter_proxy = {
                'server': 'http://156.228.86.29:3128',
            }
residential_proxy = {
                'server': 'http://rp.scrapegw.com:6060',
                'username': 'proxy_username',
                'password': 'proxy_password'
            }

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        proxy=residential_proxy,
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://httpbin.org/ip")
    time.sleep(3)

    print(page.content())

    browser.close()
