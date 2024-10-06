import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://httpbin.org/ip",
                               proxy="http://@rp.proxyscrape.com:6060") as response:
            print(response.status)
            print(await response.json())


if __name__ == '__main__':
    asyncio.run(main())