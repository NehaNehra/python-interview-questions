#!/usr/bin/env python
# coding: utf-8

# Questions - 
# Given an integer array arr, write a function decreasing_values to return an array of integers so that the subsequent integers in the array get filtered out if they are less than an integer in a later index of the array.
# 
# Example 1:
# 
# arr = [20,17,19,18,12,16,10,4,6,3]
# 
# def decreasing_values(arr) -> [20,19,18,16,10,6,3]
# 
# Example 2:
# 
# arr = [25,30,21,22,14,10,5,26]
# 
# def decreasing_values(arr) -> [30,26]
# 

# In[41]:


def decreasing_values(arr):
    list1 = []
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            list1.append(arr[i])
        else:
            continue
    list1.append(arr[-1])
    return(list1)
            
            

    


# In[43]:


arr = [20,17,19,18,12,16,10,4,6,3]

decreasing_values(arr)


# In[ ]:




