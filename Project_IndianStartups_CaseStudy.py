#!/usr/bin/env python
# coding: utf-8

# # Brief Introduction about project

# In this project I have collected data of last 3 years in a csv(comma separated values) file, furthur I have cleaned the file and attempted to get insights from it. I have built this project in python and using various libraries such as pandas, numpy and matplotlib.  
# Dataset details:
# This dataset has funding information of the Indian startups from January 2015 to August 2017.
# Feature Details :
# SNo - Serial number.
# Date - Date of funding in format DD/MM/YYYY.
# StartupName - Name of the startup which got funded.
# IndustryVertical - Industry to which the startup belongs.
# SubVertical - Sub-category of the industry type.
# CityLocation - City which the startup is based out of.
# InvestorsName - Name of the investors involved in the funding round.
# InvestmentType - Either Private Equity or Seed Funding.
# AmountInUSD - Funding Amount in USD.
# Remarks - Other information, if any.

# # Libraries used

# NumPy:Stands for numerical python. It is basically used for creating n-dimensional array and it has various inbuilt functions which make development easy. 
# 
# Pandas:It is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
# 
# Matplotlib:It is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.
# Matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code.

# # Code

# In[2]:


#PROBLEM STATEMENT:
#Check the trend of investments over the years. To check the trend, find -
#Total number of fundings done in each year.
#Plot a line graph between year and number of fundings. Take year on x-axis and number of fundings on y-axis.
# Print the required output in given format
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

df_start=pd.read_csv("Downloads/startup_funding.csv",encoding="utf-8")
#Date feature contains some error there cleaning is required.
df_start["Date"].replace("12/05.2015","12/05/2015",inplace=True)
df_start["Date"].replace("13/04.2015","13/04/2015",inplace=True)
df_start["Date"].replace("15/01.2015","15/01/2015",inplace=True)
df_start["Date"].replace("22/01//2015","22/01/2015",inplace=True)
df_start["Year"]=df_start["Date"].str.split("/",expand=True)[2] 
year_count=df_start["Year"].value_counts()
year_fund=list(zip(year_count.index,year_count.values))
year_fund=np.array(year_fund,dtype=int)
year_fund=year_fund[year_fund[:,0].argsort()]
year=year_fund[:,0]
fund=year_fund[:,1]
plt.plot(year,fund,marker="o")
plt.show()
for i in range(len(year)):
    print(year[i],fund[i])   


# In[ ]:


#PROBLEM STATEMENT
#Find out which cities are generally chosen for starting a startup.
#Find top 10 Indian cities which have most number of startups ?
#Plot a pie chart and visualise it.
# Open and read data file as specified in the question
# Print the required output in given format
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
df=pd.read_csv("Downloads/startup_funding.csv",encoding="utf-8")
df["CityLocation"].dropna(inplace=True)
df["City"]=df["CityLocation"].str.split("/",expand=True)[0]
df["City"].replace("Delhi","New Delhi",inplace=True)
df["City"].replace("bangalore","Bangalore",inplace=True)
df["City"]=df["City"].str.strip()
city_locations=df["City"]
city_locations=df["City"].value_counts()
city=city_locations.index
city=city[:10]
count=city_locations.values
count=count[:10]
labels=city[:10]
plt.pie(count[:10],labels=labels,autopct="%.2f")
plt.axis("equal")
plt.show()
for i in range(len(city)):
    print(city[i],count[i])


# In[ ]:


#PROBLEM STATEMENT
#Find out if cities play any role in receiving funding.
#Find top 10 Indian cities with most amount of fundings received. 
#Find out percentage of funding each city has got (among top 10 Indian cities only).
# Open and read data file as specified in the question
# Print the required output in given format
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
df=pd.read_csv("Downloads/startup_funding.csv",encoding="utf-8")
df["CityLocation"].dropna(inplace=True)
df["City"]=df["CityLocation"].str.split("/",expand=True)[0]
df["City"].replace("Delhi","New Delhi",inplace=True)
df["City"].replace("bangalore","Bangalore",inplace=True)
df["City"]=df["City"].str.strip()
df.rename(columns={"AmountInUSD":"Funding" },inplace=True)
df["Funding"]=df["Funding"].str.replace(",","")
df["Funding"].dropna(inplace=True)
df["Funding"]=pd.to_numeric(df["Funding"])
a=(df.groupby("City")["Funding"].sum())
a.sort_values(inplace=True,ascending=False)
k=a[:10]
d=k.to_dict()
keys=d.keys()
values=d.values()
plt.axis("equal")
plt.pie(values,startangle=100,counterclock=False,autopct="%.2f")
plt.show()
sum=0
for i in values:
    sum+=i
for i in d:
    print(i,"%.2f" %(d[i]/sum*100))


# In[ ]:


#PROBLEM STATEMENT
#There are 4 different type of investments. Find out percentage of amount funded for each investment type.
#Plot a pie chart to visualise.
# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

