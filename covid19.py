#!/usr/bin/env python
# coding: utf-8

# In[114]:


import os
import requests
from bs4 import BeautifulSoup as BS
import json


# In[115]:


url = "https://ncov.dxy.cn/ncovh5/view/en_pneumonia?from=dxy&source=&link=&share="
page = requests.get(url)


# In[116]:


soup = BS(page.content, 'html.parser')
ByCountry = soup.find('script', attrs = {'id':'getListByCountryTypeService2true'})


# In[117]:


ByCountry = ByCountry.text[48:]
ByCountry = ByCountry[:-11]


# In[118]:


ByCountry = str(ByCountry)
ByCountry = ByCountry.replace("Syrian\xa0ArabRepublic", "Syrian Arab Republic")
ByCountry = ByCountry.replace("'", '"')
ByCountry = json.loads(ByCountry)


# In[119]:


globalData = soup.find('script', attrs = {'id':'getStatisticsService'})

globalData = globalData.text[36:]
globalData = globalData[:-11]
globalData = json.loads(str(globalData))


# In[136]:


globalStatistics = globalData["globalStatistics"]
print("World Wide: Confirmed: ", globalStatistics['confirmedCount'], "| Active: ", globalStatistics['currentConfirmedCount'], "| Death: ", globalStatistics['deadCount'], "| Recovered: ", globalStatistics['curedCount'])


# In[137]:


for ByCountrys in ByCountry:
    print(ByCountrys["countryFullName"], ": Confirmed: ", ByCountrys['confirmedCount'], "| Active: ", ByCountrys['currentConfirmedCount'], "| Death: ", ByCountrys['deadCount'], "| Recovered: ", ByCountrys['curedCount'])


# In[142]:


def searchByCountry(country):
    for ByCountrys in ByCountry:
        if(ByCountrys["countryFullName"] == country):
            print(ByCountrys["countryFullName"], ": Confirmed: ", ByCountrys['confirmedCount'], "| Active: ", ByCountrys['currentConfirmedCount'], "| Death: ", ByCountrys['deadCount'], "| Recovered: ", ByCountrys['curedCount'])
            return 0
    print("Country Name Wrong!")


# In[151]:


searchByCountry(input("Country Name: "))


# In[147]:


ByCountry[0]


# In[149]:


from IPython.display import Image
imgsrc = "https://img1.dxycdn.com/2020/0319/685/3402856849412997239-135.png"
Image(filename='example.png')

