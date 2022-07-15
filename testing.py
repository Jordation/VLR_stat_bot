from glob import glob
from hashlib import new
from multiprocessing.spawn import prepare
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

def PrepareMap(Map):
    newlist = [x for x in Map if x != '\n']
    return newlist
def PrepareMatchData(Map):
    newlist = [x for x in Map if x != '\n']
    negativeindex = (23-len(newlist)-1)
    for i in range(2):
        newlist.pop(negativeindex)
        newlist.pop(0)
    return newlist

OrderedAgents = list(ItAintPretty())
Map1 = soup.find("div", class_="pr-matrix-map").contents[1].contents[1]
Map1_picks = PrepareMap(Map1.contents)
Map1_matches = Split_Teams_From_Map(Map1_picks)
for i in range(len(Map1_matches)):
    Map1_matches[i].contents = PrepareMatchData(Map1_matches[i].contents)
Map1_comps_01 = Team_played_OVERALL(Map1_matches)
Map1_Oponent_List = Get_Opononent_List(Map1)
Map1_Cleaned_Matches = Team_Played_MATCH(Map1_matches)
Map1_Teams_Playing = Get_team_list(Map1)
m1Team_Overall_Picked = Assemble_Comps(OrderedAgents, Map1_comps_01, Map1_Teams_Playing)
Map1_Active_Map = get_map_map_map(Map1)

event_TEST = []
event_TEST.append(Begin_Assemble(Map1_Oponent_List, Map1_Cleaned_Matches, Map1_Teams_Playing, Map1_Active_Map, m1Team_Overall_Picked))

print(event_TEST)

Map2 = Map1.find_next("div", class_="pr-matrix-map").contents[1].contents[1]
Map2_picks = PrepareMap(Map2.contents)
Map3 = Map2.find_next("div", class_="pr-matrix-map").contents[1].contents[1]
Map3_picks = PrepareMap(Map3.contents)
Map4 = Map3.find_next("div", class_="pr-matrix-map").contents[1].contents[1]
Map4_picks = PrepareMap(Map4.contents)
Map5 = Map4.find_next("div", class_="pr-matrix-map").contents[1].contents[1]
Map5_picks = PrepareMap(Map5.contents)
Map6 = Map5.find_next("div", class_="pr-matrix-map").contents[1].contents[1]
Map6_picks = PrepareMap(Map6.contents)
Map7 = Map6.find_next("div", class_="pr-matrix-map").contents[1].contents[1]
Map7_picks = PrepareMap(Map7.contents)



Map2_matches = Split_Teams_From_Map(Map2_picks)
for i in range(len(Map2_matches)):
    Map2_matches[i].contents = PrepareMatchData(Map2_matches[i].contents)
Map2_comps_01 = Team_played_OVERALL(Map2_matches)
Map2_Oponent_List = Get_Opononent_List(Map2)
Map2_Cleaned_Matches = Team_Played_MATCH(Map2_matches)
Map2_Teams_Playing = Get_team_list(Map2)
m2Team_Overall_Picked = Assemble_Comps(OrderedAgents, Map2_comps_01, Map2_Teams_Playing)
Map2_Active_Map = get_map_map_map(Map2)

event_TEST.append(Begin_Assemble(Map2_Oponent_List, Map2_Cleaned_Matches, Map2_Teams_Playing, Map2_Active_Map, m2Team_Overall_Picked))