from bs4 import BeautifulSoup
import requests
import random
import re
import webbrowser
import sys
sys.path.append("..")

from asset.modules.OpenUrl.openurl import openweb
from asset.modules.playvideo.play import playthis

def boredomKiller():
    options = ["youtube","fossbytes","moz"]
    option = options[random.randint(0,len(options))]

    if option == "youtube":
        html = requests.get("https://www.youtube.com/feed/trending")
        soup = BeautifulSoup(html.text,"html.parser")
        finalResults = []
        for link in soup.findAll('a', attrs={'href': re.compile("^/watch")}):
            finalResults.append(link.get('href'))
        
        uselink = "https://www.youtube.com"+finalResults[random.randint(0,len(finalResults))]
        playthis(uselink)

    elif option == "fossbytes":
        html = requests.get("https://fossbytes.com/most-useful-websites-internet/")
        soup = BeautifulSoup(html.text,"html.parser")
        results = []
        for link in soup.findAll('a', attrs={'href': re.compile("^http|https")}):
            results.append(link.get('href'))
        finalResults = [result for result in results if not re.search("fossbytes",result)]
        
        uselink = finalResults[random.randint(0,len(finalResults)-1)]
        webbrowser.open(uselink,new=2)
    
    else:
        html = requests.get("https://moz.com/top500")
        soup = BeautifulSoup(html.text,"html.parser")
        results = []
        for link in soup.findAll('a', attrs={'href': re.compile("^http|https")}):
            results.append(link.get('href'))
        finalResults = [result for result in results if not re.search("moz",result)]
        uselink = finalResults[random.randint(0,len(finalResults)-1)]
        webbrowser.open(uselink,new=2)
