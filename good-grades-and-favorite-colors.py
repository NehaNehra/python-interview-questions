#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a function named grades_colors to select only the rows where the student’s favorite color is green or red and their grade is above 90.


# QUESTIONS => https://www.interviewquery.com/questions/good-grades-and-favorite-colors
# 
# You’re given a dataframe of students named students_df:
# students_df table
# 
# name	age	favorite_color	grade
# Tim Voss	19	red	91
# Nicole Johnson	20	yellow	95
# Elsa Williams	21	green	82
# John James	20	blue	75
# Catherine Jones	23	green	93
# 
# Quest => Write a function named grades_colors to select only the rows where the student’s favorite color is green or red and their grade is above 90.

# In[3]:


def grades_colors(students):
    temp =students[students['favorite_color'].isin(['red','green'])]
    return temp[temp['grade']>90]
    


# In[4]:


import pandas as pd

students = {"name" : ["Tim Voss", "Nicole Johnson", "Elsa Williams", "John James", "Catherine Jones"], "age" : [19, 20, 21, 20, 23], "favorite_color" : ["red", "yellow", "green", "blue", "green"], "grade" : [91, 95, 82, 75, 93]}

students_df = pd.DataFrame(students)


# In[9]:


print("Orginal Table ----\n", students_df)


# In[10]:


# Print the output -----
print("Output -------\n", grades_colors(students_df))


# In[ ]:




