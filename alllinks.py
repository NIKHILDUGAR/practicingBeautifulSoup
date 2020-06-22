#scrape all links linked in a web site
#ALL 4 FUNCTIONS DO THE SAME JOB
import requests
import re
import lxml.html
import lxml
from selectolax.parser import HTMLParser
k=input("Enter URL to parse - ")
try:
    r=requests.get(k)
except:
    r = requests.get("http://"+k)
    k="http://"+k
def extractlink(s):
    l=[]
    dom = HTMLParser(s)
    for tag in dom.tags("a"):
        attrs=tag.attributes
        if "href" in attrs:
            if str(attrs["href"]).startswith(r"/"):
                l.append(k + attrs["href"])
            else:
                if attrs["href"].startswith(r"http"):
                    l.append(attrs["href"])
                elif attrs["href"]:
                    l.append(k + r"/" + attrs["href"])
    return l
def linkextractor(s):
    t=re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1',re.IGNORECASE)
    l=[]
    l1=[match[1] for match in t.findall(s)]
    for i in l1:
        if str(i).startswith(r"/"):
            l.append(k + i)
        else:
            if i.startswith(r"http"):
                l.append(i)
            elif i:
                l.append(k + r"/" + i)
    return l
def linkextractorlxml(s):
    l=[]
    dom=lxml.html.fromstring(s)
    for i in dom.xpath('//a/@href'):
        if str(i).startswith(r"/"):
            l.append(k + i)
        else:
            if i.startswith(r"http"):
                l.append(i)
            elif i:
                l.append(k + r"/" + i)
    return l
from bs4 import BeautifulSoup as bs
def extractbs(s):
    l=[]
    soup=bs(s,"lxml")
    for tag in soup.findAll("a",href=True):
        if str(tag["href"]).startswith(r"/"):
            l.append(k+tag["href"])
        else:
            if tag["href"].startswith(r"http"):
                l.append(tag["href"])
            elif tag["href"]:
                l.append(k+r"/"+tag["href"])
    return l

for i in extractbs(r.text):
    print("URLS of the website - " , i)
for i in extractlink(r.text):
    print("URLS of the website - " , i)
for i in linkextractor(r.text):
    print("URLS of the website - " , i)
for i in linkextractorlxml(r.text):
    print("URLS of the website - " , i)
