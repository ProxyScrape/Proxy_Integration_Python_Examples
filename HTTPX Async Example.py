import httpx
import asyncio

async def async_request_with_proxy():
    proxies = {
        "http://": "@rp.proxyscrape.com:6060",
        "https://": "@rp.proxyscrape.com:6060"
    }

    async with httpx.AsyncClient(proxies=proxies) as client:
        # Make 5 concurrent requests
        tasks = [client.get('http://httpbin.org/ip') for _ in range(5)]
        responses = await asyncio.gather(*tasks)

        for i, response in enumerate(responses):
            print("Status Code:", response.status_code)
            print("Response:", response.json())
            print("-" * 20)

if __name__ == '__main__':
    asyncio.run(async_request_with_proxy())
