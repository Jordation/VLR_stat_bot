from lib2to3.pgen2.token import NEWLINE
import statistics
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import requests
filterlist=['astra', 'breach', 'brimstone', 'chamber', 'cypher', 'fade', 'jett', 'kayo', 'killjoy', 'neon', 'omen', 'phoenix', 'raze', 'reyna', 'sage', 'skye', 'sova', 'viper', 'yoru']
url_filtered = "https://www.vlr.gg/event/stats/1014/valorant-champions-tour-stage-2-masters-copenhagen?exclude=&min_rounds={}&agent={}"
def nlk(x):
    newlist = [y for y in x if y != '\n']
    return newlist
def get_stat_categories(stats_in):
    newlist=['Name', 'Team']
    for i in range(1,len(stats_in)):
        stats_in[i]=str(stats_in[i])
        newstr=str(re.findall('title=".+"', stats_in[i]))
        newlist.append(newstr[9:-3])
    return newlist
def split_players_picks_rnds(player_in, filterlist, filterlistnum):
    returnlist=[]
    returnlist.extend((player_in[0].text[4:-3]).splitlines())
    returnlist.append(str(filterlist[filterlistnum]))
    returnlist.append(player_in[2].text)
    return returnlist
def split_stats(stats_in):
    statlist=[]
    for i in range(len(stats_in)):
        statlist.append(stats_in[i].text.strip())
    return statlist
def get_stats(stats_in, filterlist, filterlistnum):
    stats=[]
    for i in range(len(stats_in)):
        stats_in[i].contents = nlk(stats_in[i].contents)
        stats.append(list(split_players_picks_rnds(stats_in[i].contents[0:3], filterlist, filterlistnum)))
        stats[i].extend((split_stats(stats_in[i].contents[3:])))
    return stats
def player_dict(categories, stats):
    d={}
    for x in range(len(categories)):
        d[categories[x]] = stats[x]
    return d
def make_export_dict(stat_categories, stats):
    l=[]
    for i in range(len(stats)):
        l.append(player_dict(stat_categories, stats[i]))
    return l

def new_url(url, filterlist, flistnum):
    newurl = url.format(0, filterlist[flistnum])
    ActivePage = requests.get(newurl)
    return ActivePage.text

def call_all(url_filtered, filterlist, filterlistnum):
    stat_dicts=[]
    active_Page = new_url(url_filtered, filterlist, filterlistnum)
    theSOUP = BeautifulSoup(active_Page, "html.parser")
    stat_categories_OBJ = theSOUP.findAll("thead")
    stats_thestats_OBJ = theSOUP.findAll("tbody")
    
    cleaned_stat_categories = nlk(stat_categories_OBJ[0].contents[1].contents)
    stat_categories=get_stat_categories(cleaned_stat_categories)
    
    cleaned_stats = nlk(stats_thestats_OBJ[0].contents)
    stats = get_stats(cleaned_stats, filterlist, filterlistnum)
    
    stat_dicts.append(make_export_dict(stat_categories, stats))
    if len(stat_dicts) == 0:
        stat_dicts=("No pick data for " + filterlist[filterlistnum])
    return stat_dicts

print("howareya")