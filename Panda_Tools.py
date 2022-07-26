import statistics
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import pandas as pd



def get_average(inlist):
    return inlist.mean()


data_in = pd.read_csv('out.csv')
data_in.set_index('Name')
acs_ave = get_average(data_in["Average Combat Score"])

print(data_in.loc[(data_in["Average Combat Score"] > acs_ave) & (data_in["Agents Played"]=='astra')])
