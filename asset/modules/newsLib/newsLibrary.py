#newsapi.org Great Api
#https://newsapi.org/docs/endpoints/everything
import random
from newsapi.newsapi_client import NewsApiClient
from datetime import datetime,timedelta
import random
# Init
newsapi = NewsApiClient(api_key='2b613eac07a2422996b431ce5b9c68fa')

#q is keyword
#format of date is yyyy-mm-dd
#Cant request more than one month old articles

def news_func(passedKeywords=['india','delhi']):
    keyWords = passedKeywords
    headlines = []
    for keys in keyWords:
        case = str(keys)
        today = str(datetime.now().date())
        period = datetime.now() - timedelta(15)
        lastday = str(period.date())

        all_headlines = newsapi.get_everything(q=case,from_param=today,to=lastday,language='en')
        headlines = headlines + all_headlines['articles']
        #print(headlines)
    return headlines
