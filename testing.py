from asyncore import loop
from curses import getwin
from glob import glob
from bs4 import BeautifulSoup
import re
import asyncio

with open("testing.html") as testpage:
    soup = BeautifulSoup(testpage, "html.parser")
    
#def FindComps(tag):
agentspicked = []
position = soup.find('tr', attrs={"class": "pr-matrix-row"})

for children in position.children:
    agentspicked.append(children)
for i in range(5,):
    agentspicked.pop(0)
print(agentspicked)
    