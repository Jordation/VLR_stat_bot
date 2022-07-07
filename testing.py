from glob import glob
from hashlib import new
from turtle import pos
from xml.sax.handler import all_properties
from bs4 import BeautifulSoup
import re
import asyncio

with open("newtest.html") as testpage:
    soup = BeautifulSoup(testpage, "html.parser")
    
allcomps = soup.find('div', class_="pr-matrix-map")
print(len(list(allcomps.descendants)))
newshit = list(allcomps.descendants)
print(newshit)
on the 139'th comma, build a regex thing to target this start, pop all list items until this, once td null tag is reached, begin popping again and finding correct portions, eventually cna do the /19 trick









# for i in range(len(agentspicked)):
#     if agentspicked[i] == '\\n' or ' <td class="null"></td>':
#         print(agentspicked[i])
#          agentspicked.pop(i)