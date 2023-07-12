import requests
from bs4 import BeautifulSoup

url = 'https://ko.wikipedia.org/wiki/컴퓨터'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

title = soup.select_one('#firstHeading').text
paragraph = soup.select('.mw-parser-output p')

print("제목: ", title)

print("내용 ----------")
for p in paragraph:
    print(p.text)