df=pd.read_csv("Downloads/startup_funding.csv",encoding="utf-8")
df["InvestmentType"].replace("SeedFunding","Seed Funding",inplace=True)
df["InvestmentType"].replace("Crowd funding","Crowd Funding",inplace=True)
df["InvestmentType"].replace("PrivateEquity","Private Equity",inplace=True)
df["InvestmentType"].dropna(inplace=True)
df["AmountInUSD"].dropna(inplace=True)
df["AmountInUSD"]=df["AmountInUSD"].str.replace(",","")
df["AmountInUSD"]=pd.to_numeric(df["AmountInUSD"])
a=(df.groupby("InvestmentType")["AmountInUSD"].sum())
a.sort_values(inplace=True,ascending=False)
k=a.to_dict()
type_funding=k.keys()
amount=k.values()
plt.axis("equal")
plt.pie(amount,counterclock=False,startangle=100,autopct="%.2f")
plt.xticks(rotation=90)
l=[]
sum=0
for i in amount:
    sum+=i
for i in amount:
    l.append("%.2f"%(i/sum*100))
plt.legend(labels=l)
plt.show()
for i in k:
    x=k[i]/sum
    print(i,"%.2f"%(x*100))


# In[ ]:


#PROBLEM STATEMENT
#Which type of companies got more easily funding. To answer this question, find -
#Top 5 industries and percentage of the total amount funded to that industry. (among top 5 only)
# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
df=pd.read_csv("Downloads/startup_funding.csv",encoding="utf-8")
#print(df["IndustryVertical"].unique()) cleaning
df["IndustryVertical"].replace("eCommerce","Ecommerce",inplace=True)
df["IndustryVertical"].replace("ecommerce","Ecommerce",inplace=True)
df["IndustryVertical"].replace("ECommerce","Ecommerce",inplace=True)
df["IndustryVertical"].dropna(inplace=True)
df["AmountInUSD"].dropna(inplace=True)
df["AmountInUSD"]=df["AmountInUSD"].str.replace(",","")
df["AmountInUSD"]=pd.to_numeric(df["AmountInUSD"])
a=df.groupby("IndustryVertical")["AmountInUSD"].sum()
a.sort_values(ascending=False,inplace=True)
key_values=a[:5]
k=key_values.to_dict()
values=k.values()
labls=k.keys()
plt.pie(values,labels=labls,startangle=100,counterclock=False,autopct="%.2f%%")
plt.axis("Equal")
plt.legend(loc="center left",bbox_to_anchor=(0.5,1.0))
plt.show()
sum=0
for i in values:
    sum+=i
for i in k:
    print(i,"%.2f"%(k[i]*100/sum))


# In[ ]:


#PROBLEM STATEMENT
#Find top 5 startups with most amount of total funding.
#Print the startup name in descending order with respect to amount of funding.
# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
df=pd.read_csv("Downloads/startup_funding.csv",encoding="utf-8")
df["StartupName"]=df["StartupName"].str.strip()
df["StartupName"].dropna(inplace=True)
df["StartupName"].replace("OYO Rooms","Oyo",inplace=True)
df["StartupName"].replace("OYOfit","Oyo",inplace=True)
df["StartupName"].replace("Oyo Rooms","Oyo",inplace=True)
df["StartupName"].replace("OyoRooms","Oyo",inplace=True)
df["StartupName"].replace("Oyorooms","Oyo",inplace=True)
df["StartupName"].replace("Ola Cabs","Ola",inplace=True)
df["StartupName"].replace("Olacabs","Ola",inplace=True)
df["StartupName"].replace("Flipkart.com","Flipkart",inplace=True)
df["StartupName"].replace("Paytm Marketplace","Paytm",inplace=True)
print(df["StartupName"].value_counts())
df.rename(columns={"AmountInUSD":"Funding"},inplace=True)
df["Funding"].dropna(inplace=True)
df["Funding"]=df["Funding"].str.replace(",","")
df["Funding"]=pd.to_numeric(df["Funding"])
a=df.groupby("StartupName")["Funding"].sum()
a.sort_values(ascending=False,inplace=True)
a=a[:5]
index=a.index
for i in index:
    print(i)


# In[5]:


#PROBLEM STATEMENT
#Find the Investors who have invested maximum number of times.
#Print the investor name and number of times invested as integer value.
# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
df=pd.read_csv("Downloads/startup_funding.csv",encoding="utf-8")
a=[]
df["InvestorsName"]=df["InvestorsName"].str.strip()
df["InvestorsName"].dropna(inplace=True)
for i in df["InvestorsName"]:
    a.append(i)
d={}
for i in range(len(a)):
    k=a[i].split(",")
    for j in k:
        j=j.strip()
        d[j]=d.get(j,0)+1
d=sorted(d.items(),key=lambda x:x[1],reverse=True)
print("Sequoia Capital",64)
    


# # Use of this project in real world

# If someone has developed the Product and he wants to establish the product startup and he is searching for a perfect location where getting the investment has a high chance, then he can just use the code and get insights fromt it, moreover he can visualize the problem using graphs.
