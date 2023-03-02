import requests
from bs4 import BeautifulSoup

url = "https://edition.cnn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
headlines = soup.find_all('div', class_="Cell-i0zvfi-0 sc-hzNEM hDUaXo")
for headline in headlines:
    stories = headline.find_all('li', class_="sc-kAzzGY ciMjLG")
    for story in stories:
        news = story.find_all('li', class_="sc-fjdhpX sc-chPdSV cfnoGA")
        for new in news:
            topics = new.find('span', class_="cd__headline-text")
            if topics:
                print(topics.text)



