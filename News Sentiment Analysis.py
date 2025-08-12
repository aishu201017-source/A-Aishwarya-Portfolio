#!/usr/bin/env python
# coding: utf-8

# In[2]:


import feedparser
import torch
import matplotlib.pyplot as plt


# In[3]:


from transformers import pipeline
pipe = pipeline("text-classification", model="ProsusAI/finbert")


# In[4]:


get_ipython().system('pip install hf_xet')


# In[62]:


ticker = 'GC=F'
keyword = 'Gold'


# In[63]:


RSS_url = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=US&lang=en-US"


# In[64]:


feed = feedparser.parse(RSS_url)


# In[65]:


print(len(feed.entries))
for e in feed.entries:
    print(e.title)


# In[66]:


positive_count = 0
neutral_count = 0
negative_count = 0

Total_Score = 0
Num_articles = 0


# In[67]:


for i, entry in enumerate(feed.entries):
    if keyword.lower() not in entry.summary.lower():
        continue

    print(f'Title:{entry.title}')
    print(f'Link:{entry.link}')
    print(f'Published:{entry.published}')
    print(f'Summary:{entry.summary}')

    sentiment = pipe(entry.summary)[0]

    print(f'Sentiment:{sentiment['label']},Score:{sentiment['score']}')
    print('-'*50)

    if sentiment['label'] == 'positive':
        positive_count += 1
        Total_Score += sentiment['score']
        Num_articles += 1
    elif sentiment['label'] == 'negative':
        negative_count += 1
        Total_Score -= sentiment['score']
        Num_articles += 1
    else:
        neutral_count += 1


# In[68]:


if Num_articles > 0:
    Final_Score = Total_Score / Num_articles
else:
    Final_Score = 0 


# In[69]:


labels = ['Positive', 'Neutral', 'Negative']
counts = [positive_count, neutral_count, negative_count]

colors = ['#98FB98',  # Pale Green
          '#FFFF99',  # Pale Yellow
          '#FFB6C1'] 

plt.figure(figsize=(8, 5))
plt.bar(labels, counts,color=colors)
plt.title(f"Sentiment Distribution of {keyword}")
plt.xlabel("Sentiment")
plt.ylabel("Number of Articles")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[70]:


print(f'Overall Sentiment = {"Positive" if Final_Score > 0.15 else "Negative" if Final_Score < -0.15 else "Neutral"}{' '}{Final_Score}')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




