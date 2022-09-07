from bs4 import BeautifulSoup
import requests

halfurl1 = 'https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text='
halfurl2 = '&op=translate'

text = input('enter text to translte: ')
text = text.replace(' ', '%20')
url = halfurl1 + text + halfurl2
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
result = soup.find_all("span", class_="Q4iAWc")
print(result)
