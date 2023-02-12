# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:20:16 2023

@author: hp
"""

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


data = pd.read_excel('articles.xlsx')

#summary of the data

data.describe()
data.info()
data.head()


# examples of grouping then summing or counting

data.groupby(data['source_name']).size().sort_values(ascending = False)
data.groupby(data['source_id'])['engagement_reaction_count'].sum().sort_values(ascending = False)


#dropping one table


data = data.drop('engagement_comment_plugin_count' , axis = 1)





def word_in_title(key):
    key_flag = []; 
    for x in range(0,len(data)):
        title = data['title'][x];
        try:
            if key in title:
                flag=1;
            else:
                flag=0;
        except:
            flag = 0;
        key_flag.append(flag);
    return key_flag
        
data['Keyword_flag'] = word_in_title('murder')

#SentimentIntensityAnalyzer
sentiment_app = SentimentIntensityAnalyzer();


sentiment_app.polarity_scores(data['title'][16])['neu'] 


#adding a for loop to extract sentiment per title
neg = [];
pos = [];
neu = [];

for x in range(len(data)):
    try:
        neg.append(sentiment_app.polarity_scores(data['title'][x])['neg'])
        pos.append(sentiment_app.polarity_scores(data['title'][x])['pos'])
        neu.append(sentiment_app.polarity_scores(data['title'][x])['neu'])
    except:
        neg.append(0)
        pos.append(0)
        neu.append(0)
    
data['negative_sentiment'] = neg;
data['positive_sentiment'] = pos;
data['neutral_sentiment'] = neu;
    


#exporting

data.to_excel('sentiment_analysis_cleaned.xlsx', sheet_name='blog_me_data' , index= False)

































