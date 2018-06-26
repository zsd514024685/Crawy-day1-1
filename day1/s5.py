import requests
from bs4 import BeautifulSoup
import re
response = requests.get(
    url='http://www.autohome.com.cn/news/'
)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,features='html.parser')
taraget = soup.find('id="auto-index-form-illegal"')
print(taraget)
