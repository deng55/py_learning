from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())
# 获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):
        internalLinks = []
        # 找出所有以‘/’开头的链接
        for link in bsObj.findAll("a", href=re.compile("(^/|.*"+includeUrl+")")):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in internalLinks:
                    internalLinks.append(link.attrs['href'])
        return internalLinks


# 獲取頁面所有外鏈的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以'http'或'www' 開頭且不包含當前url的鏈接
    for link in bsObj.findAll("a", href= re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in excludeUrl:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddredd(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj,splitAddredd(startingPage)[0])
    if len(externalLinks)==0:
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    # externalLinks = getRandomExternalLinks("http://oreilly.com")
    externalLinks = getRandomExternalLinks(startingSite)
    print("隨機外鏈是："+externalLinks)
    followExternalOnly(externalLinks)

# followExternalOnly("http://oreilly.com")
followExternalOnly("http://zhihu.com")

