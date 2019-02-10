from scrapy.selector import Selector
import urllib.request
import requests
import pandas as pd

df = pd.read_csv("/Users/smhsu/Documents/N3.csv")
jp = df.iloc[:,0]
audio = []

def auto_dict(item):

    try:
        #change the encdoing of japanese word
        item_encoding = urllib.request.quote(item)

        #build the url of word
        u="https://jisho.org/search/"+item_encoding
        #print(u)
        r=urllib.request.Request(u,headers={'User-Agent':''})

        #read the html code from the url
        data = urllib.request.urlopen(r).read()
        t = Selector(text=data)
        audio_path = 'http:'+t.xpath("//source/@src").get() #find the mp3 file directory
        a = requests.get(audio_path, allow_redirects=True)

        file_name = item + '.mp3'
        open('./audio/%s' % (file_name), 'wb').write(a.content) #download the mp3 file
        audio.append("[sound:" + file_name + "]") #create a name to put into anki
        print("%s Downloaded" % (item))

    except:
        print("%s Failed" % (item))
        audio.append("")

    return 0


for i in jp:
    auto_dict(i)

df['audio'] = audio

df.to_csv(path_or_buf="audio_N3.csv" ,index=False)







