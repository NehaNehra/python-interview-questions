#!/usr/bin/env python
# coding: utf-8

# -------Question------
# 
# Let’s say you’re given a huge 100 GB log file. You want to be able to count how many lines are in the file. 
# Write code in Python to count the total number of lines in the file.

# In[ ]:


# Opening a file
file = open("text.txt","r")
Count = 0
file_read = file.read()
List = file_read.split("\n")
for i in List:
    if i:
        Count += 1
          
print("Number of lines in the file")
print(Count)

