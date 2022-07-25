import statistics
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import requests
d1={'Name': 'tester1', 'shit': 'dontcare' }
d2={'Name': 'tester1', 'shit': 'dontcare' }
d3={'Name': 'tester3', 'shit': 'dontcare' }
d4={'Name': 'tester2', 'shit': 'dontcare' }
d5={'Name': 'tester2', 'shit': 'dontcare' }
d6={'Name': 'tester3', 'shit': 'dontcare' }
d7={'Name': 'tester1', 'shit': 'dontcare' }
d8={'Name': 'tester2', 'shit': 'dontcare' }
d9={'Name': 'tester1', 'shit': 'dontcare' }
listy=[d1,d2,d3,d4,d5,d6,d7,d8,d9]
#def Find_Unique_Names(bigasslist):
#    newlist = [x['Name'] for x in bigasslist]
#    player_names = list(set(newlist))
#    new2=[]
#    for i in range(len(player_names)):
#        playerlist=[x for x, enumerate(bigasslist) if x['Name'] == player_names[i]]
#    new2.append(playerlist)
#    return newlist
#print(Find_Unique_Names(listy))

#result = [(index, item) for index, item in enumerate(listy)]
#print(result)