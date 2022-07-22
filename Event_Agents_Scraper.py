from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import requests



Agents_ORDER = []
teams_ORDER = []
maps_ORDER = []
atk_def_wl = []

def comp_compare():
    #return t or f bool after comparing comps - for panda filtering requests, removing dupes, etc .
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



def get_pick_rates(get_PR_OBJ):
    #table class_="wf-table mod-pr-global"
    get_PR_OBJ.contents = nlk(get_PR_OBJ.contents)
    get_agent_order(get_PR_OBJ.contents[0])
    overall_pickrates = find_overall_pickrates(get_PR_OBJ)
    map_pickrates = find_map_pickrates(get_PR_OBJ)
    return overall_pickrates, map_pickrates

def deal_with_mod_right(currentcringe):
    global atk_def_wl
    for i in range(len(currentcringe)):
        currentcringe[i] = re.split("([A-Z]\w+|\d+%|\d+)", currentcringe[i].text)[1]
    atk_def_wl.append(list(currentcringe))

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


def get_comps(get_comps_OBJ):
    def assemblequick(nlst):
        global teams_ORDER
        for i in range(len(nlst)):
            teams_ORDER.append(nlst[i][-1])
    bigboy = []
    get_comps_OBJ = prepare_soup_comps(get_comps_OBJ)
    for i in range(len(get_comps_OBJ)):
        bigboy.append(find_teams_picks_overall(get_comps_OBJ[i]))
    assemblequick(bigboy[0][0])
    return bigboy
def prepare_soup_comps(get_comps_OBJ):
    global maps_ORDER
    for i in range(len(get_comps_OBJ)):
        maps_ORDER.append(re.findall("[A-Z]\w+", get_comps_OBJ[i].text)[0])
        get_comps_OBJ[i] = nlk(get_comps_OBJ[i].contents[1].contents[1].contents)
        get_comps_OBJ[i] = split_teams_matches(get_comps_OBJ[i])
        
    return get_comps_OBJ
def split_teams_matches(tempList):
    tempList.pop(0)
    sorted_list = []
    cntr = 0
    for i in range(len(tempList)):
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

def find_teams_picks_overall(comps_obj):
    picks_overall_list = []
    op_WL_compPlayed_list = []
    for i in range(len(comps_obj)):
        picks_overall_list.append(split_overall_from_matches(comps_obj[i]))
    for i in range(len(picks_overall_list)):
        op_WL_compPlayed_list.append(find_oponent_WL_compPlayed(picks_overall_list[i][1]))
        picks_overall_list[i] = picks_overall_list[i][0]
    
    return picks_overall_list, op_WL_compPlayed_list

def split_overall_from_matches(comps_obj):#groups all picks on map and relevant match
    global Agents_ORDER
    for i in range(len(Agents_ORDER)):
        if len(comps_obj[i].attrs['class'])>0: #replaces mod-picked with agent name
            comps_obj[i] = Agents_ORDER[i]
    newlist = [x for x in comps_obj if type(x) == str] #fills list with agent names
    newlist2 = [y for y in comps_obj[len(Agents_ORDER):] if type(y) != str] #fills list with everything else
    return newlist, newlist2

def find_oponent_WL_compPlayed(matches_list):
    def deal_with_result_op(modresult):#splits result, matchup from data block
        vspattern = re.compile("vs. \w+")
        newlist = []
        if str(modresult) == '[<td class="mod-win"':
            newlist.append('W')
        else:
            newlist.append('L')
        newlist.append(re.search(vspattern, modresult.text).group())
        return newlist
    def deal_with_comp(compdata):#splits and assembles comp from data block
        global Agents_ORDER
        for i in range(len(compdata)):
            if len(compdata[i].attrs['class'])>0:
                compdata[i] = Agents_ORDER[i]
        newlist = [x for x in compdata if type(x) == str]
        return newlist
    newlist = []
    for i in range(len(matches_list)):#appends cleaned data to return list
        newlist.append(deal_with_result_op(matches_list[i][0]))#
        newlist[i].append(deal_with_comp(matches_list[i][2:]))#
    return newlist

url = "https://www.vlr.gg/event/agents/1014/valorant-champions-tour-stage-2-masters-copenhagen"
def Get_Page(url):
    ActivePage = requests.get(url)
    return ActivePage.text


def call_all(url):
    active_Page = Get_Page(url)
    theSOUP = BeautifulSoup(active_Page, "html.parser")
    get_comps_OBJ = theSOUP.find_all("div", class_="pr-matrix-map")
    get_PR_OBJ = theSOUP.find("table", class_="wf-table mod-pr-global")
    PickRates = get_pick_rates(get_PR_OBJ)
    AgentsSelected = get_comps(get_comps_OBJ)
    return PickRates,AgentsSelected

def organise_for_PANDAS(Comp_Data, PR_Data):
    pass
print("Dese")
    