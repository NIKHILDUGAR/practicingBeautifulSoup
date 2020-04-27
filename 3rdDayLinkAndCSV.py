import requests
from bs4 import BeautifulSoup
src=requests.get("https://coreyms.com/").text
soup=BeautifulSoup(src,'lxml')
print(article.prettify())
headline=article.a.text
print(headline)
summary=article.find('div',class_='entry-content').p.text
print(summary)
vidsrc=article.find('iframe',class_='youtube-player')['src']
print(vidsrc)
vidid=vidsrc.split('/')[4]
vidid=vidid.split('?')[0]
print(vidid)
yt=f'https://youtube.com/watch?v={vidid}'
print(yt)
import csv
csv_file=open('scrape.csv','w')
csvwriter=csv.writer(csv_file)
csvwriter.writerow(['headerline','summary','link'])
for article in soup.find_all('article'):

    headline = article.a.text
    summary = article.find('div', class_='entry-content').p.text
    try:
        vidsrc = article.find('iframe', class_='youtube-player')['src']
        vidid = vidsrc.split('/')[4]
        vidid = vidid.split('?')[0]
        #print(vidid)
        yt = f'https://youtube.com/watch?v={vidid}'

    except:
        yt=None
    print(yt)
    print("")
    csvwriter.writerow([headline,summary,yt])
csv_file.close()
