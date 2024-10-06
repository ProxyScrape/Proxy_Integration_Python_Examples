import httpx
import asyncio

async def async_request_with_proxy():
    proxies = {
        "http://": "http://@rp.proxyscrape.com:6060",
        "https://": "http://@rp.proxyscrape.com:6060"
    }

    async with httpx.AsyncClient(proxies=proxies) as client:
        response = await client.get('http://httpbin.org/ip')

        print("Status Code:", response.status_code)
        print("Response:", response.json())

if __name__ == '__main__':
    asyncio.run(async_request_with_proxy())
