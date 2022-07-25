#!/usr/bin/env python
# coding: utf-8

# Quest -- Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) using the first timestamp as the starting point.
# 
# This question sounds like it should be a SQL question, doesn’t it? Weekly aggregation implies a form of GROUP BY in a regular SQL or pandas question. In either case, aggregation on a dataset of this form by week would be pretty trivial.
# 
# But since it’s a scripting question, it’s trying to pry out if the candidate deals with unstructured data. Data scientists deal with a lot of unstructured data.
# 
# O/p - [['2019-01-01', '2019-01-02'],
#  ['2019-01-08'],
#  ['2019-02-01', '2019-02-02'],
#  ['2019-02-05']]

# In[33]:


import pandas as pd

ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
]

ts_1 = pd.DataFrame(ts, columns = ["date"])
ts_1['week'] = pd.to_datetime(ts_1.date).dt.week
ts_1.groupby('week')['date'].apply(list).tolist()


# In[ ]:




