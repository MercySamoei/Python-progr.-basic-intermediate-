import requests
from bs4 import BeautifulSoup


#Scraping Notion teaser headlines example
url = 'https://nation.africa/kenya'
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
h3 = soup.find_all('h3')
# print(h3)
for titles in h3:
    print(titles.text)

##yOUR CODE HERE    
# url = "https://edition.cnn.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# headlines = soup.find_all('div', class_="Cell-i0zvfi-0 sc-hzNEM hDUaXo")
# for headline in headlines:
#     stories = headline.find_all('li', class_="sc-kAzzGY ciMjLG")
#     for story in stories:
#         news = story.find_all('li', class_="sc-fjdhpX sc-chPdSV cfnoGA")
#         for new in news:
#             topics = new.find('span', class_="cd__headline-text")
#             if topics:
#                 print(topics.text)

