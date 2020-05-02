import requests
import re
from bs4 import BeautifulSoup

url ="http://api.nature.go.kr/openapi/service/rest/PlantService/seedSearch?serviceKey=VJUmcPAhwvdMolFe%2FyqXyuhlXfxa4m0mUW%2BYKxhkz%2Buadx9F4hQ6RgfvxBA5c0h14gDZYblIp1sBjgUufsmCcA%3D%3D&3&numOfRows=10000"

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

name_list = soup.select('plantgnrlnm')

for idx, name in enumerate(name_list, 100):
    print(name.text)

