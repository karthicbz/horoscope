import requests
from bs4 import BeautifulSoup

def parseUrl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    mainData = soup.find_all('div',{'class':'tablet-ad'})
    for data in mainData:
        print(data.contents[1].find_all('p')[0].text)

parseUrl('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=3')

#https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=ta&dt=t&q=what
