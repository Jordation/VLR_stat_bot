from bs4 import BeautifulSoup
import re
Agents = []
with open("testpage.html") as testpage:
    soup = BeautifulSoup(testpage, "html.parser")

y = soup.select("div img", class_="wf-card mod-dark mod-table mod-scroll")

for z in range(1,20):
    Agents.append(y[z])

Agents[0] = str(Agents[0])
print(Agents[0])
print(type(Agents[0]))

