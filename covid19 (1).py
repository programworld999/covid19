#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import requests
from bs4 import BeautifulSoup as BS
import json


# In[3]:


url = "https://ncov.dxy.cn/ncovh5/view/en_pneumonia?from=dxy&source=&link=&share="
page = requests.get(url)


# In[4]:


soup = BS(page.content, 'html.parser')
ByCountry = soup.find('script', attrs = {'id':'getListByCountryTypeService2true'})


# In[5]:


ByCountry = ByCountry.text[48:]
ByCountry = ByCountry[:-11]


# In[6]:


ByCountry = str(ByCountry)
ByCountry = ByCountry.replace("Syrian\xa0ArabRepublic", "Syrian Arab Republic")
ByCountry = ByCountry.replace("'", '"')
ByCountry = json.loads(ByCountry)


# In[7]:


globalData = soup.find('script', attrs = {'id':'getStatisticsService'})

globalData = globalData.text[36:]
globalData = globalData[:-11]
globalData = json.loads(str(globalData))


# In[8]:


globalStatistics = globalData["globalStatistics"]
print("World Wide: Confirmed: ", globalStatistics['confirmedCount'], "| Active: ", globalStatistics['currentConfirmedCount'], "| Death: ", globalStatistics['deadCount'], "| Recovered: ", globalStatistics['curedCount'])


# In[14]:


for ByCountrys in ByCountry:
    print(ByCountrys["countryFullName"], ": \033[1;33;40m Confirmed: ", ByCountrys['confirmedCount'], "\033[0m|\033[1;35;40m Active: ", ByCountrys['currentConfirmedCount'], "\033[0m|\033[0;37;41m Death: ", ByCountrys['deadCount'], "\033[0m|\033[1;32;40m Recovered: ", ByCountrys['curedCount'], "\033[0m")


# In[10]:


def searchByCountry(country):
    for ByCountrys in ByCountry:
        if(ByCountrys["countryFullName"] == country):
            print(ByCountrys["countryFullName"], ": \033[1;33;40m Confirmed: ", ByCountrys['confirmedCount'], "\033[0m|\033[1;35;40m Active: ", ByCountrys['currentConfirmedCount'], "\033[0m|\033[0;37;41m Death: ", ByCountrys['deadCount'], "\033[0m|\033[1;32;40m Recovered: ", ByCountrys['curedCount'], "\033[0m")
            return 0
    print("Country Name Wrong!")


# In[11]:

while(1):
  searchByCountry(input("Country Name: "))





