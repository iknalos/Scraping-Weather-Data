
import requests
from bs4 import BeautifulSoup
page=requests.get("https://weather.com/weather/tenday/l/Boston+MA?canonicalCityId=6320cadd3d539b434b5a45c094becf3edbe8ea88958185a2287a801115c9ae30")
content=page.content
soup=BeautifulSoup(content,"html.parser")
l=[]
all=soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text
 

table=soup.find_all("table",{"class":"twc-table"})
for items in table:
	for i in range(len(items.find_all("tr"))-1):
		d = {}
		try:
			d["day"]=items.find_all("span",{"class":"date-time"})[i].text
			d["date"]=items.find_all("span",{"class":"day-detail"})[i].text			
			d["desc"]=items.find_all("td",{"class":"description"})[i].text
			d["temp"]=items.find_all("td",{"class":"temp"})[i].text
			d["precip"]=items.find_all("td",{"class":"precip"})[i].text
			d["wind"]=items.find_all("td",{"class":"wind"})[i].text
			d["humidity"]=items.find_all("td",{"class":"humidity"})[i].text
		except:
			d["day"]="None"
			d["date"]="None"
			d["desc"]="None"
			d["temp"]="None"
			d["precip"]="None"
			d["wind"]="None"
			d["humidity"]="None"
		#print("")
		l.append(d)

import pandas
df = pandas.DataFrame(l)
print df.dtypes
print(df)
df.to_csv('output.csv', header=True, index=False, encoding='utf-8')


# In[8]:

type(df['date'][0])


# In[12]:

ig, ax = plt.subplots(figsize=(10, 10))

# Add the x-axis and the y-axis to the plot
ax.plot(df['date'],
        df['precip'],
        color='purple')

# Set title and labels for axes
ax.set (xlabel="Date",
       ylabel="Temperature (Fahrenheit)",
       title="Precipitation Weather, Boston in december 2019)
[Text(0, 0.5, 'Temperature (Fahrenheit)'),
 Text(0.5, 0, 'Date'),
 Text(0.5, 1.0, 'Precipitation\nBoulder, Colorado in July 2018')]


# In[ ]:



