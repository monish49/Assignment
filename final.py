import asyncio
from aiohttp import ClientSession


async def word(url, n):

    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            my_HTML = response.decode("utf8")
            splitted = my_HTML.split()

    for word in splitted[0:n]:
        print(word+' ' + f' appears {splitted.count(word)} time(s)')


asyncio.run(word('http://norvig.com/big.txt', 10))
