from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re
import datetime

random.seed(datetime.datetime.now())


def getLinks(first_url):
    # https: // movie.douban.com / subject / 1307739 /?from=subject - page
    html = urlopen("https://movie.douban.com/subject/" + first_url + "/?from=subject-page")
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"class": "recommendations-bd"}).findAll("a",
                                                                      href=re.compile("\d(?!img)"))


links = getLinks("1307739")
while len(links) > 0:
    newUrl = links[random.randint(0, len(links) - 1)].attrs['href']
    newUrl2 = [int(x) for x in re.findall("\d",newUrl)]
    num = int(''.join(map(str, newUrl2)))
    print(num)
    getLinks(str(num))
