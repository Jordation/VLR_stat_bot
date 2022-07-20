from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import requests


url = "https://www.vlr.gg/event/stats/1014/valorant-champions-tour-stage-2-masters-copenhagen?exclude=&min_rounds=0&agent=astra"
def Get_Page(url):
    ActivePage = requests.get(url)
    return ActivePage.text
active_Page = Get_Page(url)
theSOUP = BeautifulSoup(active_Page, "html.parser")
stat_categories_OBJ = theSOUP.findAll("thead")
stats_thestats_OBJ = theSOUP.findAll("tbody")

def nlk(x):
    newlist = [y for y in x if y != '\n']
    return newlist
cleaned_stats = nlk(stat_categories_OBJ[0].contents[1].contents)
def get_stat_categories(stats_in):
    newlist=['Player',]
    for i in range(1,len(stats_in)):
        stats_in[i]=str(stats_in[i])
        newstr=str(re.findall('title=".+"', stats_in[i]))
        newlist.append(newstr[9:-3])
    return newlist
    
stat_categories=get_stat_categories(cleaned_stats)

















print("howareya")