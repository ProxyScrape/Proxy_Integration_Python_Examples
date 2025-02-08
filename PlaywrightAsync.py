import asyncio
import time

from playwright.async_api import async_playwright


async def run_browser(instance_number, playwright):
    datacenter_proxy = {
        'server': 'http://156.228.86.29:3128',
    }
    residential_proxy = {
        'server': 'http://rp.scrapegw.com:6060',
        'username': 'proxy_username',
        'password': 'proxy_password'
    }

    browser = await playwright.chromium.launch(proxy=residential_proxy, headless=False)

    context = await browser.new_context()

    page = await context.new_page()

    await page.goto("https://httpbin.org/ip")
    time.sleep(3)

    content = await page.content()
    print(f"Browser {instance_number} IP information: {content}")

    await browser.close()


async def main():
    async with async_playwright() as playwright:
        # Create tasks for each browser instance
        tasks = [run_browser(i, playwright) for i in range(1, 4)]
        await asyncio.gather(*tasks)


asyncio.run(main())
