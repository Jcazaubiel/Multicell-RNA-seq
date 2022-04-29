#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os
import pandas as pd
import re


# In[19]:


with open('SN_filenames.txt','r') as f:
    filenames = []
    IDs = []

    for line in f:
        name = line.strip()
        ID = name[22:30]
        
        if(ID not in IDs):
            filenames.append(name)
            IDs.append(ID)


# In[8]:


data = pd.read_csv('SN_assignments.csv')

# Get the cluster assignments as integers
column = ['2_clusters', '4_clusters', '16_clusters', '64_clusters', '128_clusters']
for i in range(data.shape[0]):
    for j in range(2, data.shape[1]):
        name = data.iloc[i, j]
        name = int(re.search(r'\d+', name).group())
        data.iloc[i,j] = name
        
for col in column:
    data[col] = data[col].astype(int)


# In[9]:


nums = [2, 4, 16, 64, 128]

list_names = []
lists = []

for i in range(2, data.shape[1]):
    for j in range(nums[i-2]):
        list_name = 'N' + str(nums[i-2]) + 'c' + str(j)
        vars() [list_name] = data.index[data[column[i-2]] == j].tolist()
        list_names.append(list_name)
        lists.append(vars() [list_name])


# In[10]:


# Get all the file names for each cluster into a text file
# Necessary to bypass the limit on command character length
for i in range(len(list_names)):
    files = ''
    name = list_names[i] + '.txt'
    output = list_names[i] + '.fastq.gz'
    for j in range(len(lists[i])):
        files = files + filenames[lists[i][j]] + ' '
    
    command = 'cat ' + files + ' > ' + output
    os.system(command)


# In[ ]:




