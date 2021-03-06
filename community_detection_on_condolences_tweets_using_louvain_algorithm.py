# -*- coding: utf-8 -*-
"""Community Detection On Condolences-Tweets Using Louvain Algorithm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cXmAMHj73NWvDxRzGh4XAvaViRyozcGX
"""

!pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint

import twint
import pandas as pd
import numpy as np
import nest_asyncio
import networkx as nx
import matplotlib.pyplot as plt
nest_asyncio.apply()

c = twint.Config()

c.Search = "rip OR rest in peace"
c.Limit = 5000
c.Store_csv = True
c.Output = "tweetx.csv"

twint.run.Search(c)

tweets=pd.read_csv("tweetx.csv")
tweets

tweets=tweets[tweets['reply_to'] !='[]']
tweets['reply_to']=tweets['reply_to'].str[1:]
a=(tweets.assign(list=tweets["reply_to"].str.split(", ")).explode("list"))

c=a[a.list.str.contains("'screen")]

c['list']=c['list'].str[17:]
c['list']=c['list'].str[:-1]
#print(c.head())
c.to_csv(r'artru.csv')

G=nx.from_pandas_edgelist(c,source='username', target='list', create_using=nx.Graph())

import community
partition = community.best_partition(G)
pos = nx.spring_layout(G)  
plt.figure(figsize=(100, 100))
plt.axis('off')
#nx.draw_networkx_nodes(G, pos, node_size=600, label='username', cmap=plt.cm.RdYlBu, node_color=list(partition.values()))
#nx.draw_networkx_edges(G, pos, alpha=0.3)
nx.draw_networkx(G, pos, alpha=0.5, node_size=600, label='username', cmap=plt.cm.RdYlBu, node_color=list(partition.values()))
plt.savefig('hasli.png')
plt.show(G)

c.head()

list_par = max(list(partition.values()))
print(list_par)

dfp= pd.DataFrame(partition.items(), columns=['username','community'])
dfp.to_csv(r'dfp.csv')
dfp

dft['frequency']=dfp['community'].value_counts()
dft.to_csv(r'dft.csv')
dft.head(10)

