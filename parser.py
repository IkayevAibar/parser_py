import requests
url = 'https://freetp.org/' # url для второй страницы
r = requests.get(url)
with open('test.html', 'wb') as output_file:
  output_file.write(r.text.encode('UTF-16'))

from bs4 import BeautifulSoup

results = []
# Beautiful Soup
soup = BeautifulSoup(r.text)
film_list = soup.find('div', {'id': 'dle-content'})
counter=0
items = film_list.find_all('div', {'class': 'base'})
for item in items:
  # print(item.find('div', {'class': 'heading'}).find('a').innerHTML )
  game = item.find('div', {'class': 'heading'}).find('a').get('href')
  game_name = item.find('div', {'class': 'heading'}).find('a').text
  desc = item.find('div', {'class': 'maincont bnews'}).find('p').text
  category = item.find('p', {'class': 'lcol argcat'}).text
  counter+=1
  results.append({
      'id': counter,
      'game_name':game_name,
      'game_link': game,
      'desc': desc,
      'category': category,
  })


# print(film_list)
# print(results)
for item in results:
  print(item,'\n')