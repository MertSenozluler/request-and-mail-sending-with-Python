# -*- coding: utf-8 -*-
import configparser
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import time
#  The part that creates the url and returns a list

class Url:      
    def getUrl(self,page):

        config = configparser.ConfigParser()
        config.read('filter.ini', encoding='utf-8')
    

        carDict = {}

        colorCodes = {"WHITE": "33611", "BLACK": "33616", "GREY": "33612", "RED": "33613", "ORANGE": "40148", "GREEN": "33618", "BLUE": "33610",  "BROWN": "33621", "SMOKED": "658878", "CHAMPAGNE": "675106", "YELLOW": "33614", "PURPLE": "33624", "PINK": "40167",  "BEIGE": "655354"}


        for section in config.sections():
            for key, value in config.items(section):
                carDict[key] = value
        colorCode = colorCodes.get(carDict["color"].upper(), "")

        url = "https://www.sahibinden.com/"+ carDict["model"] +"?pagingOffset="+str(page)+"&a3=" +colorCode+ "&a5_max="+ carDict["max_year"]+"&a4_max="+carDict["max_km"]+"&sorting=price_asc&a4_min="+carDict["min_km"]+"&a5_min="+ carDict["min_year"]+"&price_min="+carDict["min_price"]+"&price_max"+carDict["max_price"]
        print('*******************************************************************************')
        print(url)
        print('*******************************************************************************')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        retry_count = 3
        for i in range(retry_count):
            try:
                req = Request(url, headers=headers)
                with urlopen(req, timeout=10) as response:
                    page = response.read()
                break
            except Exception as e:
                print(e)
                if i == retry_count - 1:
                    raise
            time.sleep(12)

        soup = BeautifulSoup(page, 'html.parser')
        lists = soup.find_all("tr", class_=["searchResultsItem", "searchResultsPromoHighlight", "searchResultsPromoBold","searchResultsPromoSuper","searchResultsFireSale"])
        
        return lists