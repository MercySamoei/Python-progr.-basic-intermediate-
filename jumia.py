import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.jumia.co.ke/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
products = soup.find_all('div', class_="crs row _no-g -fw-nw _6cl-4cm -pvxs")

with open('Jumia.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(['Product Name', 'Price', 'Discount'])

    for index, product in enumerate(products):
        name_elements = product.find_all('div', class_="name")
        name_items = product.find_all('div', class_="prc")
        discounts = product.find_all('div', class_="bdg _dsct")
        for discount in discounts:
            product_name = name_elements[0].text.strip()
            price = name_items[0].text.strip()
            discount = discount.text.strip()
            write.writerow([product_name, price, discount])
        print(f'Product {index} saved to file')

print('All products saved to Jumia CSV file')


