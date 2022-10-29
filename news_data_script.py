#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:55:54 2022

@author: jamescarney
"""

import pandas as pd
import seaborn as sns
sns.set()

from dateutil.parser import parse

import matplotlib.pyplot as plt

import plotly.express as px

news = pd.read_pickle('/Users/jamescarney/Desktop/Teaching_T1_2022/Qual_1a/processed_news.pkl')

news = news[['date', 'headline', 'source', 'section', 'valence', 'arousal', 'dominance', 'concreteness', 'semantic_size']]

news = news[news['section'].str.len() < 10]

day = pd.read_pickle('/Users/jamescarney/Desktop/Teaching_T1_2022/Qual_1a/processed_news_grouped_by_day.pkl')



news['source'] = news['source'].replace(['inews',
 'daily_mail',
 'express',
 'guardian',
 'evening_standard',
 'independent'], ['iNews',
  'Daily Mail',
  'Express',
  'Guardian',
  'Evening Standard',
  'Independent'])

plt.figure(figsize=(30,15))
h = sns.pointplot(x = 'section', y = 'arousal', join = False, data = news)
plt.xticks(rotation = 45, ha = 'right')

h.get_figure().savefig('/Users/jamescarney/Desktop/Teaching_T1_2022/Qual_1a/section_plot.png', dpi = 300)



plt.figure(figsize=(8,4))
h = sns.pointplot(x = 'source', y = 'valence', join = False, data = news)
plt.xticks(rotation = 45, ha = 'right')

plt.tight_layout()
h.get_figure().savefig('/Users/jamescarney/Desktop/Teaching_T1_2022/Qual_1a/title_plot_valence.png', dpi = 300)



immi = []

for i in news['headline']:
    if 'immig ' in i.lower():
        immi.append('mentions immigration')
    else:
        immi.append("doesn't mention immigration")
        
news['immigration'] = immi


future = []

for i in news['headline']:
    if 'future ' in i.lower():
        future.append('mentions future')
    else:
        future.append("doesn't mention future")
        
news['future'] = future




meghan = []

for i in news['headline']:
    if 'meghan' in i.lower():
        meghan.append('mentions meghan')
    else:
        meghan.append("doesn't mention meghan")
        
news['meghan'] = meghan



kate = []

for i in news['headline']:
    if 'kate' in i.lower():
        kate.append('mentions kate')
    else:
        kate.append("doesn't mention kate")
        
news['kate'] = kate


brexit = []

for i in news['headline']:
    if 'brexit' in i.lower():
        brexit.append('mentions brexit')
    else:
        brexit.append("doesn't mention brexit")
        
news['brexit'] = brexit


musk = []

for i in news['headline']:
    if 'musk' in i.lower():
        musk.append('mentions musk')
    else:
        musk.append("doesn't mention musk")
        
news['musk'] = musk


plt.figure(figsize=(8,4))
h = sns.pointplot(x = 'source', y = 'arousal', hue = 'immigration', join = False, data = news)
plt.xticks(rotation = 45, ha = 'right')

plt.tight_layout()
h.get_figure().savefig('/Users/jamescarney/Desktop/Teaching_T1_2022/Qual_1a/title_plot_imi_valence.png', dpi = 300)


plt.figure(figsize=(8,4))
h = sns.pointplot(x = 'source', y = 'valence', hue = 'immigration', join = False, data = news)
plt.xticks(rotation = 45, ha = 'right')

plt.tight_layout()
h.get_figure().savefig('/Users/jamescarney/Desktop/Teaching_T1_2022/Qual_1a/title_plot_imi_valence.png', dpi = 300)


immig = news[news['immigration'] == "mentions immigration"].reset_index(drop = True)

#immig['date'] = [parse(i) for i in immig['date']]


immig['arousal rolling mean'] = immig['arousal'].rolling(100).mean()
immig['valence rolling mean'] = immig['valence'].rolling(100).mean()

plt.figure(figsize=(8,4))
h = sns.lineplot(x = 'date', y = 'arousal rolling mean', hue = 'source', data = immig)
sns.move_legend(h, "upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
h.get_figure().savefig('/Users/jamescarney/Desktop/Teaching_T1_2022/Qual_1a/arousal_over_time_by_title.png', dpi = 300)


plt.figure(figsize=(8,4))
h = sns.lineplot(x = 'date', y = 'valence rolling mean', hue = 'source', data = immig)
sns.move_legend(h, "upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
h.get_figure().savefig('/Users/jamescarney/Desktop/Teaching_T1_2022/Qual_1a/valence_over_time_by_title.png', dpi = 300)






clt = pd.read_excel('/Users/jamescarney/Downloads/CU_CLT_Anxiety_Survey_Data.xlsx')

dvs = ['Impact_me',
'Day_to_day_life', 'Next_6_months', 'Prevent_the_impact',
'Changes_in_my_life', 'Need_to_make_changes']

results = []

for i in dvs:
    md = smf.mixedlm(i+' ~ Climate_anxious', clt, groups=clt["Stimulus"]).fit()
    results.append(md.summary())
    
for i in dvs:
    md = smf.mixedlm(i+' ~ Anxiety_Score', clt, groups=clt["Stimulus"]).fit()
    results.append(md.summary())
    
    
with open("/Users/jamescarney/Downloads/CU_CLT_results.txt", "a") as f:
    f.write('Linear Mixed Model Results\n\n\n')
    

for i in results:
    with open("/Users/jamescarney/Downloads/CU_CLT_results.txt", "a") as f:
        f.write("\n\n\'"+i.as_text())
        
    



































