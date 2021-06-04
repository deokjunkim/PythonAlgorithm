import requests
from bs4 import BeautifulSoup

url = 'https://programmers.co.kr/learn/courses/30/lessons/42626/solution_groups?language=python3&page=1'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

else :
    print(response.status_code)