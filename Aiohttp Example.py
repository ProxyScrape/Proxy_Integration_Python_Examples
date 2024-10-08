import asyncio
import aiohttp

# Variable to adjust the number of requests at the same time
num_requests = 5


async def fetch(session, url, proxy):
    async with session.get(url, proxy=proxy) as response:
        # print(response.status)
        print(await response.json())


async def main():
    url = "http://httpbin.org/ip"
    proxy = "http://apvx45n24g1q810:32cp09nenvb27c2@rp.proxyscrape.com:6060"

    async with aiohttp.ClientSession() as session:
        # Create a list of tasks
        tasks = [fetch(session, url, proxy) for _ in range(num_requests)]
        # Run all tasks concurrently
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
