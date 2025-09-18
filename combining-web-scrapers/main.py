import requests
from bs4 import BeautifulSoup

def get_soup(url):
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
  }
  r = requests.get(url, headers=headers)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
  soup = get_soup(url)
  data = {}
  categories = soup.find_all("dl")
  for category in categories:
    category_name = category.find("dt").get_text()
    category_animals = category.find_all("a")
    data[category_name] = category_animals
  return data

def get_animal(url):
  soup = get_soup(url)
  table = soup.find("table", {"class": "infobox biota"})
  if not table:
    return "No class found."
  rows = table.find_all("tr")
  for row in rows:
    if "Class:" in row.get_text():
      animal_class = row.find("a").contents[0]
      return animal_class


category_data = get_categories("https://skillcrush.github.io/web-scraping-endangered-species/")

# print(category_data)

collected_data = []

# animal_class = get_animal("https://en.wikipedia.org/wiki/Honey_badger")

# print(animal_class)

for category in category_data:
  for animal in category_data[category]:
    animal_href = animal["href"]
    animal_name = animal.contents[0]
    animal_class = get_animal(animal_href)
    data = {
      "Category": category,
      "Name": animal_name,
      "Class": animal_class
    }
    collected_data.append(data)

print(collected_data)