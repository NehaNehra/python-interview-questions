#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#write a Python program to swap first and last element of the list.


# write a Python program to swap first and last element of the list.
# 
# Examples: 
# 
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
# 
# Input : [1, 2, 3]
# Output : [3, 2, 1]

# In[1]:


def swapp(newlist):
    size = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1]=temp
    return newlist
    


# In[2]:


newlist = [12, 35, 9, 56, 24] 
swapp(newlist)


# In[ ]:




