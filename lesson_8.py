import asyncio
import aiohttp
import requests as r1

from bs4 import BeautifulSoup


def get_categories(url):
    page = r1.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    categories = []
    for category in soup.find_all('a', {"class": 'nav-link'}):
        categories.append(url + category.get('href'))
    return categories


my_url = 'http://127.0.0.1:8000'


async def main(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await response.text()
            # soup = BeautifulSoup(html, "html.parser")
            # soup.get()
            # async with aiofiles.open(url, mode='w') as f:
            #     await f.write(html)
            with open(url[:4] + url[-1], 'w') as f:
                f.write(html)

async def asynchronous():
    tasks = [asyncio.ensure_future(
        main(url)) for url in get_categories(my_url)]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(asynchronous())
loop.close()
