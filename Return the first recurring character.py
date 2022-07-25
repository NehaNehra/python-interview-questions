#!/usr/bin/env python
# coding: utf-8

# Question- 
# Given a string, return the first recurring character in it, or None if there is no recurring chracter.

# In[46]:


def firstchar(strr):
    rec_lst = []
    for i in strr:
        if i in rec_lst:
            return i
        else:
            rec_lst.append(i)
            
    return '\0'
        


# In[57]:


strr ="interviewquery"
firstchar(strr)


# In[ ]:




