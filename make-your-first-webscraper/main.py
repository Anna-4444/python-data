import requests
from bs4 import BeautifulSoup

# Set headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
url = "https://en.wikipedia.org/wiki/Honey_badger#"
# Send the request with headers
response = requests.get(url, headers=headers)
# Raise if there is an error
response.raise_for_status()
# html = resonse.text.encode("utf-8") # This code in unnecessary - Beautiful Soup can handle raw text directly
soup = BeautifulSoup(response.text, 'html.parser')

h2_tags = soup.find_all("h2")
print(len(h2_tags))
for element in h2_tags:
    print(element)

link_tags = soup.find_all("a")
print(link_tags[:5])

image_tags = soup.find_all("img")
print(image_tags[-4:])