import requests
from bs4 import BeautifulSoup

# url = "https://health-diet.ru/table_calorie/"
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# headers = {
#       "accept": "*/*",
#       "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
# }
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
# with open("index.html", "w") as file:
#     file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, 'html.parser')
# print(soup)

all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")

for item in all_products_hrefs:
    item_text = item.text
    item_href = item.get("href")
    print(f"{item_text}:{item_href}")
