import urllib
import urllib.request
url = 'https://www.bilibili.com/video/av21663728/?p=742'
urllib.request.urlretrieve(url=url,filename='./python.mp4')