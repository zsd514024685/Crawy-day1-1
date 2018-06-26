import urllib
import urllib.request
import urllib.parse
url='https://www.baidu.com/s?word=%s/'
key = input('请输入查询的关键字：')
key = urllib.parse.quote(key)
print(key)
url = url%(key)
heads = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
           'Connection':'keep-alive',
           'Accept-Language':'zh-CN,zh;q=0.9'}
request=urllib.request.Request(url=url,headers=heads)
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
