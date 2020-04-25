import bs4 as bs
import urllib.request
sauce=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup=bs.BeautifulSoup(sauce,'lxml')
import pandas as pd
for para in soup.find_all('p'):
   print(para.text)
print(soup.get_text())
for url in soup.find_all('a'):
    print(url.get('href'))
nav=soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))
table=soup.find('table')
trr=table.find_all('tr')
for tr in trr:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)
dfs=pd.read_html('https://pythonprogramming.net/parsememcparseface/')
for df in dfs:
    print(df)
sauce=urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup=bs.BeautifulSoup(sauce,'xml')
for url in soup.find_all('loc'):
    print(url.text)
