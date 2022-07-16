from glob import glob
from hashlib import new
from operator import index
from reprlib import recursive_repr
from turtle import pos
from xml.sax.handler import all_properties
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import asyncio

from pkg_resources import working_set

with open("newtest.html") as testpage:
    soup = BeautifulSoup(testpage, "html.parser")
    
Agents = []
GetAgents = soup.select("div img")
for i in range(1,20):
    Agents.append(GetAgents[i])
for i in range(0, len(Agents)):
    Agents[i] = str(Agents[i])
    Agents[i] = (Agents[i].split('.', 1)[0])
    Agents[i] = Agents[i][31:]
    
GlobalPickRates=[]
GetGPRs = soup.select('table[class*="wf-table mod-pr-global"] td span')
for i in range(0,19):
    GlobalPickRates.append(GetGPRs[i])
for i in range(0, len(Agents)):
    GlobalPickRates[i] = str(GlobalPickRates[i])
    GlobalPickRates[i] = (GlobalPickRates[i].split('%', 1)[0])
    GlobalPickRates[i] = GlobalPickRates[i][22:]

GetMapOrder = soup.select('td[style*="white-space: nowrap; padding-top: 0; padding-bottom: 0;"]')
MapOrder_PickRates = []
MapOrder_Comps = []
for i in range(1,8):
    MapOrder_PickRates.append(GetMapOrder[i])
    MapOrder_PickRates[(i-1)] = str(MapOrder_PickRates[(i-1)])
    MapOrder_PickRates[(i-1)] = re.findall("([\^A-Z]\w+)", MapOrder_PickRates[(i-1)])

GetMapOrder2 = soup.select('th[style*="padding: 0; padding-left: 15px; line-height: 0; vertical-align: middle;"]')
MapOrder_Comps = []
for i in range(7):
    MapOrder_Comps.append(GetMapOrder2[i])
    MapOrder_Comps[i] = str(MapOrder_Comps[i])
    MapOrder_Comps[i] = re.findall("([\^A-Z]\w+)", MapOrder_Comps[i])

raw_pickrates = []
PickRateByMap = soup.select('tr div span')
for i in range(len(PickRateByMap)):
    raw_pickrates.append(PickRateByMap[i])
    raw_pickrates[i] = str(raw_pickrates[i])
    raw_pickrates[i] = re.findall("([0-9]+%)", raw_pickrates[i])

map_agent_pickrate_STORED= []
for i in range(8):
    for y in range((i*19),(i+1)*19):
            if i < 1:
                map_agent_pickrate_STORED.append({'Agent':Agents[y],'Pickrate':raw_pickrates[y]})
            else:
                map_agent_pickrate_STORED.append({'Map':MapOrder_PickRates[i-1], 'Agent':Agents[(y%19)],'Pickrate':raw_pickrates[y]})

teams_ordered = []
def GetTeams():
    global teams_ordered
    Teams = soup.select('span[class*="text-of"]')
    for i in range(1, (len(Teams))):
        if Teams[0] == Teams[(i)]:
            TotalTeams = i
            print("Total Teams Found: ", TotalTeams)
            break
    for y in range(TotalTeams):
         teams_ordered.append(str(Teams[y]))
         teams_ordered[y] = re.findall("([\^A-Z]\w+)", teams_ordered[y])
            
GetTeams()
print(teams_ordered)
Tables_Agents_Data = soup.find_all('table', class_='wf-table')
def remove_ugly_COMPS(active_ugly):
    for i in range(2):
        killkillkill = active_ugly.i.extract()
        killkillkill = active_ugly.a.extract()
    return active_ugly

def Get_Agents_Picked_Pos(MapNum):
    Sent_data = []
    global Tables_Agents_Data
    useindex = MapNum + 1

    Active_Soup = Tables_Agents_Data[useindex].find('tr', class_='pr-matrix-row')
    Cleaned_Soup = remove_ugly_COMPS(Active_Soup)
    for i in range(len(Cleaned_Soup)):
        if Cleaned_Soup.contents[i] != '\n':
            Sent_data.append(Cleaned_Soup.contents[i])
    for i in range(2):
        Sent_data.pop(0)
        Sent_data.pop(-1)
    for i in range(19):
        Sent_data[i] = str(Sent_data[i])
        if Sent_data[i] == '<td class="">\n</td>':
            Sent_data[i] = 0
        else:
            Sent_data[i] = 1
    return Sent_data

def Comp_finder(WorkingSet):
    global Agents
    for i in range(19):
        if WorkingSet[i] == 1:
            WorkingSet[i] = Agents[i]
        else:
            WorkingSet[i] = 'Not Picked'
    return WorkingSet
            
    
Fracture_Picks = Get_Agents_Picked_Pos(0)
Comp_finder(Fracture_Picks)
print(Fracture_Picks)