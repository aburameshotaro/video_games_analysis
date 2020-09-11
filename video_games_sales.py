# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 07:18:22 2020

@author: user
"""

import plotly.express as px
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from plotly.offline import plot

pd.set_option('display.max_columns', None)
df = pd.read_csv('./data/vgsales.csv')

# %%

df.head()
df.describe()
df.describe(include=['object'])
df.nlargest(10,columns='EU_Sales')
df.query('Platform=="PC"').nsmallest(10, columns='Rank')

# %%

sns.catplot(data=df[:500], x='Genre', y='Global_Sales', kind='box')
sns.catplot(data=df, x='Genre', kind='count')
sns.catplot(data=df, x='Platform', kind='count')

# %%

fig = px.scatter(data_frame=df, x='Year', y='Global_Sales', color='Genre', 
                 hover_name='Name', hover_data='Platform')
plot(fig)

# %%

fig = px.parallel_categories(df[df.Rank<=1000])
plot(fig)

# %%
data = df.Genre.value_counts()
import plotly.graph_objects as go

fig = go.Figure(data=[go.Pie(
        labels = data.index,
        values = data
    )])
plot(fig)

# %%

fig = px.pie(df, names='genres')
plot(fig)

# %%

fig = px.histogram(df, x='Year', color = 'Genre')
plot(fig)

# %%

data= df.query("Platform =='PC'")
data_rpg = data.query("Genre == 'Role-Playing'")
fig = px.histogram(data, x='Year', color='Genre')
best_PC_games = data.nsmallest(20, 'Rank')
plot(fig)

# %%

data_xbox = df.query("Platform == 'X360'")
