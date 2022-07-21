from lib2to3.pgen2.token import NEWLINE
import statistics
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import requests

filterlist=['astra', 'breach', 'brimstone', 'chamber', 'cypher', 'fade', 'jett', 'kayo', 'killjoy', 'neon', 'omen', 'phoenix', 'raze', 'reyna', 'sage', 'skye', 'sova', 'viper', 'yoru']
url_filtered = "https://www.vlr.gg/event/stats/1014/valorant-champions-tour-stage-2-masters-copenhagen?exclude=&min_rounds={minrnd}&agent={agent}"


url = "https://www.vlr.gg/event/stats/1014/valorant-champions-tour-stage-2-masters-copenhagen?exclude=&min_rounds=0&agent=astra"
def Get_Page(url):
    ActivePage = requests.get(url)
    return ActivePage.text
active_Page = Get_Page(url)
theSOUP = BeautifulSoup(active_Page, "html.parser")
stat_categories_OBJ = theSOUP.findAll("thead")
stats_thestats_OBJ = theSOUP.findAll("tbody")
def new_stat_dict(clean_data):
#     >>> s = 'A - 13, B - 14, C - 29, M - 99'
# >>> dict(e.split(' - ') for e in s.split(','))
# {'A': '13', 'C': '29', 'B': '14', 'M': '99'}
#split on 
        pass
def nlk(x):
    newlist = [y for y in x if y != '\n']
    return newlist
def get_stat_categories(stats_in):
    newlist=['Player',]
    for i in range(1,len(stats_in)):
        stats_in[i]=str(stats_in[i])
        newstr=str(re.findall('title=".+"', stats_in[i]))
        newlist.append(newstr[9:-3])
    return newlist
cleaned_stat_categories = nlk(stat_categories_OBJ[0].contents[1].contents)
stat_categories=get_stat_categories(cleaned_stat_categories)
cleaned_stats = nlk(stats_thestats_OBJ[0].contents)

def split_players_picks_rnds(player_in):
    returnlist=[]
    returnlist.extend((player_in[0].text[4:-3]).splitlines())
    returnlist.append(player_in[2].text + " rnds")
    return returnlist
def split_stats(stats_in):
    statlist=[]
    for i in range(len(stats_in)):
        statlist.append(stats_in[i].text.strip())

    return statlist
def get_stats(stats_in):
    players_picks_rnds=[]
    stats=[]
    for i in range(len(stats_in)):
        stats_in[i].contents = nlk(stats_in[i].contents)
        players_picks_rnds.append(list(split_players_picks_rnds(stats_in[i].contents[0:3])))
        stats.append(list(split_stats(stats_in[i].contents[3:])))
    pass
get_stats(cleaned_stats)
for i in range(len(filterlist)):
    pass

















print("howareya")