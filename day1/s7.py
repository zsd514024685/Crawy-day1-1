import urllib
import urllib.request
import urllib.parse
url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action='
form = {'start':0,'limit':10}
data = urllib.parse.urlencode(form).encode('utf-8')
response = urllib.request.urlopen(url=url,data=data)
print(response.read().decode('utf-8'))