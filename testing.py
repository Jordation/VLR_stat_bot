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
    return Map_In
    
    

def Get_Opononent_List(Active_Map_Object):
    pattern = re.compile("(vs. \w+ \w+ \w+)|(vs. \w+ \w+)|(vs. \w+)")
    Match_list = []
    ugly_matchlist = str(Active_Map_Object.text)
    for x in re.finditer(pattern, ugly_matchlist):
        Match_list.append(str(x.group()))
    return Match_list

def Get_team_list(Active_map_Object):
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
    MatchesPlayed = []
    for i in range(12):
        temp_list.clear()
        for y in range(19):
            if onesandzeros[i][y] == 1:
                temp_list.append(str(Agents_Ordered[y]))
        export_picks.append({'Team': Teams[i], 'Agents Picked': list(temp_list), 'Matches': MatchesPlayed})
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

def ImSoSorry(forgiveme):
    forgiveme = str(forgiveme)
    p = forgiveme.split('>')
    p.pop(1)
    forgiveme = str(p[0])
    return forgiveme

def OneZero_To_agents_M(oneszeros):
    PickedAgents = []
    global OrderedAgents
    oneszeros[0] = ImSoSorry(oneszeros)
    for i in range(20):
        if oneszeros[i] == 1:
            PickedAgents.append(OrderedAgents[i-1])
        elif str(oneszeros[i]) == '[<td class="mod-win"':
            PickedAgents.append('W')
        elif str(oneszeros[i]) == '[<td class="mod-loss"':
            PickedAgents.append('L')
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

def CleanMatchList(MatchList):
    for i in range(len(MatchList)):
        MatchList[i] = MatchList[i][4:]
    return MatchList

def Begin_Assemble(OpponentList, GroupedMatches, TeamsList, damap, TeamDicts):
    def Make_match_dicts(Match, Team, Opponent):
        matchDict = {}
        matchDict["Team"]=str(Team)
        matchDict["Opponent"]=str(Opponent)
        matchDict["Result"]=str(Match[0])
        matchDict["Comp"]=list(Match[1:6])
        return matchDict
    
    LTeams = list(TeamDicts)
    Matches_Counter = 0
    ThisMap={'Map': damap, 'Teams': LTeams}
    OpponentList = CleanMatchList(OpponentList)
    
    for i in range(len(LTeams)):
        aha = []
        aha.clear()
        for y in range(len(GroupedMatches[i])):
            aha.append(Make_match_dicts(GroupedMatches[i][y], TeamsList[i], OpponentList[Matches_Counter]))
            Matches_Counter += 1
            ThisMap['Teams'][i]['Matches'] = aha
    return ThisMap

def GetMapsReady(wftable):
    retlist = []
    for i in range(len(wftable.contents)):
        if wftable.contents[i] != '\n':
            retlist.append(wftable.contents[i])
    return retlist


#events_maps = [0,0,0,0,0,0,0]
#Actv_Map = soup.find_all("div", class_="pr-matrix-map")
#events_maps[0]=Actv_Map[0].contents[1].contents[1]
#events_maps[1]=Actv_Map[1].contents[1].contents[1]
#events_maps[2]=Actv_Map[2].contents[1].contents[1]
#events_maps[3]=Actv_Map[3].contents[1].contents[1]
#events_maps[4]=Actv_Map[4].contents[1].contents[1]
#events_maps[5]=Actv_Map[5].contents[1].contents[1]
#events_maps[6]=Actv_Map[6].contents[1].contents[1]
#for i in range(len(events_maps)):
#    events_maps[i] = GetMapsReady(events_maps[i])

Map_1_All_Picks = []
Map_2_All_Picks = []
Map_3_All_Picks = []
Map_4_All_Picks = []
Map_5_All_Picks = []
Map_6_All_Picks = []
Map_7_All_Picks = []

OrderedAgents = list(ItAintPretty())

Actv_Map = soup.find("div", class_="pr-matrix-map").contents[1].contents[1]
for i in range(len(Actv_Map.contents)):
    if Actv_Map.contents[i] != '\n':
        Map_1_All_Picks.append(Actv_Map.contents[i])

Teams_s_Matches = Split_Teams_From_Map(Map_1_All_Picks)
for i in range(len(Teams_s_Matches)):
    Teams_s_Matches[i].contents = begone_newlineSHITFUCKOFFFFFF(Teams_s_Matches[i].contents)
Cleaned_Match_Data = Team_Played_MATCH(Teams_s_Matches)
Oponent_List = Get_Opononent_List(Actv_Map)
Active_Map = get_map_map_map(Actv_Map)

HTML_Comps_to_01 = Team_played_OVERALL(Teams_s_Matches)
Teams_Playing = Get_team_list(Actv_Map)
Team_Overall_Picked = Assemble_Comps(OrderedAgents, HTML_Comps_to_01, Teams_Playing)

event_TEST = []
event_TEST.append(Begin_Assemble(Oponent_List, Cleaned_Match_Data, Teams_Playing, Active_Map, Team_Overall_Picked))

Next_Map = Actv_Map.find_next("div", class_="pr-matrix-map").contents[1].contents[1]
for i in range(len(Next_Map.contents)):
    if Next_Map.contents[i] != '\n':
        Map_2_All_Picks.append(Next_Map.contents[i])

Teams_s_Matches = Split_Teams_From_Map(Map_2_All_Picks)
for i in range(len(Teams_s_Matches)):
    Teams_s_Matches[i].contents = begone_newlineSHITFUCKOFFFFFF(Teams_s_Matches[i].contents)
Cleaned_Match_Data = Team_Played_MATCH(Teams_s_Matches)
Oponent_List = Get_Opononent_List(Next_Map)
Active_Map = get_map_map_map(Next_Map)

HTML_Comps_to_01 = Team_played_OVERALL(Teams_s_Matches)
Teams_Playing = Get_team_list(Next_Map)
Team_Overall_Picked = Assemble_Comps(OrderedAgents, HTML_Comps_to_01, Teams_Playing)

event_TEST.append(Begin_Assemble(Oponent_List, Cleaned_Match_Data, Teams_Playing, Active_Map, Team_Overall_Picked))

print(event_TEST)
