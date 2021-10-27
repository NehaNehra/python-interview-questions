#!/usr/bin/env python
# coding: utf-8

# -------Question------
# 
# Write a function compute_deviation that takes in a list of dictionaries with a key and list of integers and returns a dictionary with the standard deviation of each list.
# 
# Note that this should be done without using the numpy built in functions.
# 
# Example:
# 
# input = [
#     {
#         'key': 'list1',
#         'values': [4,5,2,3,4,5,2,3],
#     },
#     {
#         'key': 'list2',
#         'values': [1,1,34,12,40,3,9,7],
#     }
# ]
# 
# output -> {'list1': 1.12, 'list2': 14.19}

# In[67]:


def list_dev(var):
    list1 = {}
    for i,j in enumerate(input):
        y_mean= sum(j['values'])/len(j['values'])
        y_dev = sum([(x-y_mean)**2 for x in j['values']])/len(j['values'])
        y_dev1=y_dev**0.5
        list1[j["key"]] = round(y_dev1,2)
    print(list1)

    


# In[68]:


input = [
    {
        'key': 'list1',
        'values': [4,5,2,3,4,5,2,3],
    },
    {
        'key': 'list2',
        'values': [1,1,34,12,40,3,9,7],
    }
]

list_dev(input)


# In[ ]:




