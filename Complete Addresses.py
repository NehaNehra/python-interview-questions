#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a function complete_address to create a single dataframe with complete addresses in the format of street, city, state, zip code.


# Question ==>> Complete Addresses https://www.interviewquery.com/questions/complete-addresses
# 
# You’re given two dataframes. One contains information about addresses and the other contains relationships between various cities and states
# 
# 
# Example:
# 
# df_addresses
# 
# address
# 4860 Sunset Boulevard, San Francisco, 94105
# 3055 Paradise Lane, Salt Lake City, 84103
# 682 Main Street, Detroit, 48204
# 9001 Cascade Road, Kansas City, 64102
# 5853 Leon Street, Tampa, 33605
# df_cities
# 
# city	state
# Salt Lake City	Utah
# Kansas City	Missouri
# Detroit	Michigan
# Tampa	Florida
# San Francisco	California
# 
# Write a function complete_address to create a single dataframe with complete addresses in the format of street, city, state, zip code.
# 
# 
# output-
# 
# address
# 4860 Sunset Boulevard, San Francisco, California, 94105
# 3055 Paradise Lane, Salt Lake City, Utah, 84103
# 682 Main Street, Detroit, Michigan, 48204
# 9001 Cascade Road, Kansas City, Missouri, 64102
# 5853 Leon Street, Tampa, Florida, 33605
# 

# In[11]:


adresses = {"address": ["4860 Sunset Boulevard, San Francisco, 94105", "3055 Paradise Lane, Salt Lake City, 84103", "682 Main Street, Detroit, 48204", "9001 Cascade Road, Kansas City, 64102", "5853 Leon Street, Tampa, 33605"]}
cities = {"city":["Salt Lake City", "Kansas City", "Detroit", "Tampa", "San Francisco"],"state":["Utah", "Missouri", "Michigan", "Florida", "California"]}

df_adresses = pd.DataFrame(adresses)
df_cities = pd.DataFrame(cities)


# In[12]:


print("Address------\n", df_adresses)
print("Cities------\n", df_cities)


# In[13]:


#print(add) 
add = []
dictt = {}
lst = len(df_adresses.address.values)
convt_dict = 0
for i in df_adresses.address:
    temp = i.split(",")
    add.append(temp)
print(add)
    


# In[14]:


split_add = pd.DataFrame(add, columns = ['street_add', 'city','pin_code'])


# In[17]:


print("Table of having split address-----\n", split_add)


# In[18]:


# to remove trailing & leading spaces
split_add['city']= split_add['city'].str.strip()
split_add['pin_code']= split_add['pin_code'].str.strip()
split_add['street_add']= split_add['street_add'].str.strip()


# In[19]:


# perform merge ----

address_city_merge= pd.merge(split_add,df_cities, how = 'inner', left_on = 'city', right_on = 'city')


# In[20]:


address_city_merge


# In[21]:


# concate the address fields
address_new = address_city_merge.street_add + "," + address_city_merge.city + "," + address_city_merge.state + "," + address_city_merge.pin_code


# In[22]:


address_new1 = pd.DataFrame(address_new, columns = ['address'])


# In[23]:


# To set/increase the table size so that can see the values
address_new1.style.set_properties(subset=['address'], **{'width-min': '300px'})


# In[ ]:




