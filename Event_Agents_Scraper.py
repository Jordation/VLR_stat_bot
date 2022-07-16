from http.client import OK
from pydoc import getpager
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import re
import requests

url = "https://www.vlr.gg/event/agents/1014/valorant-champions-tour-stage-2-masters-copenhagen"
def Get_Page(url):
    ActivePage = requests.get(url)
    return ActivePage.text

active_Page = Get_Page(url)
theSOUP = BeautifulSoup(active_Page, "html.parser")

def get_map_order():
    pass

def get_agent_order():
    pass



def get_pick_rates():
    #table class="wf-table mod-pr-global"
    pass
def deal_with_mod_right():
    #instantly copy out and delete this data so that map and overall funcs can work with just the relevant objects
    #td class="mod-right"
    pass
def find_overall_pickrates():
    #tr class="pr-global-row mod-all"
    #td class="mod-color-sq"
    pass
def find_map_pickrates():
    #tr class="pr-global-row "
    #td class="mod-color-sq"
    pass
def find_side_winrate_playedn():
    #uses list that i filled over the course of the function with deal_with_mod_right
    pass



def prepare_soup_comps():
    #cut out shit i dont need early, map/agent info should be saved from above already
    pass



def get_comps():
    #div class="pr-matrix-map"
    pass
def find_teams_picks_overall():
    #tr class="pr-matrix-row"
    #td class="mod-picked"
    pass
def find_oponent_WL_compPlayed():
    #td class="mod-loss"
    #tr class="pr-matrix-row mod-dropdown"
    #td class="mod-picked-lite"
    pass



def group_teams_compPlayed():
    pass