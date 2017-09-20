
# coding: utf-8

# In[87]:


import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS")
c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class":"propertyRow"})

all[0].find("h4", {"class":"propPrice"}).text.replace("\n", "").replace(" ", "")
page_n = soup.find_all("a", {"class" : "Page"})[-1].text


# In[88]:


l = []

base_url = "http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#T=0&S=0.html"
for page in range(0, int(page_n) * 10, 10):
    print(base_url + str(page) + ".html")
    r = requests.get(base_url + str(page) + ".html")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class" : "propertyRow"})

    for item in all:
        d = {}
        d["Address"] = item.find_all("span", {"class":"propAddressCollapse"})[0].text
        try:
            d["Locality"] = item.find_all("span", {"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"] = None
        d["Price"] = item.find("h4", {"class":"propPrice"}).text.replace("\n", "").replace(" ", "")
        try:
            d["Beds"] = item.find("span", {"class":"infoBed"}).find("b").text
        except:
            d["Beds"] = None
        try:
            d["Area"] = item.find("span", {"class":"infoSqFt"}).find("b").text
        except:
            d["Area"] = None
        try:
            d["Full Baths"] = item.find("span", {"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None
        try:
            d["Half Baths"] = item.find("span", {"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None
        for column_group in item.find_all("div", {"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}), column_group.find_all("span", {"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)


# In[81]:


import pandas

df = pandas.DataFrame(l)


# In[89]:


df


# In[90]:


df.to_csv("Output.csv")


# In[ ]:




