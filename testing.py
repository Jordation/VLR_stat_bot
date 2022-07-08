from glob import glob
from hashlib import new
from turtle import pos
from xml.sax.handler import all_properties
from bs4 import BeautifulSoup
import re
import asyncio

with open("testing.html") as testpage:
    soup = BeautifulSoup(testpage, "html.parser")
    
# allcomps = soup.find_all('table', class_="wf-table")
# newshit = allcomps[0].find_all('td')
# newershit = newshit.select(".pr-matrix-row ~ td")
# print(newershit)
aaaaaa = soup.select("[class~=pr-matrix-row]")
print(aaaaaa[0])




#2-19-4-19-2-19-2etc

# print(len(newshit))


# If none of the other matches work for you, define a function that takes an element as its only argument. The function should return True if the argument matches, and False otherwise.

# Here’s a function that returns True if a tag defines the “class” attribute but doesn’t define the “id” attribute:


# for i in range(len(agentspicked)):
#     if agentspicked[i] == '\\n' or ' <td class="null"></td>':
#         print(agentspicked[i])
#          agentspicked.pop(i)