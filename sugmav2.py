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

#GMO_Pattern = re.compile("([\^A-Z]\w+)")
GetMapOrder = soup.select('td[style*="white-space: nowrap; padding-top: 0; padding-bottom: 0;"]')
MapOrder_PickRates = []
MapOrder_Comps = []
for i in range(1,8):
    MapOrder_PickRates.append(GetMapOrder[i])
    MapOrder_PickRates[(i-1)] = str(MapOrder_PickRates[(i-1)])
    MapOrder_PickRates[(i-1)] = re.findall("([\^A-Z]\w+)", MapOrder_PickRates[(i-1)])

List_AllData = []
for i in range(0, 19): #dict maker
    List_AllData.append({'Agent':Agents[i], 'Pickrate':GlobalPickRates[i]})

list_allpicks = []
PickRateByMap = soup.select('tr div span')
print(len(PickRateByMap))
for i in range(len(PickRateByMap)):
    list_allpicks.append(PickRateByMap[i])
    list_allpicks[i] = str(list_allpicks[i])
    list_allpicks[i] = re.findall("([0-9]+%)", list_allpicks[i])
print(list_allpicks)
List_PR_by_map = []
for i in range(7):
    for y in range((i*19),(i+1)*19):
            if i < 1:
                List_PR_by_map.append({'Agent':Agents[y],'Pickrate':list_allpicks[y]})
            else:
                List_PR_by_map.append({'Map':MapOrder_PickRates[i], 'Agent':Agents[(y%19)],'Pickrate':list_allpicks[y]})
                
print(List_PR_by_map)


#zz = soup.find_all("span", class_="map-pseudo-icon", limit=7)
#print(zz)