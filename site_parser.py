import requests
# import asyncio
import grequests
from bs4 import BeautifulSoup
URL = 'https://anim-shop.ru'

def get_html(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup



def get_links(soup):
    body = soup.find('body')
    a_elems = body.find_all('a')
    a_list = [a_elem.get('href') for a_elem in a_elems if a_elem!=None and a_elem.get('href')!=None and a_elem.get('href')[0]=='/']
    return a_list

all_links =[]
urls = []
count = 0
last_url = URL
def parser(URL_,count,all_links,urls):
    print(URL_)
    try:
        last_url=URL_
        html = get_html(URL_)
        count+=1
        new_url =""
        links_ = get_links(html)
        for link in links_:
            if(len(links_)==0):
                break
            new_url = link
            new_link = URL + new_url
            if(new_link not in urls):
                all_links.append(new_url)
                urls.append(new_link)
                parser(new_link,count,all_links,urls)
            new_url = ""
    except:
        print("Не удалось "+URL_)
    return "Done"

# hrml = get_html(URL+"/")
# links_ = get_links(hrml)
# print(links_)
# reqs = (grequests.get(link) for link in links_)
# resp=grequests.imap(reqs, grequests.Pool(10))

# for r in resp:
#    soup = BeautifulSoup(r.text, 'lxml')
#    results =[a.get('href') for a in soup.find_all('a')]
#    all_links+=results
   

parser(URL+"/",count,all_links,urls)

print(all_links)
# print(get_html(URL))