import urllib
import urllib.request
import ssl
ssl._create_default_https_context =ssl._create_unverified_context
url = 'https://www.12306.cn/mormhweb/'
response = urllib.request.urlopen(url=url)
print(response.read().decode('utf-8'))
