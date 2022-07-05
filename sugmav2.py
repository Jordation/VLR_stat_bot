from glob import glob
from bs4 import BeautifulSoup
import re

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

List_AllData = []
for i in range(0, 19):
    List_AllData.append({'Agent':Agents[i], 'Pickrate':GlobalPickRates[i]})
#print(List_AllData)
zz = soup.find_all("span", class_="map-pseudo-icon", limit=7)
print(zz)
    


#for i in range(0, 19):
#    print(Agents[i] + "'s pickrate is " + GlobalPickRates[i])



#print(len(GlobalWRs))
#print(len(MapPR))
