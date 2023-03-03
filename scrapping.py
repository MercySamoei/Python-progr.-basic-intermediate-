import requests
from bs4 import BeautifulSoup

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

print("Which skill are you not familiar with?")
unfamiliar_skill = input('>')
print(f'Filtering out, {unfamiliar_skill}')

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    published_date = job.find('span', class_="sim-posted").span.text
    
    if "few" in published_date:
        company_name = job.find('h3',class_="joblist-comp-name").text
        skills = job.find('span', class_="srp-skills").text
        #description = job.find('div', class_="job-description fs12")
        if unfamiliar_skill not in skills:
            print(f"Company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            #print(f'More Info: {description.strip()}')
            print()
