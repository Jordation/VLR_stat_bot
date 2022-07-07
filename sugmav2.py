from asyncore import loop
from curses import getwin
from glob import glob
from bs4 import BeautifulSoup
import re
import asyncio

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

map_agent_pickrate= []
for i in range(8):
    for y in range((i*19),(i+1)*19):
            if i < 1:
                map_agent_pickrate.append({'Agent':Agents[y],'Pickrate':raw_pickrates[y]})
            else:
                map_agent_pickrate.append({'Map':MapOrder_PickRates[i-1], 'Agent':Agents[(y%19)],'Pickrate':raw_pickrates[y]})

teams_order = []
def GetTeams():
    global teams_order
    Teams = soup.select('span[class*="text-of"]')
    for i in range(1, (len(Teams))):
        if Teams[0] == Teams[(i)]:
            TotalTeams = i
            break
    for y in range(TotalTeams):
         teams_order.append(str(Teams[y]))
         teams_order[y] = re.findall("([\^A-Z]\w+)", teams_order[y])
GetTeams()

agentspicked = []
ALLpickdata = soup.select('td[class*="mod-picked"]')
for i in range(19):
    agentspicked.append(ALLpickdata[i])
    agentspicked[i] = str(agentspicked[i])
    
team_map_picked = []
for i in range(19):
    pass