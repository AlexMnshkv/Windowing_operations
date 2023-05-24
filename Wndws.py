#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10), sharey='col', sharex=True)



df=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_6/avocado_mean.csv')
df1=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_6/avocado_full.csv',index_col=0, parse_dates=['Date'])


# In[2]:


df1


# In[4]:


avocado_mean=df.AveragePrice
avocado_mean


# In[6]:


# Посчитаем скользящее среднее цены авокадо  с окном равным 3
avocado_mean.rolling(window=3).mean().max()


# In[13]:


# построиv графики скользящего среднего с разными значениями параметра window (2, 4, 10, 50)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10), sharey='col', sharex=True)

window = [2, 4, 10, 50]
colors = ['blue', 'coral', 'green', 'purple']

for window, ax, color in zip(windows, axes.flatten(), colors): 
    ax.plot(avocado_mean.rolling(window=window).mean(), label=window, color=color)


# In[18]:


# подсчитаем экспоненциальное скользящее среднее
df.groupby('Date').agg({'AveragePrice':sum}).ewm(span=2).mean()


# In[4]:


df1


# In[85]:


# df2=df1.groupby(['region','type'],as_index = False).agg({'AveragePrice':'count'})
df7=df1.loc[(df1['region']=='Chicago') & (df1['type'] =='organic')]
df7


# In[100]:


avoewm=df7.ewm(span=4).mean().round(3).reset_index()
avoewm.Date=pd.to_datetime(avoewm.Date)
avoewm[ "AveragePrice"].plot(figsize=( 12 , 8 ))
# avoewm.plot()


# In[ ]:





# In[101]:


avoroll=df7.rolling(window=4).mean().round(3).reset_index()
avoroll.Date=pd.to_datetime(avoroll.Date)
avoroll[ "AveragePrice"].plot(figsize=( 12 , 8 ))
avoewm[ "AveragePrice"].plot(figsize=( 12 , 8 ))


# sns.barplot(avoroll.AveragePrice,avoroll.Date)
# sns.distplot(avoroll.AveragePrice)
# sns.distplot(avoroll.Date)


# In[83]:


avoroll.AveragePrice.mean()


# In[84]:


avoewm.AveragePrice.mean()


# In[ ]:


df7=df1.loc[(df1['region']=='Chicago') & (df1['type'] =='organic')]


# In[115]:


avoroll.loc[(avoroll['Date']=='2017-02-19')]


# In[116]:


avoewm.loc[(avoewm['Date']=='2017-02-19')]


# In[113]:


avoroll.sort_values('Date')[52:104]


# In[114]:


avoewm.sort_values('Date')[52:104]


# In[117]:


# Считаем данные
df=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_6/delays.csv')
df


# In[118]:


df.dtypes


# In[132]:


# переведем delay в timedelta формат
df['delay']=df.delay.str.replace('-', '')

df.delay = pd.to_timedelta(df.delay)
# , format='%d %H:%M:%S')


# In[133]:


df


# In[145]:


# Разобьем колонку на 3 интервала
df['delay_categorical']=pd.cut(df.delay, bins=3)
# delay_categorical=pd.cut(df,3)


# In[143]:


df


# In[183]:



sp=pd.to_timedelta(['0d', '1d', '2d','3d','106751 days 23:47:16.854775'])

df['delay_categorical']=pd.cut(df.delay, bins=sp, labels=['less than 1 day', '1-2 days', '2-3 days', 'more than 3 days'])

# ff = pd.Series(labels)
# labels=['less than 1 day', '1-2 days', '2-3 days', 'more than 3 days']
# pd.to_timedelta(df.delay)


# In[189]:


df1=df.groupby('delay_categorical', as_index=False).agg({'revenue':'count'})


# In[190]:


# построим барплот с тем, насколько часто задерживаются сделки.
sns.barplot(data=df1, x=df1.delay_categorical, y=df1.revenue)


# In[ ]:




