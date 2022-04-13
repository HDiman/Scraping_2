import requests
from bs4 import BeautifulSoup

# url = "https://health-diet.ru/table_calorie/"
url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
      "accept": "*/*",
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
}
req = requests.get(url, headers=headers)
src = req.text
# print(src)

with open("index.html", "w") as file:
    file.write(src)




# soup = BeautifulSoup(url, 'html.parser')

