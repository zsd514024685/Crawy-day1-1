import urllib
import urllib.request
url = 'http://www.qq.com/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           'Connection':'keep-alive',
           'Accept-Language':'zh-CN,zh;q=0.9',
           'Accept-Encoding':''}
request = urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
print(response.read().decode('gbk'))