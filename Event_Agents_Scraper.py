from calendar import c
from http.client import OK
from pydoc import getpager
from socket import getprotobyname
from typing import Mapping
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import requests


url = "https://www.vlr.gg/event/agents/1014/valorant-champions-tour-stage-2-masters-copenhagen"
def Get_Page(url):
    ActivePage = requests.get(url)
    return ActivePage.text

active_Page = Get_Page(url)
theSOUP = BeautifulSoup(active_Page, "html.parser")
Agents_ORDER = []
maps_ORDER = []
teams_ORDER = []

def comp_compare():
    #return t or f bool after comparing comps - for panda filtering requests, removing dupes, etc .
    pass

def get_map_order():
    pass

def get_agent_order(HasAgents):
    global Agents_ORDER
    HasAgents.contents = nlk(HasAgents.contents)
    Agents_ORDER = list(HasAgents.contents[4:23])
    for i in range(len(Agents_ORDER)):
        Agents_ORDER[i] = str(Agents_ORDER[i].contents[1])
        Agents_ORDER[i] = Agents_ORDER[i].split('.')[0][31:]      

def nlk(x):
    newlist = [y for y in x if y != '\n']
    return newlist

get_PR_OBJ = theSOUP.find("table", class_="wf-table mod-pr-global")
def get_pick_rates(get_PR_OBJ):
    #table class_="wf-table mod-pr-global"
    get_PR_OBJ.contents = nlk(get_PR_OBJ.contents)
    get_agent_order(get_PR_OBJ.contents[0])
    overall_pickrates = find_overall_pickrates(get_PR_OBJ)
    map_pickrates = find_map_pickrates(get_PR_OBJ)
    return overall_pickrates, map_pickrates
def deal_with_mod_right(currentcringe):
    global maps_ORDER
    for i in range(len(currentcringe)):
        currentcringe[i] = re.split("([A-Z]\w+|\d+%|\d+)", currentcringe[i].text)[1]
    maps_ORDER.append(list(currentcringe))
def find_overall_pickrates(overall_PR_OBJ):
    overall_data = nlk(overall_PR_OBJ.find("tr", class_="pr-global-row mod-all").contents)
    deal_with_mod_right(overall_data[1:4])
    overall_data = overall_data[4:]
    for i in range(len(overall_data)):
        overall_data[i] = re.split("(\d+%)", overall_data[i].text)[1]
    return overall_data
def find_map_pickrates(overall_PR_OBJ):
    def split_and_clean(contents):
        contents = nlk(contents)
        deal_with_mod_right(contents[:4])
        contents = contents[4:]
        for i in range(len(contents)):
            contents[i] = re.split("(\d+%)", contents[i].text)[1]
        return contents
    map_data = overall_PR_OBJ.contents[2:]
    for i in range(len(map_data)):
        map_data[i] = split_and_clean(map_data[i].contents)
    return map_data
PickRates = get_pick_rates(get_PR_OBJ)

print("z")
get_comps_OBJ = theSOUP.find_all("div", class_="pr-matrix-map")
def get_comps(get_comps_OBJ):
    get_comps_OBJ = prepare_soup_comps(get_comps_OBJ)
    for i in range(len(get_comps_OBJ)):
        find_teams_picks_overall(get_comps_OBJ[i])
    pass
def split_teams_matches(tempList):
    tempList.pop(0)
    sorted_list = []
    cntr = 0
    for i in range(len(tempList)):#why break
        if len(tempList[i].attrs['class']) == 1: 
            sorted_list.append(nlk(tempList[i].contents))
            sorted_list[cntr].pop(0)
            sorted_list[cntr].pop(0)
            sorted_list[cntr].pop(-1)
            sorted_list[cntr].pop(-1)
            sorted_list[cntr].append(re.split("([A-Z]\w+)", tempList[i].text)[1])
            cntr += 1
        else:
            sorted_list[cntr-1].append(nlk(tempList[i]))
    return sorted_list
def prepare_soup_comps(get_comps_OBJ):
    for i in range(len(get_comps_OBJ)):
        get_comps_OBJ[i] = nlk(get_comps_OBJ[i].contents[1].contents[1].contents)
        get_comps_OBJ[i] = split_teams_matches(get_comps_OBJ[i])
    return get_comps_OBJ
def find_teams_picks_overall(comps_obj):
    pass
def find_oponent_WL_compPlayed():
    #td class_="mod-loss"
    #tr class_="pr-matrix-row mod-dropdown"
    #td class_="mod-picked-lite"
    pass

AgentsSelected = get_comps(get_comps_OBJ)

def group_teams_compPlayed():
    pass