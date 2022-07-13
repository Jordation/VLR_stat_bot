from glob import glob
from hashlib import new
from operator import index
from reprlib import recursive_repr
from this import d
from tokenize import group
from turtle import pos
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import asyncio

with open("newtest.html") as testpage:
    soup = BeautifulSoup(testpage, "html.parser")
  
 
def remove_newlines(oldlist):
    newlist_cleaned = []
    for i in range(len(oldlist)):
        if oldlist[i] != '\n':
            newlist_cleaned.append(oldlist[i])
    return newlist_cleaned
        
def Split_Teams_From_Map(SentData):
    CleanedPickData = []
    for i in range(12):
        CleanedPickData.append(i)
    othercounter = -1
    ShouldBeTeamsCount = 0
    SentData.pop(0)
    for i in range(len(SentData)):
        if str(SentData[i].attrs['class']) == "['pr-matrix-row']":
            CleanedPickData[ShouldBeTeamsCount]=SentData[i]
            ShouldBeTeamsCount += 1
            othercounter += 1
        else:
            CleanedPickData[othercounter].contents.append(SentData[i])
    return CleanedPickData

def get_map_map_map(Active_map_object_lol):
    pattern = re.compile("([A-Z]\w+)")
    textdata = str(Active_map_object_lol.text)
    reobject = re.search(pattern, textdata)
    Map_In = reobject.group(1)
    #UR ALMOST THERE JUST FINISH IT WHEN UR HONME
    return Map_In
    
    

def Get_match_list_map(Active_Map_Object):
    pattern = re.compile("(vs. \w+ \w+ \w+)|(vs. \w+ \w+)|(vs. \w+)")
    Match_list = []
    ugly_matchlist = str(Active_Map_Object.text)
    for x in re.finditer(pattern, ugly_matchlist):
        Match_list.append(str(x.group()))
    return Match_list

def Get_team_list_map(Active_map_Object):
    TeamsPlaying = []
    JustNames = Active_map_Object.find_all('span', class_='text-of')
    for i in range(len(JustNames)):
        for string in JustNames[i].stripped_strings:
            TeamsPlaying.append(string)
    return TeamsPlaying

    
def begone_newlineSHITFUCKOFFFFFF(yeppackitupcunt):
    HoldOnMate = []
    for i in range(len(yeppackitupcunt)):
        if yeppackitupcunt[i] != '\n':
            HoldOnMate.append(yeppackitupcunt[i])
    negativeindex = (23-len(HoldOnMate)-1)
    for i in range(2):
        HoldOnMate.pop(negativeindex)
        HoldOnMate.pop(0)
    return HoldOnMate

def Team_played_OVERALL(RawPicks):
    All_Picks_NO_AGENTS = []
    Picked_NO_AGENTS = []
    for i in range(12):
        Picked_NO_AGENTS.clear()
        for y in range(19):
            if str(RawPicks[i].contents[y]) == '<td class="">\n</td>':
                Picked_NO_AGENTS.append(0)
            else:
                Picked_NO_AGENTS.append(1)
        All_Picks_NO_AGENTS.append(list(Picked_NO_AGENTS))
    return All_Picks_NO_AGENTS

def ItAintPretty():
    AgentListInFunc = []
    global soup
    GetAgents = soup.select("div img")
    for i in range(1,20):
        AgentListInFunc.append(GetAgents[i])
    for i in range(0, len(AgentListInFunc)):
        AgentListInFunc[i] = str(AgentListInFunc[i])
        AgentListInFunc[i] = (AgentListInFunc[i].split('.', 1)[0])
        AgentListInFunc[i] = AgentListInFunc[i][31:]
    return AgentListInFunc

def Get_Individual_Comps(Teams_Matches):
    TempList = []
    for y in range((len(Teams_Matches)-(len(Teams_Matches)-19)), (len(Teams_Matches))):
        newlist = remove_newlines(list(Teams_Matches[y].contents))
        TempList.append(newlist)
    return Teams_Matches
        


def Assemble_Comps(Agents_Ordered, onesandzeros, Teams):
    export_picks = []
    temp_list = []
    for i in range(12):
        temp_list.clear()
        for y in range(19):
            if onesandzeros[i][y] == 1:
                temp_list.append(str(Agents_Ordered[y]))
        export_picks.append({'Team': Teams[i],'Map': 'whatevs', 'Agents Picked': list(temp_list)})
    return export_picks

def OneZeroFromMatches(AgentsPickedData):
    oneandzerolist = []
    grouped_matches = []
    retlist = []
    for i in range(12):
        grouped_matches.clear()
        for x in range(len(AgentsPickedData[i])):
            oneandzerolist.clear()
            oneandzerolist.append(AgentsPickedData[i][x][0])
            for y in range(1, len(AgentsPickedData[i][x])):
                if str(AgentsPickedData[i][x][y]) == '<td class="">\n</td>':
                    oneandzerolist.append(0)
                else:
                    oneandzerolist.append(1)
            grouped_matches.append(list(oneandzerolist))
        retlist.append(list(grouped_matches))
    return retlist

def OneZero_To_agents_M(oneszeros):
    PickedAgents = []
    global Agents
    for i in range(1,20):
        if oneszeros[i] == 1:
            PickedAgents.append(Agents[i-1])
    return PickedAgents
            
        
def Team_Played_MATCH(PickData):
    retlist = []
    templist = []
    for i in range(12):
        templist.clear()
        for y in range(19, len(PickData[i].contents)):
            p = y-19
            templist.append(remove_newlines(list(PickData[i].contents[y].contents)))
            templist[p].pop(1)
        retlist.append(list(templist))
    retlist = OneZeroFromMatches(retlist)
    for i in range(len(retlist)):
        for y in range(len(retlist[i])):
            retlist[i][y] = list(OneZero_To_agents_M(retlist[i][y]))
    return retlist

#in use becomes the table nested within pr-matrix-map, - 1 of these per map
#need to automate find.next or whatever

MapName_All_Picks = []
Actv_Map = soup.find("div", class_="pr-matrix-map").contents[1].contents[1]
for i in range(len(Actv_Map.contents)):
    if Actv_Map.contents[i] != '\n':
        MapName_All_Picks.append(Actv_Map.contents[i])

JustPicks = Split_Teams_From_Map(MapName_All_Picks)

for i in range(len(JustPicks)):
    JustPicks[i].contents = begone_newlineSHITFUCKOFFFFFF(JustPicks[i].contents)

#Individual_Comps = []
#for i in range(12):
#        Individual_Comps.append(Get_Individual_Comps(list(JustPicks[i])))

Matches_Played = Get_match_list_map(Actv_Map)

Teams_Playing = Get_team_list_map(Actv_Map)

#cleans picks

#redundant


Agents = list(ItAintPretty())

onesandzerospicks = Team_played_OVERALL(JustPicks)

Cleaned_Match_Data = Team_Played_MATCH(JustPicks)


Map_In_Funcs = get_map_map_map(Actv_Map)

Team_Overall_Picked = Assemble_Comps(Agents, onesandzerospicks, Teams_Playing)
#xD


print("fuckin breakpoint bitch")

# Wizardry = Assemble_TeamsToPicks(Teams_Playing, JustPicks)
# def Assemble_TeamsToPicks(Teams_p, PickData):
#     TheGuy = []
#     for i in range(12):
#         TheGuy.append({'Team': Teams_p[i], 'Played Map Count': (len(PickData[i].contents)-19), 'Matches': PickData[i]})
#     return TheGuy