#!/usr/bin/env python
# coding: utf-8

# Questions - 
# Fibonacci Series - The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# 

# In[15]:


def fib(n):
    fib_series= []
    for i in range(0,n):
        if i==0:
            fib_series.append(i)
        elif i==1:
            fib_series.append(i)
        else :
            temp = fib_series[i-2]+fib_series[i-1]
            fib_series.append(temp)
    return fib_series


# In[16]:


fib(11)


# In[ ]:




