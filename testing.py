from asyncore import loop
from curses import getwin
from glob import glob
from turtle import pos
from bs4 import BeautifulSoup
import re
import asyncio

with open("newtest.html") as testpage:
    soup = BeautifulSoup(testpage, "html.parser")
    
#def FindComps(tag):
agentspicked = []
ALLpickdata = soup.select('td[class*="mod-picked"]')


print(len(ALLpickdata))
# for i in range(len(agentspicked)):
#     if agentspicked[i] == '\\n' or ' <td class="null"></td>':
#         print(agentspicked[i])
#         agentspicked.pop(i)