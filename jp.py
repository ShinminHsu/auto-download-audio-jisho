from scrapy.selector import Selector
import urllib.request
import requests
import pandas as pd

df = pd.read_csv("/Users/smhsu/Documents/N3.csv")
jp = df.iloc[:,0]

def auto_dict(item):

    try:
        item_encoding = urllib.request.quote(item)

        u="https://jisho.org/search/"+item_encoding
        #print(u)
        r=urllib.request.Request(u,headers={'User-Agent':''})

        data = urllib.request.urlopen(r).read()

        t = Selector(text=data)
        audio_path = 'http:'+t.xpath("//source/@src").get()
        a = requests.get(audio_path, allow_redirects=True)
        open('./audio/%s.mp3' % (item), 'wb').write(a.content)

        print("%s Downloaded") % (item)
    except:
        print("%s Failed") % (item)

    return 0


for i in jp:
    auto_dict(i)







