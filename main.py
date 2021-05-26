import aiohttp
import asyncio
from bs4 import BeautifulSoup

class WebScraper(object):
    def __init__(self, urls):
        self.urls = urls
        # Global Place To Store The Data:
        self.all_data  = []
        self.master_dict = {}
        # Run The Scraper:
        asyncio.run(self.main())
        

    async def fetch(self, session, url):
        try:
            async with session.get(url) as response:
                # 1. Extracting the Text:
                text = await response.text()
                # 2. Extracting the <title> </title> Tag:
                title_tag = await self.extract_title_tag(text)
                return text, url, title_tag
        except Exception as e:
            print(str(e))
            
    async def extract_title_tag(self, text):
        try:
            soup = BeautifulSoup(text, 'html.parser')
            return soup.title
        except Exception as e:
            print(str(e))

    async def main(self):
        tasks = []
        headers = {
            "user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        async with aiohttp.ClientSession(headers=headers) as session:
            for url in self.urls:
                tasks.append(self.fetch(session, url))

            htmls = await asyncio.gather(*tasks)
            self.all_data.extend(htmls)

            # Storing the raw HTML data.
            for html in htmls:
                if html is not None:
                    url = html[1]
                    self.master_dict[url] = {'Raw Html': html[0], 'Title': html[2]}
                else:
                    continue

# scraper = WebScraper(urls = ["http://forcecom.kz","https://anim-shop.ru"])
# scraper.master_dict['https://understandingdata.com/']['Title']
# # 3. Notice how we have a list length of 2:
# len(scraper.all_data)

async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        return await res.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, 'http://datascience.com')
        print(html[: 1000]) # first 1000 characters

loop = asyncio.get_event_loop()
loop.run_until_complete(main())