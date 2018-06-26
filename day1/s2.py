import urllib
import urllib.request
url= 'https://www.baidu.com/'
heads = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
           'Connection':'keep-alive',
           'Accept-Language':'zh-CN,zh;q=0.9'


 }
requset = urllib.request.Request(url=url,headers=heads)
response=urllib.request.urlopen(requset)
print(response.read().decode('utf'))